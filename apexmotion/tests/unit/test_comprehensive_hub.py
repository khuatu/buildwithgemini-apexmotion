"""=============================================================================
ApexMotion Workshop - Comprehensive HTML Hub & Portability Test Suite
=============================================================================
Tests EVERY single specified feature of the standalone learning hub:
1. Physical file existence, sizes, and absence of symlinks.
2. 100% Zero-CDN and zero-network autarky (no external HTTP/HTTPS resources).
3. All 19 step cards (1-13 completed with why-box & review checkboxes, 14-19 upcoming).
4. Interactive Roadmap Tree navigation (all jumpToStep & jumpToSection targets valid).
5. Gamified Level-Up Quest Arena (all 6 missions, options, correct indices, XP, sounds, confetti).
6. Terminal Screencast Video Studio (all 5 tutorials, animation frames, DE/EN narration).
7. Interactive Muscle Fatigue & Recovery Simulator (bars, scores, decay math, readiness).
8. Firestore Database Live Explorer (sample docs, valid JSON, syntax tabs).
9. Bilingual Internationalization (i18n key parity, data-de/data-en symmetry).
10. Search & Filter controls (all categories including offline tests).
11. ZIP archive integrity & byte-exact SHA256 extraction roundtrip.
12. verify_offline.py diagnostic script subprocess execution.
============================================================================="""

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

HTML_DIR = Path("/config/Desktop/HTML")
INDEX_PATH = HTML_DIR / "index.html"
PROGRESS_PATH = HTML_DIR / "learning_progress.html"
VERIFY_SCRIPT_PATH = HTML_DIR / "verify_offline.py"
README_PATH = HTML_DIR / "README.txt"
ZIP_PATH = HTML_DIR / "ApexMotion_Workshop_Hub.zip"


