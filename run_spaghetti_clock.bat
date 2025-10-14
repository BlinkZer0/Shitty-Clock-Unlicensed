@echo off
REM Spaghetti Code Clock Language Launcher
REM Licensed under the Overprotective License (OPL-infinity)

chcp 65001 >nul 2>&1
title The Spaghetti Code Clock Language - Polite Compilation Required

echo.
echo        ~~~ ~~~  ~~~ ~~~
echo       ~~~  ~~  ~~  ~~~
echo         \  ^^  ^^  /
echo          \ ^^ ^^ /
echo           \^^^^^/
echo         ___\^^^/___
echo        ^|  DADDY!!  ^|
echo        ^| ( ^ w ^ )^|
echo         \  \^^^/  /
echo          ^|  ^^^  ^|
echo         /^|  ^^^  ^|\
echo        / ^|  ^^^  ^| \
echo     ~~~  ^| ^^^ ^|  ~~~
echo    ~~~   ^|/   \^|   ~~~
echo     ~~~ /       \ ~~~
echo        ^|  NOODLE ^|
echo        ^|  LEGS!! ^|
echo         ~~~~~~~~~
echo.
echo    *DANCING INTENSIFIES*
echo.
echo ========================================================================
echo                  SPAGHETTI CODE CLOCK LANGUAGE                            
echo.
echo  Based on POLITE COMPILATION - You MUST say "SPAGHETTI DADDY PLEASE"     
echo.
echo  Licensed under the Overprotective License (OPL-infinity)                       
echo ========================================================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found! Cannot cook spaghetti without Python!
    echo.
    echo SPAGHETTI_DADDY_PLEASE install Python 3.6+ from https://python.org
    pause
    exit /b 1
)

REM Check file exists
if not exist "src\spaghetti_clock.py" (
    echo ERROR: spaghetti_clock.py not found! Missing noodle ingredients!
    pause
    exit /b 1
)

echo [OK] Python detected (THANK_YOU_SPAGHETTI_DADDY)
echo [OK] Spaghetti ingredients found (MAY_I_HAVE_ANOTHER_NOODLE)
echo.
echo WARNING: Unauthorized polite compilation detected!
echo.
echo POLITE LANGUAGE SYNTAX GUIDE:
echo    SPAGHETTI_DADDY_PLEASE_START              - Start program
echo    SPAGHETTI_DADDY_PLEASE_CLEAR_SCREEN       - Clear screen
echo    SPAGHETTI_DADDY_PLEASE_DISPLAY            - Display operation
echo    SPAGHETTI_DADDY_PLEASE_CALCULATE_TIME     - Time calculation
echo    SPAGHETTI_DADDY_PLEASE_LOOP               - Loop structure
echo    SPAGHETTI_DADDY_PLEASE_IF_SAUCE_READY     - Conditional
echo    SPAGHETTI_DADDY_PLEASE_WAIT               - Wait/sleep
echo    SPAGHETTI_DADDY_PLEASE_END                - End program
echo.
echo    THANK_YOU_SPAGHETTI_DADDY                 - Acknowledge completion
echo    MAY_I_HAVE_ANOTHER_NOODLE                 - Continue operation
echo    SORRY_FOR_BOTHERING_YOU_DADDY             - Error handling
echo.
echo SPAGHETTI_DADDY_PLEASE press any key to start compilation...
pause >nul

echo.
echo Launching polite compilation...
echo    SPAGHETTI_DADDY_PLEASE_START...
echo    THANK_YOU_SPAGHETTI_DADDY!
echo.

python src\spaghetti_clock.py

echo.
echo ========================================================================
echo                    SPAGHETTI COMPILATION STOPPED                          
echo.
echo  You have stopped the polite compilation (Spaghetti Daddy is sad).       
echo  THANK_YOU_SPAGHETTI_DADDY for running the program!
echo ========================================================================
echo.
pause
