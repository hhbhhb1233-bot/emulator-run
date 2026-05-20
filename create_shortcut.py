"""创建桌面快捷方式 - 虚拟跑步"""
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def main():
    project_dir = Path(__file__).resolve().parent
    target = project_dir / "一键跑步.bat"
    icon = project_dir / "狼队夺了.ico"

    if not target.exists():
        print(f"错误: 找不到 {target}")
        return 1

    icon_line = ""
    if icon.exists():
        icon_line = f"$s.IconLocation = '{icon}'"

    ps_script = f"""\
$ws = New-Object -ComObject WScript.Shell
$desktop = [Environment]::GetFolderPath('Desktop')
$s = $ws.CreateShortcut("$desktop\\虚拟跑步.lnk")
$s.TargetPath = '{target}'
$s.WorkingDirectory = '{project_dir}'
{icon_line}
$s.Description = '雷电模拟器虚拟跑步'
$s.Save()
Write-Host 'OK'
"""

    fd, ps_path = tempfile.mkstemp(suffix=".ps1")
    try:
        with os.fdopen(fd, "w", encoding="utf-8-sig") as f:
            f.write(ps_script)

        result = subprocess.run(
            ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
             "-File", ps_path],
            capture_output=True, text=True, encoding="utf-8",
        )

        if result.returncode != 0 or "OK" not in result.stdout:
            print("创建快捷方式失败!")
            if result.stderr:
                print(result.stderr)
            return 1

        print("桌面快捷方式已创建!")
        return 0
    finally:
        try:
            os.unlink(ps_path)
        except OSError:
            pass


if __name__ == "__main__":
    sys.exit(main())
