@echo off
chcp 65001 >nul
title 虚拟跑步

cd /d "%~dp0fk-gps\fakerun\ldplayer_run"
python main.py
pause