class TestComprehensiveHubFeatures(unittest.TestCase):
    """Exhaustive test suite covering all hub features, offline readiness, and portability."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        assert INDEX_PATH.exists(), f"Missing {INDEX_PATH}"
        cls.html_content = INDEX_PATH.read_text(encoding="utf-8")

    def test_01_physical_files_and_sizes(self):
        """Verifies files exist as physical files (no symlinks) and have appropriate sizes."""
        for path in [INDEX_PATH, PROGRESS_PATH, VERIFY_SCRIPT_PATH, README_PATH, ZIP_PATH]:
            self.assertTrue(path.exists(), f"File {path} must exist!")
            self.assertFalse(path.is_symlink(), f"File {path} must NOT be a symlink for email safety!")

        # Size gut checks
        self.assertGreater(INDEX_PATH.stat().st_size, 150_000, "index.html too small!")
        self.assertLess(INDEX_PATH.stat().st_size, 600_000, "index.html too large!")
        self.assertGreater(ZIP_PATH.stat().st_size, 50_000, "ZIP too small!")
        self.assertLess(ZIP_PATH.stat().st_size, 200_000, "ZIP should be < 200 KB for easy emailing!")

    def test_02_zero_external_network_dependencies(self):
        """Ensures 100% offline self-containment: 0 external scripts, links, fonts, or images."""
        content = self.html_content

        # Remote styles
        ext_css = re.findall(r'<link[^>]+href=["\'](https?://[^"\']+)["\']', content)
        self.assertEqual(ext_css, [], f"Found external CSS: {ext_css}")

        # Remote scripts
        ext_js = re.findall(r'<script[^>]+src=["\'](https?://[^"\']+)["\']', content)
        self.assertEqual(ext_js, [], f"Found external scripts: {ext_js}")

        # Remote font imports
        ext_fonts = re.findall(r'@import\s+url\(["\']?(https?://[^"\'\)]+)["\']?\)', content)
        self.assertEqual(ext_fonts, [], f"Found external font imports: {ext_fonts}")

        # Remote images
        ext_imgs = re.findall(r'<img[^>]+src=["\'](https?://[^"\']+)["\']', content)
        self.assertEqual(ext_imgs, [], f"Found external images: {ext_imgs}")

        # Remote iframes
        ext_iframes = re.findall(r'<iframe[^>]+src=["\'](https?://[^"\']+)["\']', content)
        self.assertEqual(ext_iframes, [], f"Found external iframes: {ext_iframes}")

    def test_03_all_19_step_cards_structure(self):
        """Verifies all 19 steps exist, cards 1-13 are completed with why-boxes, and 14-19 are upcoming."""
        content = self.html_content

        for i in range(1, 20):
            card_id = f"step-card-{i}"
            self.assertIn(f'id="{card_id}"', content, f"Step card {card_id} is missing!")

            # Extract card content
            card_pattern = rf'<div class="step-card ([^"]+)"[^>]*id="{card_id}".*?(?=<div class="step-card|$)'
            m = re.search(card_pattern, content, re.DOTALL)
            self.assertIsNotNone(m, f"Could not match card {card_id}")
            card_classes = m.group(1)
            card_body = m.group(0)

            # Check why-box exists
            self.assertIn('class="why-box"', card_body, f"Card {card_id} is missing why-box rationale!")
            self.assertIn('data-i18n="lbl_why_step"', card_body, f"Card {card_id} why-box missing label!")

            if i <= 13:
                self.assertIn("completed", card_classes, f"Step {i} should be marked completed!")
                # Must have review checkbox
                self.assertIn(f"markReviewed({i},", card_body, f"Step {i} missing review checkbox callback!")
                # Must have terminal or code snippet
                has_code = "terminal-block" in card_body or "<pre" in card_body or "<code>" in card_body
                self.assertTrue(has_code, f"Step {i} should contain a terminal or code example!")
            else:
                self.assertIn("upcoming", card_classes, f"Step {i} should be marked upcoming!")

    def test_04_roadmap_tree_navigation_integrity(self):
        """Ensures every jumpToStep and jumpToSection in the roadmap tree targets an existing DOM element."""
        content = self.html_content

        # All jumpToStep targets
        jump_steps = re.findall(r"jumpToStep\((\d+)\)", content)
        self.assertGreater(len(jump_steps), 0, "No jumpToStep calls found!")
        for step_num in jump_steps:
            target_id = f'id="step-card-{step_num}"'
            self.assertIn(target_id, content, f"jumpToStep({step_num}) references missing card {target_id}!")

        # All jumpToSection targets
        jump_sections = re.findall(r"jumpToSection\((\x27|\")([^\x27\"]+)(\x27|\")\)", content)
        self.assertGreater(len(jump_sections), 0, "No jumpToSection calls found!")
        for _, sec_id, _ in jump_sections:
            target_id = f'id="{sec_id}"'
            self.assertIn(target_id, content, f"jumpToSection('{sec_id}') references missing element {target_id}!")

    def test_05_gamified_quest_arena_complete(self):
        """Verifies Level-Up Quest Arena, 6 missions, correct indices, rank badges, sounds, and confetti."""
        content = self.html_content

        # DOM containers
        self.assertIn('id="game-arena"', content)
        self.assertIn('onclick="startGameQuest()"', content)
        self.assertIn('id="confetti-canvas"', content)
        self.assertIn('id="hud-lives-display"', content)
        self.assertIn('id="hud-xp-display"', content)
        self.assertIn('id="hud-streak-display"', content)
        self.assertIn('id="hud-level-text"', content)

        # Functions
        self.assertIn("startGameQuest", content)
        self.assertIn("playSoundChime", content)
        self.assertIn("playSoundFanfare", content)
        self.assertIn("playSoundBuzz", content)
        self.assertIn("triggerConfetti", content)

        # Extract missionsData structure
        rewards = [int(r) for r in re.findall(r"reward:\s*(\d+)", content)]
        self.assertEqual(len(rewards), 6, f"Expected exactly 6 missions, found {len(rewards)}")
        self.assertTrue(all(r > 0 for r in rewards), "All rewards must be positive XP!")

        # Title and scenario bilingual symmetry
        titles_de = re.findall(r'title_de:\s*"([^"]+)"', content)
        titles_en = re.findall(r'title_en:\s*"([^"]+)"', content)
        self.assertEqual(len(titles_de), 6, "Expected 6 German mission titles")
        self.assertEqual(len(titles_en), 6, "Expected 6 English mission titles")

        # Check options: exactly one correct option per mission (total 6)
        correct_flags = re.findall(r"correct:\s*true", content)
        self.assertEqual(len(correct_flags), 6, f"Expected 6 correct answers across 6 missions, found {len(correct_flags)}")

        options_de = re.findall(r'text_de:\s*"([^"]+)"', content)
        options_en = re.findall(r'text_en:\s*"([^"]+)"', content)
        self.assertGreaterEqual(len(options_de), 18, "Expected at least 18 options (>= 3 per mission)")
        self.assertEqual(len(options_de), len(options_en), "DE/EN options count mismatch!")

        # Verify level-up rank names
        ranks = ["Cloud Trainee", "ReAct Developer", "Firestore Architect", "Systems Engineer", "Apex Grandmaster"]
        for rank in ranks:
            self.assertIn(rank, content, f"Rank {rank} missing from gamification system!")

    def test_06_screencast_video_studio_complete(self):
        """Verifies terminal screencast video studio, player controls, and all 5 tutorial recordings."""
        content = self.html_content

        # Player elements
        self.assertIn('id="video-studio"', content)
        self.assertIn('id="video-screen-content"', content)
        self.assertIn('id="terminal-screen-text"', content)
        self.assertIn('id="video-clip-title"', content)
        self.assertIn('id="narration-box"', content)
        self.assertIn('id="video-progress"', content)

        # Controls
        self.assertIn("togglePlayVideo", content)
        self.assertIn("restartVideo", content)
        self.assertIn("cycleSpeed", content)

        # Extract tutorials
        tut_titles = re.findall(r'title:\s*"([^"]+\.mp4)"', content)
        self.assertEqual(len(tut_titles), 5, f"Expected 5 tutorial titles, found {len(tut_titles)}")

        screens = re.findall(r"screen:\s*['\"]", content)
        narrations_de = re.findall(r'narration_de:\s*"([^"]+)"', content)
        narrations_en = re.findall(r'narration_en:\s*"([^"]+)"', content)

        self.assertGreaterEqual(len(screens), 15, f"Expected >= 15 scene frames, found {len(screens)}")
        self.assertEqual(len(narrations_de), len(screens), "Mismatched narration_de count")
        self.assertEqual(len(narrations_en), len(screens), "Mismatched narration_en count")

    def test_07_interactive_simulator_and_biomechanics_math(self):
        """Verifies fatigue and recovery simulator UI elements, control buttons, and mathematical formulas."""
        content = self.html_content

        self.assertIn('id="interactive-simulator"', content)
        self.assertIn('id="math-deep-dive"', content)

        # Muscle bars and badges
        for muscle in ["delts", "lats", "core", "biceps", "legs"]:
            self.assertIn(f'id="bar-{muscle}"', content, f"Missing bar-{muscle}")
            self.assertIn(f'id="score-{muscle}"', content, f"Missing score-{muscle}")

        # Readiness indicators
        self.assertIn('id="readiness-display"', content)
        self.assertIn('id="readiness-status"', content)

        # Simulator functions
        self.assertIn("executeSimWorkout", content)
        self.assertIn("simulateRestDecay", content)
        self.assertIn("resetSimMuscles", content)
        self.assertIn("updateSimDisplay", content)

        # Mathematical formulas
        self.assertIn("Borg CR10", content)
        self.assertIn("F(t) = F<sub>0</sub>", content)
        self.assertIn("T<sub>1/2</sub>", content)
        self.assertIn("Readiness", content)

    def test_08_firestore_live_explorer(self):
        """Verifies Firestore data explorer tab navigation and sample document JSON syntax."""
        content = self.html_content

        self.assertIn('id="firestore-explorer"', content)
        self.assertIn('id="db-viewer-content"', content)
        self.assertIn("showDbDoc", content)

        # Sample documents
        for doc in ["planche", "front_lever", "pullup", "athlete"]:
            self.assertIn(doc, content, f"Missing sample document {doc} in database explorer")

    def test_09_bilingual_i18n_parity(self):
        """Verifies dictionary completeness: every key in i18n.de exists in i18n.en and vice versa."""
        content = self.html_content

        de_match = re.search(r"const i18n = \{\s*de:\s*\{(.*?)\},\s*en:\s*\{(.*?)\}\s*\};", content, re.DOTALL)
        self.assertIsNotNone(de_match, "Could not match i18n dictionary block!")
        keys_de = set(re.findall(r"(\w+):", de_match.group(1)))
        keys_en = set(re.findall(r"(\w+):", de_match.group(2)))

        self.assertEqual(keys_de, keys_en, f"Keys mismatch! Diff DE-EN: {keys_de - keys_en}, Diff EN-DE: {keys_en - keys_de}")

        # Check all data-i18n in DOM map to known keys
        dom_i18n_keys = set(re.findall(r'data-i18n=["\']([^"\']+)["\']', content))
        unknown_keys = dom_i18n_keys - keys_de
        self.assertEqual(unknown_keys, set(), f"DOM elements reference unknown i18n keys: {unknown_keys}")

    def test_10_search_and_filter_controls(self):
        """Verifies search input, category filters (including offline tests), and expand/collapse buttons."""
        content = self.html_content

        self.assertIn('id="search-input"', content)
        self.assertIn("filterSteps", content)
        self.assertIn("setFilter", content)
        self.assertIn("toggleAllSteps", content)

        for cat in ["all", "setup", "agent", "db", "storage", "tests", "upcoming"]:
            self.assertIn(f'data-filter="{cat}"', content, f"Filter button for '{cat}' missing!")

    def test_11_zip_archive_and_extraction_roundtrip(self):
        """Tests that the ZIP archive is intact, under email limits, and SHA256 hashes match on extract."""
        self.assertTrue(ZIP_PATH.exists(), "ZIP archive missing!")
        size_kb = ZIP_PATH.stat().st_size / 1024
        self.assertLess(size_kb, 150, f"ZIP file {size_kb:.1f} KB is larger than 150 KB limit!")

        with zipfile.ZipFile(ZIP_PATH, "r") as zf:
            self.assertIsNone(zf.testzip(), "ZIP file is corrupted!")
            namelist = zf.namelist()
            expected_files = {"index.html", "learning_progress.html", "README.txt", "verify_offline.py"}
            self.assertEqual(set(namelist), expected_files, f"Unexpected ZIP contents: {namelist}")

            # Extraction and hash verification
            with tempfile.TemporaryDirectory() as tmpdir:
                zf.extractall(tmpdir)
                for fname in expected_files:
                    extracted_path = Path(tmpdir) / fname
                    original_path = HTML_DIR / fname
                    self.assertTrue(extracted_path.exists())

                    h_orig = hashlib.sha256(original_path.read_bytes()).hexdigest()
                    h_extr = hashlib.sha256(extracted_path.read_bytes()).hexdigest()
                    self.assertEqual(h_orig, h_extr, f"SHA256 mismatch for extracted {fname}!")

    def test_12_verify_offline_script_execution(self):
        """Runs the standalone verify_offline.py script and asserts it completes with exit code 0."""
        self.assertTrue(VERIFY_SCRIPT_PATH.exists(), "verify_offline.py is missing!")

        result = subprocess.run(
            [sys.executable, str(VERIFY_SCRIPT_PATH)],
            capture_output=True,
            text=True,
            timeout=10,
            cwd=str(HTML_DIR),
        )

        self.assertEqual(
            result.returncode,
            0,
            f"verify_offline.py failed with exit code {result.returncode}:\n{result.stderr}\n{result.stdout}",
        )
        self.assertIn("ALL 8 OFFLINE VERIFICATION CHECKS PASSED", result.stdout)


if __name__ == "__main__":
    unittest.main()
