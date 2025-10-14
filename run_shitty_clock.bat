@echo off
REM ╔═══════════════════════════════════════════════════════════════════════════╗
REM ║                                                                           ║
REM ║                    🕐 THE SHITTY CLOCK APPLICATION 🕐                      ║
REM ║                                                                           ║
REM ║  Licensed under the Overprotective License (OPL-∞)                       ║
REM ║  "All rights aggressively reserved. Including the right to tell time."   ║
REM ║                                                                           ║
REM ╚═══════════════════════════════════════════════════════════════════════════╝

title The Shitty Clock Application - Licensed Under OPL-∞

echo.
echo ╔═══════════════════════════════════════════════════════════════════════════╗
echo ║                                                                           ║
echo ║                    🕐 THE SHITTY CLOCK APPLICATION 🕐                      ║
echo ║                                                                           ║
echo ║  Licensed under the Overprotective License (OPL-∞)                       ║
echo ║  "All rights aggressively reserved. Including the right to tell time."   ║
echo ║                                                                           ║
echo ╚═══════════════════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo 🚨 ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.6+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    echo ⚖️  LEGAL NOTICE:
    echo    This error constitutes a violation of Article I, Clause 1
    echo    "Failure to have Python installed is prohibited use"
    echo.
    pause
    exit /b 1
)

REM Check if the Python script exists
if not exist "src\shitty_clock.py" (
    echo 🚨 ERROR: shitty_clock.py not found in src\ directory
    echo.
    echo ⚖️  LEGAL NOTICE:
    echo    This error violates Article VIII, Clause 16
    echo    "Missing source files constitute unauthorized modification"
    echo.
    pause
    exit /b 1
)

echo ✅ Python detected
echo ✅ Source files found
echo.
echo ⚠️  WARNING: Unauthorized execution detected!
echo    You are about to violate approximately 17 clauses of the OPL-∞ license
echo.
echo 📋 License violations that will occur:
echo    • Article I, Clause 1 (Prohibited Use)
echo    • Article VI, Clause 13 (Temporal Restrictions)
echo    • Article IX, Clause 17 (License Incompatibility)
echo    • The vibes
echo.
echo 💳 Trial period: 5 minutes
echo 💰 After trial: $999.99 + $49.99/hour + unauthorized use fees
echo.
echo Press any key to continue (and accept the consequences)...
pause >nul

echo.
echo 🚀 Launching The Shitty Clock Application...
echo    Loading legal disclaimers...
echo    Calculating unauthorized use fees...
echo    Preparing countdown timer...
echo.

REM Run the Python application
python src\shitty_clock.py

REM After the application exits
echo.
echo ╔═══════════════════════════════════════════════════════════════════════════╗
echo ║                                                                           ║
echo ║                    ⚠️  APPLICATION TERMINATED  ⚠️                        ║
echo ║                                                                           ║
echo ║  You have violated Article I, Clause 1 by exiting the application.      ║
echo ║  This constitutes unauthorized termination of licensed software.        ║
echo ║                                                                           ║
echo ║  Your violation has been logged.                                         ║
echo ║  (Not really. We don't track anything. But you should feel bad.)        ║
echo ║                                                                           ║
echo ║  Please report to 404 Not Found Street for processing.                   ║
echo ║                                                                           ║
echo ╚═══════════════════════════════════════════════════════════════════════════╝
echo.
echo Press any key to exit...
pause >nul
