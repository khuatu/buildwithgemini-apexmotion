#!/usr/bin/env bash
# ==============================================================================
# ApexMotion Workshop - Local & Private PC Test Suite (Linux / macOS)
# ==============================================================================
set -e
echo "Starting ApexMotion Local Test Suite (Zero Google Cloud Required)..."
export APEXMOTION_OFFLINE_MODE=1
python3 run_all_tests.py
