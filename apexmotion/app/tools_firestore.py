import os
import uuid
from typing import Any, Dict, List, Optional

# Hardcode project ID as string so deployed Reasoning Engine doesn't resolve to project number
PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"

try:
    from google.cloud import firestore
    SERVER_TIMESTAMP = firestore.SERVER_TIMESTAMP
except Exception:
    firestore = None
    SERVER_TIMESTAMP = "SERVER_TIMESTAMP"

# Seed exercises fallback for offline mode (on private computers without Google Cloud)
SEED_EXERCISES_OFFLINE = [
    {
        "id": "planche_tuck",
        "name": "Tuck Planche",
        "category": "skill_push",
        "target_muscles": ["anterior_delts", "chest", "core", "scapular_protractors"],
        "difficulty": "intermediate",
        "fatigue_factor": 7,
    },
    {
        "id": "front_lever_tuck",
        "name": "Tuck Front Lever",
        "category": "skill_pull",
        "target_muscles": ["lats", "rear_delts", "core", "scapular_retractors"],
        "difficulty": "intermediate",
        "fatigue_factor": 7,
    },
    {
        "id": "handstand_pushup_wall",
        "name": "Wall Handstand Push-up",
        "category": "push",
        "target_muscles": ["anterior_delts", "triceps", "upper_chest"],
        "difficulty": "advanced",
        "fatigue_factor": 8,
    },
    {
        "id": "weighted_pullup",
        "name": "Weighted Pull-Up",
        "category": "pull",
        "target_muscles": ["lats", "biceps", "rear_delts", "forearms"],
        "difficulty": "intermediate",
        "fatigue_factor": 8,
    },
    {
        "id": "v_sit_progression",
        "name": "L-Sit to V-Sit Hold",
        "category": "skill_core",
        "target_muscles": ["core", "hip_flexors", "triceps"],
        "difficulty": "intermediate",
        "fatigue_factor": 6,
    },
    {
        "id": "pistol_squat",
        "name": "Pistol Squat",
        "category": "legs",
        "target_muscles": ["quads", "glutes", "hamstrings", "calves"],
        "difficulty": "intermediate",
        "fatigue_factor": 7,
    },
    {
        "id": "nordic_curl",
        "name": "Nordic Hamstring Curl",
        "category": "legs",
        "target_muscles": ["hamstrings", "glutes", "calves"],
        "difficulty": "advanced",
        "fatigue_factor": 8,
    },
    {
        "id": "handstand_balance_hold",
        "name": "Freestanding Handstand Practice",
        "category": "accessory_balance",
        "target_muscles": ["anterior_delts", "traps", "forearms", "core"],
        "difficulty": "intermediate",
        "fatigue_factor": 4,
    },
    {
        "id": "wrist_and_shoulder_mobility_flow",
        "name": "Shoulder & Wrist Mobility Flow",
        "category": "accessory_mobility",
        "target_muscles": ["anterior_delts", "scapular_retractors", "forearms"],
        "difficulty": "beginner",
        "fatigue_factor": 1,
    },
    {
        "id": "deep_core_compression",
        "name": "Hollow Body & Compression Holds",
        "category": "accessory_core",
        "target_muscles": ["core", "hip_flexors"],
        "difficulty": "beginner",
        "fatigue_factor": 5,
    },
]


class _LocalDocumentSnapshotMock:
    def __init__(self, doc_id: str, data: Optional[Dict[str, Any]]):
        self.id = doc_id
        self._data = data

    @property
    def exists(self) -> bool:
        return self._data is not None

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._data) if self._data else {}


class _LocalDocumentRefMock:
    def __init__(self, collection_mock: Any, doc_id: str):
        self.collection_mock = collection_mock
        self.id = doc_id

    def get(self) -> _LocalDocumentSnapshotMock:
        data = self.collection_mock.store.get(self.id)
        return _LocalDocumentSnapshotMock(self.id, data)

    def set(self, data: Dict[str, Any], merge: bool = False) -> None:
        if merge and self.id in self.collection_mock.store:
            self.collection_mock.store[self.id].update(data)
        else:
            self.collection_mock.store[self.id] = dict(data)


