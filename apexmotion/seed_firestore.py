"""Seed script for ApexMotion workout and exercise catalog in Firestore."""

from google.cloud import firestore

PROJECT_ID = "qwiklabs-gcp-03-746ba250987a"

SEED_EXERCISES = [
    {
        "id": "planche_tuck",
        "name": "Tuck Planche",
        "category": "skill_push",
        "target_muscles": ["anterior_delts", "chest", "core", "scapular_protractors"],
        "difficulty": "intermediate",
        "description": "Isometric hold with knees tucked to chest, arms straight, shoulders protracted.",
        "default_sets": 4,
        "default_hold_seconds": 12,
        "fatigue_factor": 7,
    },
    {
        "id": "front_lever_tuck",
        "name": "Tuck Front Lever",
        "category": "skill_pull",
        "target_muscles": ["lats", "rear_delts", "core", "scapular_retractors"],
        "difficulty": "intermediate",
        "description": "Horizontal hang from bar with knees tucked tight and back flat.",
        "default_sets": 4,
        "default_hold_seconds": 15,
        "fatigue_factor": 7,
    },
    {
        "id": "handstand_pushup_wall",
        "name": "Wall Handstand Push-up",
        "category": "push",
        "target_muscles": ["anterior_delts", "triceps", "upper_chest"],
        "difficulty": "advanced",
        "description": "Vertical pressing movement against a wall for vertical push power.",
        "default_sets": 3,
        "default_reps": 6,
        "fatigue_factor": 8,
    },
    {
        "id": "weighted_pullup",
        "name": "Weighted Pull-Up",
        "category": "pull",
        "target_muscles": ["lats", "biceps", "rear_delts", "forearms"],
        "difficulty": "intermediate",
        "description": "Compound vertical pulling movement with external load or bodyweight focus.",
        "default_sets": 4,
        "default_reps": 8,
        "fatigue_factor": 8,
    },
    {
        "id": "v_sit_progression",
        "name": "L-Sit to V-Sit Hold",
        "category": "skill_core",
        "target_muscles": ["core", "hip_flexors", "triceps"],
        "difficulty": "intermediate",
        "description": "Floor or parallette compression hold with legs elevated above parallel.",
        "default_sets": 4,
        "default_hold_seconds": 15,
        "fatigue_factor": 6,
    },
    {
        "id": "pistol_squat",
        "name": "Pistol Squat",
        "category": "legs",
        "target_muscles": ["quads", "glutes", "hamstrings", "calves"],
        "difficulty": "intermediate",
        "description": "Single-leg deep squat developing leg drive, balance, and knee stability.",
        "default_sets": 3,
        "default_reps": 8,
        "fatigue_factor": 7,
    },
    {
        "id": "nordic_curl",
        "name": "Nordic Hamstring Curl",
        "category": "legs",
        "target_muscles": ["hamstrings", "glutes", "calves"],
        "difficulty": "advanced",
        "description": "Eccentric knee flexion movement for hamstring strength and injury prevention.",
        "default_sets": 3,
        "default_reps": 6,
        "fatigue_factor": 8,
    },
    {
        "id": "handstand_balance_hold",
        "name": "Freestanding Handstand Practice",
        "category": "accessory_balance",
        "target_muscles": ["anterior_delts", "traps", "forearms", "core"],
        "difficulty": "intermediate",
        "description": "Low-fatigue skill practice focusing on line alignment, finger pressure, and balance.",
        "default_sets": 5,
        "default_hold_seconds": 20,
        "fatigue_factor": 4,
    },
    {
        "id": "wrist_and_shoulder_mobility_flow",
        "name": "Shoulder & Wrist Mobility Flow",
        "category": "accessory_mobility",
        "target_muscles": ["anterior_delts", "scapular_retractors", "forearms"],
        "difficulty": "beginner",
        "description": "End-of-workout wrist extensions, dislocates, and passive hangs for recovery.",
        "default_sets": 2,
        "default_hold_seconds": 60,
        "fatigue_factor": 1,
    },
    {
        "id": "deep_core_compression",
        "name": "Hollow Body & Compression Holds",
        "category": "accessory_core",
        "target_muscles": ["core", "hip_flexors"],
        "difficulty": "beginner",
        "description": "Posterior pelvic tilt hollow hold paired with seated pike compressions.",
        "default_sets": 3,
        "default_hold_seconds": 30,
        "fatigue_factor": 5,
    },
]


def seed():
    print(f"Connecting to Firestore with project: {PROJECT_ID}")
    db = firestore.Client(project=PROJECT_ID)
    collection_ref = db.collection("exercises")

    for item in SEED_EXERCISES:
        doc_id = item["id"]
        doc_ref = collection_ref.document(doc_id)
        doc_ref.set(item)
        print(f"Seeded exercise: {item['name']} ({doc_id})")

    # Also seed an initial athlete profile to demonstrate muscle recovery status
    profile_ref = db.collection("athlete_profiles").document("default_athlete")
    profile_data = {
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
    profile_ref.set(profile_data)
    print("Seeded default athlete profile (default_athlete)")
    print("Database seeding completed successfully!")


if __name__ == "__main__":
    seed()
