"""Image generation tool using gemini-3.1-flash-lite-image in global region."""

import uuid
from typing import Any, Dict
from google import genai
from google.genai import types
from google.cloud import storage
from google.adk.tools import ToolContext

PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"
BUCKET_NAME = "apexmotion-coach-qwiklabs-gcp-03-746ba250987a"
LOCATION = "global"
MODEL_NAME = "gemini-3.1-flash-lite-image"


def _get_storage_client() -> storage.Client:
    return storage.Client(project=PROJECT_ID)


async def generate_exercise_image(
    prompt: str,
    tool_context: ToolContext,
) -> Dict[str, Any]:
    """Generates an exercise illustration or calisthenics skill visualization.

    Uses the gemini-3.1-flash-lite-image model in the global region.
    Saves the image as a session artifact for the Playground's Artifacts panel,
    and uploads the raw image bytes to the public Cloud Storage bucket.

    Args:
        prompt: A detailed prompt describing the exercise, calisthenics movement,
                muscle activation, or athletic posture (e.g., 'Athlete performing a clean Front Lever hold on rings, minimalist anatomical highlight on back and core').
        tool_context: ADK ToolContext injected by the framework to persist artifacts.

    Returns:
        A dictionary containing the public Cloud Storage URL (https://storage.googleapis.com/<bucket>/<object>),
        artifact filename, and image metadata.
    """
    # 1. Generate image using gemini-3.1-flash-lite-image in global region
    client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
        ),
    )

    image_part = None
    if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if part.inline_data and part.inline_data.data:
                image_part = part
                break

    if not image_part:
        return {
            "status": "error",
            "error": "No image data returned from model.",
        }

    image_bytes = image_part.inline_data.data
    mime_type = image_part.inline_data.mime_type or "image/png"
    ext = "jpg" if "jpeg" in mime_type else "png"
    filename = f"exercise_{uuid.uuid4().hex[:8]}.{ext}"

    # 2. Save image as an ADK artifact so it appears in Playground's Artifacts panel
    await tool_context.save_artifact(
        filename=filename,
        artifact=image_part,
    )

    # 3. Upload the same image bytes to the public Cloud Storage bucket
    storage_client = _get_storage_client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob_path = f"generated_exercises/{filename}"
    blob = bucket.blob(blob_path)
    blob.upload_from_string(image_bytes, content_type=mime_type)

    public_url = f"https://storage.googleapis.com/{BUCKET_NAME}/{blob_path}"

    return {
        "status": "success",
        "image_url": public_url,
        "artifact_filename": filename,
        "mime_type": mime_type,
        "bucket": BUCKET_NAME,
        "prompt": prompt,
    }
