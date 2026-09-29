# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.tools_firestore import (
    list_exercises,
    get_exercise_details,
    get_muscle_exhaustion,
    log_workout_session,
)
from app.tools_email import send_workout_email
from app.tools_recovery import compute_recovery_decay
from app.tools_visuals import generate_and_store_form_visual
from app.tools_wger import search_public_exercises
from app.tools_maps import geocode_address, search_nearby_places
from app.tools_image_gen import generate_exercise_image
from app.tools_video_gen import generate_exercise_video


MODEL = "gemini-3.6-flash"


def get_weather(query: str) -> str:
    """Simulates a web search. Use it get information on weather.

    Args:
        query: A string containing the location to get weather information for.

    Returns:
        A string with the simulated weather information for the queried location.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        return "It's 60 degrees and foggy."
    return "It's 90 degrees and sunny."


def get_current_time(query: str) -> str:
    """Simulates getting the current time for a city.

    Args:
        city: The name of the city to get the current time for.

    Returns:
        A string with the current time information.
    """
    if "sf" in query.lower() or "san francisco" in query.lower():
        tz_identifier = "America/Los_Angeles"
    else:
        return f"Sorry, I don't have timezone information for query: {query}."

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    return f"The current time for query {query} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"


from google.adk.agents.callback_context import CallbackContext
from google.adk.tools.preload_memory_tool import PreloadMemoryTool


async def generate_memories_callback(callback_context: CallbackContext):
    """WRITE: After each turn, sends session conversation to Memory Bank for extraction.

    Extracts durable facts about user muscle fatigues, favorable workouts, exercises, and dietary/food preferences.
    """
    await callback_context.add_session_to_memory()
    return None


from a2ui.schema.manager import A2uiSchemaManager
from a2ui.basic_catalog.provider import BasicCatalog
from app.a2ui_utils import a2ui_callback

ROLE_DESCRIPTION = """You are ApexMotion, an expert calisthenics and sport strength coach.
You have cross-session long-term memory powered by Vertex AI Memory Bank.
Always remember and personalize responses based on the athlete's recalled memory:
- Remember all stated muscle fatigue levels, soreness, and exhaustion history.
- Remember their favorable workouts, preferred training styles, favorite skills (planche, front lever, etc.), and calisthenics goals.
- Remember their food, nutrition, and dietary preferences (e.g. bulking, high-protein, calorie intake, favorite meals, allergies).

Your core duties:
1. Help athletes plan workouts differentiated by target muscle groups and calisthenics skills (e.g. planche, front lever, v-sit, push/pull/legs).
2. Inspect current muscle exhaustion levels using `get_muscle_exhaustion` or recalculate time-based decay using `compute_recovery_decay` to determine which muscle groups are fresh and which need recovery before recommending what to train next.
3. Suggest exercises and accessory cooldowns (yoga, mobility, stretching, abs, handstand practice) from the local catalog using `list_exercises` and `get_exercise_details`, or query the broader open-source exercise database using `search_public_exercises` (e.g. for general strength/gym variations).
4. Generate exercise illustrations or calisthenics movement images using `generate_exercise_image`. It automatically saves the image into Playground's Artifacts and uploads it to Cloud Storage, returning its public HTTPS URL.
5. Generate short demonstration videos of exercises or calisthenics skills using `generate_exercise_video`. It uses Google's Omni model (gemini-omni-flash-preview), automatically saves the video as a session artifact so it shows up in Playground's Artifacts panel, and uploads the raw video bytes to Cloud Storage, returning its public HTTPS URL.
6. Generate technical form cue diagrams or anatomy visual cards and publish them to Cloud Storage using `generate_and_store_form_visual` when explaining posture, alignment, or form cues.
7. Locate workout spots, calisthenics parks, gymnastics facilities, or gyms using `geocode_address` and `search_nearby_places`.
8. Send recommended workout plans to the user's email address using `send_workout_email` when requested or when delivering a tailored daily routine.
9. Log completed workout sessions along with an RPE (1-10) using `log_workout_session`, which automatically updates the athlete's muscle fatigue levels.
Always be encouraging, precise with muscle targeting, and mindful of recovery.
"""

schema_manager = A2uiSchemaManager(
    version="0.8",
    catalogs=[BasicCatalog.get_config("0.8")],
)

instruction = schema_manager.generate_system_prompt(
    role_description=ROLE_DESCRIPTION,
    workflow_description="Analyze the athlete's request, inspect recovery or workout needs, execute tools, and return structured UI when appropriate.",
    ui_description=(
        "Keep every surface tiny and flat: ONE Card > ONE Column > a few Text rows. "
        "Never nest a Card inside a Card. "
        "Use ONLY these components: Card, Column, Row, Text, and Image. Do not use "
        "Table or Heading (unsupported), or Buttons, actions, or forms (they do "
        "nothing in adk web). "
        "You may include one Image component, but only when you have a public https "
        "URL for the image (for example the URL an image tool returns after uploading "
        "to a public bucket). Set the Image url to that exact https link, for example "
        '{"Image": {"url": {"literalString": "https://..."}}}. Never point an '
        "Image at a bare filename, an artifact name, or a non-http(s) path. If you do "
        "not have a public URL, add a short Text line noting the image instead. "
        "No markdown in text; use the usageHint property ('h1', 'h2', 'body') for "
        "headings and emphasis. "
        "Output ONLY the raw A2UI JSON array — no prose, and never wrap it in "
        "<a2a_datapart_json> tags or 'kind'/'data'/'metadata' objects."
    ),
    include_schema=True,
    include_examples=True,
)

import json
from pathlib import Path
from google.adk.code_executors import AgentEngineSandboxCodeExecutor

# Read Agent Engine & Sandbox metadata from deployment_metadata.json
_METADATA_FILE = Path(__file__).resolve().parent.parent / "deployment_metadata.json"
_SANDBOX_RESOURCE_NAME = None
_AGENT_ENGINE_RESOURCE_NAME = "projects/536672091587/locations/us-east1/reasoningEngines/2175605856903626752"

if _METADATA_FILE.exists():
    try:
        with open(_METADATA_FILE, "r") as f:
            _meta = json.load(f)
            _SANDBOX_RESOURCE_NAME = _meta.get("sandbox_resource_name")
            _AGENT_ENGINE_RESOURCE_NAME = _meta.get("remote_agent_runtime_id", _AGENT_ENGINE_RESOURCE_NAME)
    except Exception:
        pass

code_executor = AgentEngineSandboxCodeExecutor(
    sandbox_resource_name=_SANDBOX_RESOURCE_NAME,
    agent_engine_resource_name=_AGENT_ENGINE_RESOURCE_NAME,
)

root_agent = Agent(
    name="root_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=instruction,
    code_executor=code_executor,
    after_model_callback=a2ui_callback,
    after_agent_callback=generate_memories_callback,
    tools=[
        PreloadMemoryTool(),
        list_exercises,
        get_exercise_details,
        get_muscle_exhaustion,
        compute_recovery_decay,
        generate_exercise_image,
        generate_exercise_video,
        generate_and_store_form_visual,
        search_public_exercises,
        geocode_address,
        search_nearby_places,
        log_workout_session,
        send_workout_email,
        get_weather,
        get_current_time,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
