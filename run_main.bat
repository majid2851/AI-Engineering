@echo off
cd /d "%~dp0"
echo Running main.py with project venv...
echo.
"%~dp0venv\Scripts\python.exe" "%~dp0main.py"
echo.
pause