class _LocalCollectionMock:
    def __init__(self, store: Dict[str, Any]):
        self.store = store

    def document(self, doc_id: Optional[str] = None) -> _LocalDocumentRefMock:
        if not doc_id:
            doc_id = f"auto_{uuid.uuid4().hex[:8]}"
        return _LocalDocumentRefMock(self, doc_id)

    def stream(self):
        for doc_id, data in list(self.store.items()):
            yield _LocalDocumentSnapshotMock(doc_id, data)


class _LocalFirestoreMock:
    """In-memory Firestore client that allows running 100% offline without Google Cloud."""
    def __init__(self):
        self._collections = {
            "exercises": {ex["id"]: dict(ex) for ex in SEED_EXERCISES_OFFLINE},
            "athlete_profiles": {
                "default_athlete": {
                    "athlete_id": "default_athlete",
                    "goal": "climbing & planche",
                    "skill_focus": ["planche", "front_lever"],
                    "muscle_exhaustion": {
                        "anterior_delts": 2,
                        "chest": 1,
                        "lats": 6,
                        "rear_delts": 5,
                        "core": 3,
                        "biceps": 6,
                        "triceps": 2,
                        "quads": 1,
                        "hamstrings": 1,
                    },
                    "last_workout_type": "pull",
                    "preferred_accessories": ["handstand", "stretching"],
                }
            },
            "workout_logs": {},
        }

    def collection(self, name: str) -> _LocalCollectionMock:
        if name not in self._collections:
            self._collections[name] = {}
        return _LocalCollectionMock(self._collections[name])


_GLOBAL_OFFLINE_STORE: Optional[_LocalFirestoreMock] = None


def _get_firestore_client() -> Any:
    """Returns Firestore client, with automatic fallback to local store if offline or no credentials."""
    global _GLOBAL_OFFLINE_STORE
    
    # If offline mode is requested or no GCP library is present
    if os.environ.get("APEXMOTION_OFFLINE_MODE") == "1" or firestore is None:
        if _GLOBAL_OFFLINE_STORE is None:
            _GLOBAL_OFFLINE_STORE = _LocalFirestoreMock()
        return _GLOBAL_OFFLINE_STORE

    try:
        return firestore.Client(project=PROJECT_ID)
    except Exception:
        # Graceful fallback for local machines/private PCs without Google Cloud setup
        if _GLOBAL_OFFLINE_STORE is None:
            _GLOBAL_OFFLINE_STORE = _LocalFirestoreMock()
        return _GLOBAL_OFFLINE_STORE


def list_exercises(category: Optional[str] = None, target_muscle: Optional[str] = None) -> List[Dict[str, Any]]:
    """Lists exercises and skills from the catalog, optionally filtered by category or muscle.

    Args:
        category: Optional category filter, e.g. 'push', 'pull', 'legs', 'skill_push', 'skill_pull',
                  'skill_core', 'accessory_balance', 'accessory_mobility'.
        target_muscle: Optional muscle to filter for, e.g. 'chest', 'anterior_delts', 'lats', 'core', 'quads', 'hamstrings'.

    Returns:
        A list of exercise dictionaries containing id, name, category, target_muscles, difficulty, and fatigue_factor.
    """
    db = _get_firestore_client()
    docs = db.collection("exercises").stream()
    results = []

    for doc in docs:
        data = doc.to_dict()
        if category and data.get("category") != category:
            continue
        if target_muscle:
            muscles = data.get("target_muscles", [])
            if target_muscle.lower() not in [m.lower() for m in muscles]:
                continue
        results.append(data)

    return results


def get_exercise_details(exercise_id: str) -> Dict[str, Any]:
    """Retrieves full details for a specific exercise from the catalog.

    Args:
        exercise_id: The unique identifier of the exercise (e.g. 'planche_tuck', 'front_lever_tuck', 'pistol_squat').

    Returns:
        A dictionary with the exercise details or an error message if not found.
    """
    db = _get_firestore_client()
    doc = db.collection("exercises").document(exercise_id).get()
    if not doc.exists:
        return {"error": f"Exercise '{exercise_id}' not found in catalog."}
    return doc.to_dict()


