@echo off
chcp 65001 >nul
title 安装桌面快捷方式

powershell -Command ^
$ws = New-Object -ComObject WScript.Shell; ^
$s = $ws.CreateShortcut([Environment]::GetFolderPath('Desktop') + '\虚拟跑步.lnk'); ^
$s.TargetPath = '%~dp0一键跑步.bat'; ^
$s.WorkingDirectory = '%~dp0'; ^
$s.IconLocation = '%~dp0狼队夺了.ico'; ^
$s.Description = '雷电模拟器虚拟跑步'; ^
$s.Save()

echo 桌面快捷方式已创建！
pause
