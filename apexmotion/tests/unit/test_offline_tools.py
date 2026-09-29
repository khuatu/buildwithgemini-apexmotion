"""Unit tests for ApexMotion tools running in 100% offline mode without Google Cloud credentials.

Verifies that list_exercises, get_exercise_details, get_muscle_exhaustion, and
log_workout_session function seamlessly on any private PC without GCP setup.
"""

import os
import sys
import unittest
from pathlib import Path

# Force offline mode for this test suite
os.environ["APEXMOTION_OFFLINE_MODE"] = "1"

# Ensure apexmotion directory is in sys.path regardless of CWD
apexmotion_dir = Path(__file__).resolve().parent.parent.parent
if str(apexmotion_dir) not in sys.path:
    sys.path.insert(0, str(apexmotion_dir))

from app.tools_firestore import (
    list_exercises,
    get_exercise_details,
    get_muscle_exhaustion,
    log_workout_session,
    SEED_EXERCISES_OFFLINE,
)



class TestApexMotionToolsOffline(unittest.TestCase):
    """Verifies all agent tool functions work completely offline without Google Cloud."""

    def test_list_exercises_all(self):
        """Should return all catalog exercises when no filter is applied."""
        exercises = list_exercises()
        self.assertGreaterEqual(len(exercises), 10)
        ids = [ex["id"] for ex in exercises]
        self.assertIn("planche_tuck", ids)
        self.assertIn("front_lever_tuck", ids)
        self.assertIn("pistol_squat", ids)

    def test_list_exercises_by_category(self):
        """Should filter exercises accurately by category."""
        push_exercises = list_exercises(category="skill_push")
        self.assertGreaterEqual(len(push_exercises), 1)
        for ex in push_exercises:
            self.assertEqual(ex["category"], "skill_push")

        legs_exercises = list_exercises(category="legs")
        self.assertGreaterEqual(len(legs_exercises), 2)
        for ex in legs_exercises:
            self.assertEqual(ex["category"], "legs")

    def test_list_exercises_by_muscle(self):
        """Should filter exercises containing the target muscle group."""
        lat_exercises = list_exercises(target_muscle="lats")
        self.assertGreaterEqual(len(lat_exercises), 2)
        for ex in lat_exercises:
            muscles_lower = [m.lower() for m in ex.get("target_muscles", [])]
            self.assertIn("lats", muscles_lower)

    def test_get_exercise_details_valid(self):
        """Should return full details for an existing exercise ID."""
        details = get_exercise_details("planche_tuck")
        self.assertNotIn("error", details)
        self.assertEqual(details["id"], "planche_tuck")
        self.assertEqual(details["name"], "Tuck Planche")
        self.assertIn("anterior_delts", details["target_muscles"])

    def test_get_exercise_details_invalid(self):
        """Should return an error dictionary when exercise is not found."""
        details = get_exercise_details("non_existent_skill_xyz")
        self.assertIn("error", details)

    def test_get_muscle_exhaustion_default_athlete(self):
        """Should retrieve default athlete profile and exhaustion scores."""
        profile = get_muscle_exhaustion("default_athlete")
        self.assertEqual(profile["athlete_id"], "default_athlete")
        self.assertIn("muscle_exhaustion", profile)
        exhaustion = profile["muscle_exhaustion"]
        self.assertIn("anterior_delts", exhaustion)
        self.assertIn("lats", exhaustion)
        self.assertIsInstance(exhaustion["lats"], int)

    def test_get_muscle_exhaustion_new_athlete_baseline(self):
        """Should provide fresh baseline (0 fatigue) for newly queried athlete."""
        profile = get_muscle_exhaustion("brand_new_athlete_42")
        self.assertEqual(profile["athlete_id"], "brand_new_athlete_42")
        self.assertIn("muscle_exhaustion", profile)
        exhaustion = profile["muscle_exhaustion"]
        for score in exhaustion.values():
            self.assertEqual(score, 0)

    def test_log_workout_session_rpe_accumulation_and_decay(self):
        """Should log workout, accumulate target fatigue, and decay other muscles."""
        # Baseline profile check
        before = get_muscle_exhaustion("default_athlete")["muscle_exhaustion"]
        before_delts = before["anterior_delts"]
        before_lats = before["lats"]

        # Log a Push workout with Tuck Planche at RPE 8
        # Fatigue increment for RPE 8: max(1, min(10, 8)) // 2 = 4
        # Planche targets anterior_delts, chest, core
        result = log_workout_session(
            workout_type="push",
            exercises_performed=[{"exercise_id": "planche_tuck", "sets": 4, "reps_or_seconds": 12}],
            rpe=8,
            accessory_performed="handstand",
            notes="Felt strong on tuck hold balance",
            athlete_id="default_athlete",
        )

        self.assertEqual(result["status"], "success")
        updated = result["updated_muscle_exhaustion"]

        # Prior rest decay subtracts 2, then adds fatigue increment 4
        expected_delts = min(10, max(0, before_delts - 2) + 4)
        self.assertEqual(updated["anterior_delts"], expected_delts)

        # Non-targeted muscle (lats) should have decayed by 2
        expected_lats = max(0, before_lats - 2)
        self.assertEqual(updated["lats"], expected_lats)


if __name__ == "__main__":
    unittest.main()
