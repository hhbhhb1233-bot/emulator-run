@echo off
cd /d "%~dp0fk-gps\fakerun\ldplayer_run"
py main.py 2>nul || python main.py
pause
