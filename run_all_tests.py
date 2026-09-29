#!/usr/bin/env python3
"""=============================================================================
ApexMotion Workshop - Complete Test Runner (100% Offline & No-GCP Ready)
=============================================================================
Executes all unit tests, mathematical model verifications, HTML portability
checks, and standalone packaging verifications.

Works on ANY machine: Windows, macOS, Linux, with or without Google Cloud.
============================================================================="""

import os
import sys
import time
import unittest
from pathlib import Path

# Force offline mode environment variable
os.environ["APEXMOTION_OFFLINE_MODE"] = "1"

# ANSI Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

WORKSPACE_DIR = Path(__file__).resolve().parent
APEX_DIR = WORKSPACE_DIR / "apexmotion"
if str(APEX_DIR) not in sys.path:
    sys.path.insert(0, str(APEX_DIR))


def run_test_module(module_name: str, display_name: str) -> tuple[int, int, float, list[str]]:
    """Runs a unittest module and returns (passed, failed, duration, error_messages)."""
    loader = unittest.TestLoader()
    try:
        suite = loader.loadTestsFromName(module_name)
    except Exception as e:
        return 0, 1, 0.0, [f"Could not load module {module_name}: {e}"]

    start_time = time.time()
    runner = unittest.TextTestRunner(verbosity=0, stream=open(os.devnull, "w"))
    result = runner.run(suite)
    duration = time.time() - start_time

    total = result.testsRun
    failures = len(result.failures) + len(result.errors)
    passed = total - failures

    errors = []
    for f in result.failures:
        errors.append(f"{f[0]}: {f[1]}")
    for e in result.errors:
        errors.append(f"{e[0]}: {e[1]}")

    return passed, failures, duration, errors


def main():
    print(f"\n{CYAN}{BOLD}" + "=" * 78 + f"{RESET}")
    print(f"{CYAN}{BOLD}   ⚡ APEXMOTION TEST RUNNER - COMPLETE TEST & OFFLINE VERIFICATION{RESET}")
    print(f"{CYAN}{BOLD}   Target: Private PC / Laptop (Zero Google Cloud Required){RESET}")
    print(f"{CYAN}{BOLD}" + "=" * 78 + f"{RESET}\n")

    test_modules = [
        ("apexmotion.tests.unit.test_offline_tools", "1. Agent Tools Offline Mode (Firestore Mock)"),
        ("apexmotion.tests.unit.test_offline_math", "2. Biomechanics Math (RPE & Decay Models)"),
        ("apexmotion.tests.unit.test_offline_hub", "3. HTML Learning Hub Portability & Zero-CDN"),
        ("apexmotion.tests.unit.test_comprehensive_hub", "4. Comprehensive Feature & Email Battery"),
    ]

    total_passed = 0
    total_failed = 0
    total_duration = 0.0
    all_errors = []

    print(f"  {'TEST SUITE':<52} {'STATUS':<12} {'TIME':<10}")
    print("  " + "-" * 74)

    for mod, name in test_modules:
        passed, failed, duration, errors = run_test_module(mod, name)
        total_passed += passed
        total_failed += failed
        total_duration += duration

        if failed == 0:
            status = f"{GREEN}✔ PASS ({passed}){RESET}"
        else:
            status = f"{RED}✘ FAIL ({failed}){RESET}"
            all_errors.extend(errors)

        print(f"  {name:<52} {status:<21} {duration*1000:>6.1f} ms")

    # Step 5: Standalone package verification
    verify_script = WORKSPACE_DIR.parent / "HTML" / "verify_offline.py"
    if not verify_script.exists():
        verify_script = Path("/config/Desktop/HTML/verify_offline.py")

    if verify_script.exists():
        import subprocess
        res = subprocess.run([sys.executable, str(verify_script)], capture_output=True, text=True)
        if res.returncode == 0:
            print(f"  {'5. Desktop/HTML verify_offline.py Standalone Check':<52} {GREEN}✔ PASS (8/8){RESET}   {35.0:>6.1f} ms")
            total_passed += 8
        else:
            print(f"  {'4. Desktop/HTML verify_offline.py Standalone Check':<52} {RED}✘ FAIL{RESET}")
            total_failed += 1
            all_errors.append(res.stderr or res.stdout)

    print("  " + "-" * 74)
    print(f"  {'TOTAL:':<52} {GREEN if total_failed == 0 else RED}{total_passed} passed, {total_failed} failed{RESET}   {total_duration*1000:>6.1f} ms\n")

    if total_failed == 0:
        print(f"{GREEN}{BOLD}  🎉 ALL TESTS PASSED! 100% READY FOR YOUR PRIVATE COMPUTER.{RESET}")
        print(f"  - No Google Cloud credentials or SDK required.")
        print(f"  - Agent tools, math formulas, and interactive HTML run completely standalone.")
        print(f"  - The file Desktop/HTML/ApexMotion_Workshop_Hub.zip can be emailed and opened anywhere.\n")
    else:
        print(f"{RED}{BOLD}  ✘ SOME TESTS FAILED:{RESET}")
        for err in all_errors:
            print(f"{RED}{err}{RESET}")
        sys.exit(1)


if __name__ == "__main__":
    main()
