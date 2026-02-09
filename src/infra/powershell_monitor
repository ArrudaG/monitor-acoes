import subprocess
from pathlib import Path

def powershell_monitor():
    log_path = Path("logs/monitor.log").resolve()

    subprocess.Popen(
        ["powershell.exe", "-NoExit", "-Command",
         f'Get-Content "{log_path}" -Tail 50 -Wait'],
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )
