@echo off
REM ===========================================================
REM  Tutorial Hub - publish to GitHub
REM
REM  Double-click this file, or run from the folder:
REM      publish
REM      publish "your message here"
REM ===========================================================

cd /d "%~dp0"

set "MSG=%~1"
if "%MSG%"=="" set "MSG=Update lessons and site content"

echo.
echo ============================================
echo   Publishing Tutorial Hub
echo   Message: %MSG%
echo ============================================
echo.

git add -A
if errorlevel 1 goto :failed

REM Nothing staged? Then there is nothing to publish.
git diff --cached --quiet
if not errorlevel 1 (
    echo No changes to publish. Everything is already up to date.
    echo.
    pause
    exit /b 0
)

git commit -m "%MSG%"
if errorlevel 1 goto :failed

git push
if errorlevel 1 goto :failed

echo.
echo ============================================
echo   Done. Your site will rebuild in a minute.
echo   https://pc-master-race.github.io/CourseTech/
echo ============================================
echo.
pause
exit /b 0

:failed
echo.
echo ------------------------------------------------
echo   Something went wrong. Read the message above.
echo.
echo   Common fixes:
echo     - If it asks who you are:
echo         git config --global user.email "you@example.com"
echo         git config --global user.name  "Your Name"
echo     - If the push was rejected, someone or something
echo       else changed the repo. Run:  git pull  then try again.
echo ------------------------------------------------
echo.
pause
exit /b 1
