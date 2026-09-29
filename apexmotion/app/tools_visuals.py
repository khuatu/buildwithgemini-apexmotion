"""Visual generation and Cloud Storage publishing tool for exercise technique and anatomy."""

import os
import uuid
from typing import Any, Dict, Optional
from google import genai
from google.genai import types
from google.cloud import storage

PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"
BUCKET_NAME = f"apexmotion-coach-{PROJECT_ID}"
LOCATION = "us-central1"  # Imagen 3 standard location


def _get_storage_client() -> storage.Client:
    return storage.Client(project=PROJECT_ID)


def generate_and_store_form_visual(
    exercise_name: str,
    focus_cue: str,
    target_muscle_highlight: Optional[str] = None,
    image_style: str = "technical_anatomy_diagram",
) -> Dict[str, Any]:
    """Generates an exercise form diagram or anatomical cue visualization and publishes it to Cloud Storage.

    Args:
        exercise_name: Name of the exercise or skill (e.g. 'Tuck Planche', 'Front Lever', 'Handstand').
        focus_cue: Key biomechanical or alignment cue to highlight (e.g. 'protracted scapulae and straight arms',
                   'neutral spine and tight posterior pelvic tilt', 'open shoulders with line alignment').
        target_muscle_highlight: Optional muscle group to visually emphasize (e.g. 'anterior deltoids', 'latissimus dorsi', 'core').
        image_style: Visual format, e.g. 'technical_anatomy_diagram', 'minimalist_calisthenics_infographic', or 'athletic_action_sketch'.

    Returns:
        A dictionary with the generated public image URL, GCS URI, and image metadata.
    """
    # 1. Synthesize detailed image prompt
    prompt = (
        f"A clean, professional {image_style} of a calisthenics athlete performing {exercise_name}. "
        f"Explicit visual focus on technique: {focus_cue}. "
    )
    if target_muscle_highlight:
        prompt += f"Highlight the {target_muscle_highlight} with a vibrant anatomical contour overlay. "
    prompt += "Minimalist studio gym or dark blueprint athletic background, high resolution, precise biomechanical posture."

    # 2. Attempt Imagen 3 generation via Vertex AI GenAI Client
    public_url = None
    gcs_uri = None
    file_id = f"visual_{exercise_name.lower().replace(' ', '_')}_{uuid.uuid4().hex[:6]}.jpg"

    try:
        client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
        result = client.models.generate_images(
            model="imagen-3.0-generate-002",
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                output_mime_type="image/jpeg",
                aspect_ratio="1:1",
            ),
        )
        if result.generated_images:
            image_bytes = result.generated_images[0].image.image_bytes

            # 3. Upload to public Cloud Storage bucket
            storage_client = _get_storage_client()
            bucket = storage_client.bucket(BUCKET_NAME)
            blob = bucket.blob(f"visuals/{file_id}")
            blob.upload_from_string(image_bytes, content_type="image/jpeg")

            public_url = f"https://storage.googleapis.com/{BUCKET_NAME}/visuals/{file_id}"
            gcs_uri = f"gs://{BUCKET_NAME}/visuals/{file_id}"

            return {
                "status": "success",
                "exercise_name": exercise_name,
                "focus_cue": focus_cue,
                "target_muscle_highlight": target_muscle_highlight,
                "image_public_url": public_url,
                "gcs_uri": gcs_uri,
                "message": f"Successfully generated and published form visual to Cloud Storage: {public_url}",
            }
    except Exception as e:
        # Fallback to SVG / High-res generated infographic banner if Imagen quota is unavailable in region
        storage_client = _get_storage_client()
        bucket = storage_client.bucket(BUCKET_NAME)
        blob = bucket.blob(f"visuals/{file_id}.svg")
        
        svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="350" viewBox="0 0 600 350">
          <defs>
            <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" style="stop-color:#1e293b;stop-opacity:1" />
              <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1" />
            </linearGradient>
          </defs>
          <rect width="600" height="350" fill="url(#grad)" rx="16"/>
          <text x="30" y="55" fill="#38bdf8" font-family="Arial, sans-serif" font-size="20" font-weight="bold">⚡ APEXMOTION FORM & TECHNIQUE CUE</text>
          <text x="30" y="110" fill="#f8fafc" font-family="Arial, sans-serif" font-size="28" font-weight="bold">{exercise_name}</text>
          <rect x="30" y="135" width="540" height="2" fill="#334155" />
          <text x="30" y="180" fill="#94a3b8" font-family="Arial, sans-serif" font-size="16">Key Alignment Cue:</text>
          <text x="30" y="215" fill="#e2e8f0" font-family="Arial, sans-serif" font-size="18" font-weight="bold">"{focus_cue}"</text>
          <rect x="30" y="250" width="220" height="40" rx="8" fill="#0284c7" />
          <text x="45" y="275" fill="#ffffff" font-family="Arial, sans-serif" font-size="14" font-weight="bold">Target: {target_muscle_highlight or 'Core & Stabilizers'}</text>
        </svg>"""
        
        blob.upload_from_string(svg_content, content_type="image/svg+xml")
        public_url = f"https://storage.googleapis.com/{BUCKET_NAME}/visuals/{file_id}.svg"
        gcs_uri = f"gs://{BUCKET_NAME}/visuals/{file_id}.svg"

        return {
            "status": "fallback_graphic_published",
            "exercise_name": exercise_name,
            "focus_cue": focus_cue,
            "target_muscle_highlight": target_muscle_highlight,
            "image_public_url": public_url,
            "gcs_uri": gcs_uri,
            "note": f"Visual infographic published to Cloud Storage ({e}).",
        }
