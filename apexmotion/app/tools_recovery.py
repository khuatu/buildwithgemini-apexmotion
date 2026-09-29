"""Advanced recovery decay computation tool for muscle fatigue tracking."""

import datetime
import math
from typing import Any, Dict, Optional
from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"

# Muscle half-life recovery periods in hours
# Tendon/connective tissue heavy positions (planche/levers/knees) recover slower
MUSCLE_HALF_LIVES_HOURS: Dict[str, float] = {
    "anterior_delts": 36.0,
    "scapular_protractors": 36.0,
    "chest": 28.0,
    "upper_chest": 28.0,
    "triceps": 24.0,
    "lats": 36.0,
    "rear_delts": 28.0,
    "biceps": 24.0,
    "core": 20.0,
    "hip_flexors": 24.0,
    "quads": 36.0,
    "hamstrings": 40.0,
    "calves": 24.0,
    "forearms": 20.0,
}
DEFAULT_HALF_LIFE = 28.0


def _get_firestore_client() -> firestore.Client:
    return firestore.Client(project=PROJECT_ID)


def compute_recovery_decay(
    athlete_id: str = "default_athlete",
    simulated_hours_rest: Optional[float] = None,
    apply_to_profile: bool = True,
) -> Dict[str, Any]:
    """Computes exponential recovery decay of muscle fatigue across time and updates current status.

    Formula: Fatigue(t) = Initial_Fatigue * e^(-ln(2) * elapsed_hours / half_life)

    Args:
        athlete_id: Unique athlete ID (defaults to 'default_athlete').
        simulated_hours_rest: Optional custom elapsed rest hours to simulate (e.g. 24.0 for tomorrow's readiness).
                              If omitted, computes real elapsed time since the latest logged workout in Firestore.
        apply_to_profile: Whether to persist the recalculated fatigue levels to Firestore athlete profile (default: True).

    Returns:
        A dictionary containing:
        - elapsed_hours: Time period calculated
        - previous_exhaustion: Fatigue scores before decay
        - updated_exhaustion: Recalculated fatigue scores
        - readiness_status: High-level classification (ready_to_train, moderate_fatigue, needs_recovery) per muscle
        - recommended_focus: Suggested muscle groups and workout types based on freshness
    """
    db = _get_firestore_client()
    profile_ref = db.collection("athlete_profiles").document(athlete_id)
    profile_doc = profile_ref.get()

    if not profile_doc.exists:
        return {"error": f"Athlete profile '{athlete_id}' not found."}

    profile_data = profile_doc.to_dict()
    current_fatigue = profile_data.get("muscle_exhaustion", {})

    # Determine elapsed time
    if simulated_hours_rest is not None:
        elapsed_hours = float(simulated_hours_rest)
    else:
        # Check latest workout log timestamp
        logs_stream = (
            db.collection("workout_logs")
            .where(filter=firestore.FieldFilter("athlete_id", "==", athlete_id))
            .order_by("timestamp", direction=firestore.Query.DESCENDING)
            .limit(1)
            .stream()
        )
        logs = list(logs_stream)
        if logs and "timestamp" in logs[0].to_dict() and logs[0].to_dict()["timestamp"]:
            last_time = logs[0].to_dict()["timestamp"]
            now = datetime.datetime.now(datetime.timezone.utc)
            delta = now - last_time
            elapsed_hours = max(1.0, delta.total_seconds() / 3600.0)
        else:
            elapsed_hours = 24.0  # Default to 24h rest window

    updated_fatigue: Dict[str, int] = {}
    readiness: Dict[str, str] = {}
    fresh_muscles = []
    fatigued_muscles = []

    for muscle, initial_score in current_fatigue.items():
        half_life = MUSCLE_HALF_LIVES_HOURS.get(muscle, DEFAULT_HALF_LIFE)
        decay_constant = math.log(2) / half_life
        decayed_val = float(initial_score) * math.exp(-decay_constant * elapsed_hours)
        rounded_val = max(0, min(10, round(decayed_val)))
        updated_fatigue[muscle] = rounded_val

        if rounded_val <= 2:
            readiness[muscle] = "🟢 Fresh (100% Ready)"
            fresh_muscles.append(muscle)
        elif rounded_val <= 5:
            readiness[muscle] = "🟡 Moderate (Accessible for moderate volume)"
        else:
            readiness[muscle] = "🔴 Fatigued (Active recovery recommended)"
            fatigued_muscles.append(muscle)

    # Determine workout recommendations based on muscle readiness
    recommended_focus = []
    push_muscles = {"anterior_delts", "chest", "triceps"}
    pull_muscles = {"lats", "biceps", "rear_delts"}
    leg_muscles = {"quads", "hamstrings"}

    if push_muscles.issubset(set(fresh_muscles)):
        recommended_focus.append("Push / Planche Skill")
    if pull_muscles.issubset(set(fresh_muscles)):
        recommended_focus.append("Pull / Front Lever Skill")
    if leg_muscles.issubset(set(fresh_muscles)):
        recommended_focus.append("Legs / Lower Body Power")
    if not recommended_focus:
        recommended_focus.append("Active Recovery, Core & Mobility Flow")

    if apply_to_profile:
        profile_ref.set({"muscle_exhaustion": updated_fatigue}, merge=True)

    return {
        "status": "success",
        "athlete_id": athlete_id,
        "elapsed_hours": round(elapsed_hours, 1),
        "previous_exhaustion": current_fatigue,
        "updated_exhaustion": updated_fatigue,
        "readiness_status": readiness,
        "fresh_muscle_groups": fresh_muscles,
        "fatigued_muscle_groups": fatigued_muscles,
        "recommended_focus": recommended_focus,
    }
