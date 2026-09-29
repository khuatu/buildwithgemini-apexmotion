@echo off
REM ==============================================================================
REM ApexMotion Workshop - Local & Private PC Test Suite (Windows)
REM ==============================================================================
echo Starting ApexMotion Local Test Suite (Zero Google Cloud Required)...
set APEXMOTION_OFFLINE_MODE=1
python run_all_tests.py
pause
