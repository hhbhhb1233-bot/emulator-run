@echo off
py "%~dp0create_shortcut.py" 2>nul || python "%~dp0create_shortcut.py"
pause
