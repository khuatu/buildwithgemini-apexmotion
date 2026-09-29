"""Unit tests for ApexMotion biomechanics & recovery mathematics.

Verifies the mathematical formulas for:
1. RPE Borg CR10 fatigue increment calculation
2. Biological exponential recovery decay: F(t) = F0 * e^(-lambda * t)
3. Muscle Split Readiness Index & Decision Thresholds
"""

import math
import unittest


def compute_fatigue_increment(rpe: int) -> int:
    """Computes incremental muscle fatigue from Borg CR10 RPE."""
    clamped_rpe = max(1, min(10, rpe))
    return clamped_rpe // 2


def compute_exponential_decay(f0: float, delta_hours: float, half_life_hours: float = 24.0) -> float:
    """Computes residual fatigue based on biological exponential half-life decay."""
    if f0 <= 0:
        return 0.0
    decay_constant = math.log(2) / half_life_hours
    residual = f0 * math.exp(-decay_constant * delta_hours)
    return round(residual, 2)


def compute_split_readiness(fatigue_scores: list[float]) -> tuple[float, str]:
    """Computes average readiness and categorizes traffic light status.

    Returns:
        (readiness_score, status_category) where status is 'GREEN', 'YELLOW', or 'RED'.
    """
    if not fatigue_scores:
        return 10.0, "GREEN"
    avg_fatigue = sum(fatigue_scores) / len(fatigue_scores)
    readiness = max(0.0, min(10.0, 10.0 - avg_fatigue))
    readiness_rounded = round(readiness, 1)

    if readiness_rounded >= 7.0:
        status = "GREEN"
    elif readiness_rounded >= 4.0:
        status = "YELLOW"
    else:
        status = "RED"

    return readiness_rounded, status


class TestApexMotionMathModels(unittest.TestCase):
    """Verifies all mathematical models of ApexMotion coach."""

    def test_rpe_fatigue_increment(self):
        """Tests Borg CR10 scaling into discrete fatigue units."""
        self.assertEqual(compute_fatigue_increment(10), 5)
        self.assertEqual(compute_fatigue_increment(9), 4)
        self.assertEqual(compute_fatigue_increment(8), 4)
        self.assertEqual(compute_fatigue_increment(7), 3)
        self.assertEqual(compute_fatigue_increment(6), 3)
        self.assertEqual(compute_fatigue_increment(5), 2)
        self.assertEqual(compute_fatigue_increment(4), 2)
        self.assertEqual(compute_fatigue_increment(2), 1)
        self.assertEqual(compute_fatigue_increment(1), 0)  # 1 // 2 = 0


    def test_exponential_half_life_decay(self):
        """Tests exponential biological decay at half-life intervals."""
        initial_fatigue = 8.0
        half_life = 24.0

        # At t = 0 h: 100% of fatigue
        f_0h = compute_exponential_decay(initial_fatigue, 0.0, half_life)
        self.assertAlmostEqual(f_0h, 8.0, delta=0.01)

        # At t = 24 h (1 half-life): exactly 50% = 4.0
        f_24h = compute_exponential_decay(initial_fatigue, 24.0, half_life)
        self.assertAlmostEqual(f_24h, 4.0, delta=0.01)

        # At t = 48 h (2 half-lives): exactly 25% = 2.0
        f_48h = compute_exponential_decay(initial_fatigue, 48.0, half_life)
        self.assertAlmostEqual(f_48h, 2.0, delta=0.01)

        # At t = 72 h (3 half-lives): exactly 12.5% = 1.0
        f_72h = compute_exponential_decay(initial_fatigue, 72.0, half_life)
        self.assertAlmostEqual(f_72h, 1.0, delta=0.01)

    def test_split_readiness_status_green(self):
        """Fresh muscles (< 3.0 fatigue) should yield GREEN status."""
        push_fatigue = [1.5, 2.0, 1.0]  # Anterior delts, chest, triceps
        score, status = compute_split_readiness(push_fatigue)
        self.assertGreaterEqual(score, 7.0)
        self.assertEqual(status, "GREEN")

    def test_split_readiness_status_yellow(self):
        """Moderate fatigue (3.0 - 6.0) should yield YELLOW status."""
        push_fatigue = [5.0, 4.5, 5.5]
        score, status = compute_split_readiness(push_fatigue)
        self.assertTrue(4.0 <= score < 7.0)
        self.assertEqual(status, "YELLOW")

    def test_split_readiness_status_red(self):
        """Heavy fatigue (> 6.0) should yield RED status."""
        pull_fatigue = [7.5, 8.0, 7.0]  # Lats, rear delts, biceps
        score, status = compute_split_readiness(pull_fatigue)
        self.assertLess(score, 4.0)
        self.assertEqual(status, "RED")


if __name__ == "__main__":
    unittest.main()
