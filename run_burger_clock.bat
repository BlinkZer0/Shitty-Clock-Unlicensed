@echo off
REM ╔═══════════════════════════════════════════════════════════════════════════╗
REM ║                                                                           ║
REM ║                    🍔 CHEESEBURGER CLOCK LANGUAGE 🍔                      ║
REM ║                                                                           ║
REM ║  Licensed under the Overprotective License (OPL-∞)                       ║
REM ║  "All rights aggressively reserved. Including the right to tell time."   ║
REM ║                                                                           ║
REM ╚═══════════════════════════════════════════════════════════════════════════╝

title The Cheeseburger Clock Language - Licensed Under OPL-∞

echo.
echo      .-"""-.
echo     /        \
echo    /_        _\
echo   // \      / \\
echo   ^\__\    /__/^|
echo    \    ^^    /
echo     \        /
echo      \  __  /
echo       '.__.'
echo.
echo ╔═══════════════════════════════════════════════════════════════════════════╗
echo ║                                                                           ║
echo ║                    🍔 CHEESEBURGER CLOCK LANGUAGE 🍔                      ║
echo ║                                                                           ║
echo ║  Licensed under the Overprotective License (OPL-∞)                       ║
echo ║  "All rights aggressively reserved. Including the right to tell time."   ║
echo ║                                                                           ║
echo ╚═══════════════════════════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo 🚨 ERROR: Python not found! Cannot grill burgers without Python!
    echo.
    echo Please install Python 3.6+ from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    echo ⚖️  BURGER LEGAL NOTICE:
    echo    This error constitutes a violation of Burger Article I
    echo    "Failure to have Python installed is prohibited burger assembly"
    echo.
    pause
    exit /b 1
)

REM Check if the burger script exists
if not exist "src\burger_clock.py" (
    echo 🚨 ERROR: burger_clock.py not found! Missing burger ingredients!
    echo.
    echo ⚖️  BURGER LEGAL NOTICE:
    echo    This error violates Burger Article VIII
    echo    "Missing burger files constitute unauthorized burger modification"
    echo.
    pause
    exit /b 1
)

echo ✅ Python detected (grill is hot)
echo ✅ Burger ingredients found
echo.
echo ⚠️  WARNING: Unauthorized burger assembly detected!
echo    You are about to violate approximately 17 burger clauses of OPL-∞
echo.
echo 📋 Burger license violations that will occur:
echo    • Burger Article I (Prohibited Burger Assembly)
echo    • Burger Article VI (Temporal Condiment Restrictions)
echo    • Burger Article IX (Secret Sauce Incompatibility)
echo    • The burger vibes
echo.
echo 💳 Free samples: 5 minutes
echo 💰 After samples: $999.99 + $49.99/hour + burger assembly fees
echo.
echo 🍔 LANGUAGE SYNTAX GUIDE:
echo    🍔 TOP_BUN      - Start program
echo    🥬 LETTUCE      - Clear screen
echo    🍅 TOMATO       - Display operation
echo    🧀 CHEESE       - Time calculation
echo    🥓 BACON        - Random generation
echo    🍖 PATTY        - Loop structure
echo    🍟 FRIES        - Conditional
echo    🥤 DRINK        - Wait/sleep
echo    🎵 SESAME_SEED  - Iteration marker
echo    🍔 BOTTOM_BUN   - End program
echo.
echo Press any key to start the burger grill (and accept the consequences)...
pause >nul

echo.
echo 🚀 Launching Cheeseburger Clock Language Interpreter...
echo    🍔 Assembling top bun...
echo    🥬 Adding lettuce layers...
echo    🍅 Slicing tomatoes...
echo    🧀 Melting cheese...
echo    🥓 Frying bacon strips...
echo    🍖 Grilling main patty...
echo    🍟 Preparing side fries...
echo    🥤 Pouring beverages...
echo    🎵 Sprinkling sesame seeds...
echo    🍔 Securing bottom bun...
echo.

REM Execute the burger language
python src\burger_clock.py

REM After burger program exits
echo.
echo ╔═══════════════════════════════════════════════════════════════════════════╗
echo ║                                                                           ║
echo ║                    ⚠️  BURGER GRILL STOPPED  ⚠️                         ║
echo ║                                                                           ║
echo ║  You have violated Burger Article I by stopping the burger assembly.     ║
echo ║  This constitutes unauthorized termination of burger compilation.        ║
echo ║                                                                           ║
echo ║  Your burger violation has been logged.                                  ║
echo ║  (Not really. We don't track burgers. But you should feel hungry.)      ║
echo ║                                                                           ║
echo ║  Please report to 404 Sesame Seed Street for processing.                 ║
echo ║                                                                           ║
echo ╚═══════════════════════════════════════════════════════════════════════════╝
echo.
echo Press any key to leave the burger restaurant...
pause >nul
