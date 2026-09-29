"""Video generation tool using gemini-omni-flash-preview in global region."""

import base64
import uuid
from typing import Any, Dict
from google import genai
from google.genai import types
from google.cloud import storage
from google.adk.tools import ToolContext

PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"
BUCKET_NAME = "apexmotion-coach-qwiklabs-gcp-03-746ba250987a"
LOCATION = "global"
MODEL_NAME = "gemini-omni-flash-preview"


def _get_storage_client() -> storage.Client:
    return storage.Client(project=PROJECT_ID)


async def generate_exercise_video(
    prompt: str,
    tool_context: ToolContext,
) -> Dict[str, Any]:
    """Generates a short video demonstrating an exercise or calisthenics skill.

    Uses Google's Omni model (gemini-omni-flash-preview) in the global region.
    Saves the video as a session artifact so it shows up in the Playground's Artifacts panel,
    and uploads the raw video bytes to the public Cloud Storage bucket.

    Args:
        prompt: A detailed prompt describing the exercise movement, calisthenics skill,
                cadence, and athletic technique (e.g., 'A calisthenics athlete performing a slow, controlled muscle-up on straight bar, side view, 4 seconds').
        tool_context: ADK ToolContext injected by the framework to persist artifacts.

    Returns:
        A dictionary containing the public Cloud Storage URL (https://storage.googleapis.com/<bucket>/<object>),
        artifact filename, and video metadata.
    """
    # 1. Generate video using gemini-omni-flash-preview via Interactions API
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
    interaction = client.interactions.create(
        model=MODEL_NAME,
        input=prompt,
        response_format={
            "type": "video",
        },
    )

    output_video = getattr(interaction, "output_video", None)
    if not output_video or not getattr(output_video, "data", None):
        return {
            "status": "error",
            "error": "No video data returned from model.",
        }

    raw_data = output_video.data
    # If the video data is a base64 string, decode to raw bytes
    if isinstance(raw_data, str):
        video_bytes = base64.b64decode(raw_data)
    elif isinstance(raw_data, bytes):
        video_bytes = raw_data
    else:
        video_bytes = bytes(raw_data)

    mime_type = getattr(output_video, "mime_type", None) or "video/mp4"
    filename = f"video_{uuid.uuid4().hex[:8]}.mp4"

    # 2. Save video as an ADK artifact so it appears in Playground's Artifacts panel
    video_part = types.Part(
        inline_data=types.Blob(
            mime_type=mime_type,
            data=video_bytes,
        )
    )
    await tool_context.save_artifact(
        filename=filename,
        artifact=video_part,
    )

    # 3. Upload the same video bytes to the public Cloud Storage bucket
    storage_client = _get_storage_client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob_path = f"generated_videos/{filename}"
    blob = bucket.blob(blob_path)
    blob.upload_from_string(video_bytes, content_type=mime_type)

    public_url = f"https://storage.googleapis.com/{BUCKET_NAME}/{blob_path}"

    return {
        "status": "success",
        "video_url": public_url,
        "artifact_filename": filename,
        "mime_type": mime_type,
        "bucket": BUCKET_NAME,
        "prompt": prompt,
    }