def get_muscle_exhaustion(athlete_id: str = "default_athlete") -> Dict[str, Any]:
    """Gets the current muscle exhaustion / fatigue scores (1-10) for an athlete.

    Args:
        athlete_id: The athlete identifier (defaults to 'default_athlete').

    Returns:
        A dictionary containing exhaustion scores per muscle group and the last workout type.
    """
    db = _get_firestore_client()
    doc = db.collection("athlete_profiles").document(athlete_id).get()
    if not doc.exists:
        # Default fresh baseline if profile does not exist yet
        return {
            "athlete_id": athlete_id,
            "muscle_exhaustion": {
                "anterior_delts": 0,
                "chest": 0,
                "lats": 0,
                "rear_delts": 0,
                "biceps": 0,
                "triceps": 0,
                "core": 0,
                "quads": 0,
                "hamstrings": 0,
            },
            "last_workout_type": "none",
        }
    return doc.to_dict()


def log_workout_session(
    workout_type: str,
    exercises_performed: List[Dict[str, Any]],
    rpe: int,
    accessory_performed: Optional[str] = None,
    notes: Optional[str] = None,
    athlete_id: str = "default_athlete",
) -> Dict[str, Any]:
    """Logs a completed workout session with RPE exhaustion and updates the athlete's muscle fatigue levels.

    Args:
        workout_type: Type of workout (e.g. 'push', 'pull', 'legs', 'planche_focused', 'front_lever_focused').
        exercises_performed: List of exercises performed. Each entry is a dict like:
            {"exercise_id": "planche_tuck", "sets": 4, "reps_or_seconds": 12}
        rpe: Rate of Perceived Exertion for the overall session on a scale of 1 to 10 (10 = absolute failure/exhaustion).
        accessory_performed: Optional post-workout accessory (e.g. 'yoga', 'stretching', 'abs', 'handstand').
        notes: Optional user notes or feelings about the session.
        athlete_id: The athlete identifier.

    Returns:
        A summary of the logged workout and the updated muscle exhaustion scores.
    """
    db = _get_firestore_client()
    
    # 1. Fetch current athlete profile
    profile_ref = db.collection("athlete_profiles").document(athlete_id)
    profile_doc = profile_ref.get()
    current_data = profile_doc.to_dict() if profile_doc.exists else {}
    current_exhaustion = current_data.get("muscle_exhaustion", {
        "anterior_delts": 0, "chest": 0, "lats": 0, "rear_delts": 0,
        "biceps": 0, "triceps": 0, "core": 0, "quads": 0, "hamstrings": 0,
    })

    # Decay prior fatigue slightly (representing rest period since last workout)
    for m in current_exhaustion:
        current_exhaustion[m] = max(0, current_exhaustion[m] - 2)

    # 2. Add fatigue based on exercises performed and RPE
    fatigue_increment = max(1, min(10, rpe)) // 2  # scale RPE into incremental fatigue (1 to 5)

    for item in exercises_performed:
        ex_id = item.get("exercise_id")
        if not ex_id:
            continue
        ex_doc = db.collection("exercises").document(ex_id).get()
        if ex_doc.exists:
            target_muscles = ex_doc.to_dict().get("target_muscles", [])
            for muscle in target_muscles:
                current_val = current_exhaustion.get(muscle, 0)
                current_exhaustion[muscle] = min(10, current_val + fatigue_increment)

    # 3. Save workout log
    workout_log = {
        "athlete_id": athlete_id,
        "workout_type": workout_type,
        "rpe": rpe,
        "exercises_performed": exercises_performed,
        "accessory_performed": accessory_performed,
        "notes": notes,
        "timestamp": SERVER_TIMESTAMP,
    }
    log_ref = db.collection("workout_logs").document()
    log_ref.set(workout_log)

    # 4. Update athlete profile
    profile_update = {
        "athlete_id": athlete_id,
        "muscle_exhaustion": current_exhaustion,
        "last_workout_type": workout_type,
        "last_accessory": accessory_performed,
    }
    profile_ref.set(profile_update, merge=True)

    return {
        "status": "success",
        "workout_log_id": log_ref.id,
        "workout_type": workout_type,
        "rpe": rpe,
        "accessory_performed": accessory_performed,
        "updated_muscle_exhaustion": current_exhaustion,
        "message": f"Workout successfully logged. Muscle fatigue updated based on RPE {rpe}."
    }
