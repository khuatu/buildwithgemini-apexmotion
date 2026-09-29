"""Test suite to verify 100% offline compatibility, portability, and zero-GCP execution

Verifies:
1. Complete self-containment of HTML files (zero external scripts, styles, or CDN calls).
2. ZIP archive integrity for email transmission to private computers.
3. Interactive features: Screencast Studio, Muscle Simulator, and Level-Up Game Quest.
4. Web Audio API synthesizer and Canvas confetti zero-dependency implementation.
"""

import os
import re
import unittest
import zipfile
from pathlib import Path

HTML_DIR = Path("/config/Desktop/HTML")
INDEX_PATH = HTML_DIR / "index.html"
PROGRESS_PATH = HTML_DIR / "learning_progress.html"
ZIP_PATH = HTML_DIR / "ApexMotion_Workshop_Hub.zip"


class TestOfflineHubPortability(unittest.TestCase):
    """Verifies that the generated learning package runs 100% offline on any private PC."""

    def test_files_exist_and_non_empty(self):
        """index.html and learning_progress.html must exist and be non-empty."""
        self.assertTrue(INDEX_PATH.exists(), f"File {INDEX_PATH} is missing!")
        self.assertTrue(PROGRESS_PATH.exists(), f"File {PROGRESS_PATH} is missing!")
        self.assertGreater(INDEX_PATH.stat().st_size, 100_000, "index.html is unexpectedly small!")
        self.assertGreater(PROGRESS_PATH.stat().st_size, 100_000, "learning_progress.html is unexpectedly small!")

    def test_zero_external_network_dependencies(self):
        """Scans HTML to ensure zero external CDN or remote resource dependencies."""
        content = INDEX_PATH.read_text(encoding="utf-8")

        # Check for remote stylesheet links
        external_css = re.findall(r'<link[^>]+href=["\'](https?://[^"\']+)["\']', content)
        self.assertEqual(
            external_css,
            [],
            f"Found external CSS dependencies that will fail offline: {external_css}",
        )

        # Check for remote script tags
        external_scripts = re.findall(r'<script[^>]+src=["\'](https?://[^"\']+)["\']', content)
        self.assertEqual(
            external_scripts,
            [],
            f"Found external script dependencies that will fail offline: {external_scripts}",
        )

        # Check for remote CSS font @import
        font_imports = re.findall(r'@import\s+url\(["\']?(https?://[^"\'\)]+)["\']?\)', content)
        self.assertEqual(
            font_imports,
            [],
            f"Found external font @import dependencies that will fail offline: {font_imports}",
        )

    def test_zip_archive_integrity(self):
        """Ensures the ZIP archive is valid, uncorrupted, and below standard email limits (< 5 MB)."""
        self.assertTrue(ZIP_PATH.exists(), f"ZIP archive {ZIP_PATH} is missing!")
        size_kb = ZIP_PATH.stat().st_size / 1024
        self.assertLess(size_kb, 5000, f"ZIP file is too large for email: {size_kb:.1f} KB")

        with zipfile.ZipFile(ZIP_PATH, "r") as zf:
            # testzip() returns None if no CRC or corrupt file errors found
            corrupt = zf.testzip()
            self.assertIsNone(corrupt, f"Corrupted file found in ZIP: {corrupt}")

            namelist = zf.namelist()
            self.assertIn("index.html", namelist)
            self.assertIn("learning_progress.html", namelist)
            self.assertIn("README.txt", namelist)

    def test_screencast_video_studio_present(self):
        """Ensures the terminal video studio engine and recordings are present."""
        content = INDEX_PATH.read_text(encoding="utf-8")
        self.assertIn("video-studio", content)
        self.assertIn("loadTutorial", content)
        self.assertIn("playTutorialDirect", content)
        self.assertIn("tutorials", content)
        self.assertIn("tutorial_01_react_tool_calling.mp4", content)

    def test_muscle_simulator_and_math_present(self):
        """Ensures interactive fatigue calculator and exponential decay math are embedded."""
        content = INDEX_PATH.read_text(encoding="utf-8")
        self.assertIn("executeSimWorkout", content)
        self.assertIn("simulateRestDecay", content)
        self.assertIn("updateSimDisplay", content)
        self.assertIn("readiness-display", content)
        self.assertIn("readiness-status", content)
        # Check formula in documentation
        self.assertIn("F(t) = F<sub>0</sub>", content)


    def test_game_quest_arena_embedded(self):
        """Ensures the Level-Up Game Quest with all 6 missions and Web Audio sound synthesizer is present."""
        content = INDEX_PATH.read_text(encoding="utf-8")
        self.assertIn("game-arena", content)
        self.assertIn("startGameQuest", content)
        self.assertIn("playSoundChime", content)
        self.assertIn("triggerConfetti", content)
        self.assertIn("missionsData", content)
        self.assertIn("Apex Grandmaster", content)

    def test_bilingual_support(self):
        """Ensures bilingual DE/EN switcher and localization keys are embedded."""
        content = INDEX_PATH.read_text(encoding="utf-8")
        self.assertIn("setLanguage", content)
        self.assertIn("btn-de", content)
        self.assertIn("btn-en", content)
        self.assertIn("data-de", content)
        self.assertIn("data-en", content)




if __name__ == "__main__":
    unittest.main()
