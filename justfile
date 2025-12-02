# Set shell for non-Windows OSs:
set shell := ["powershell", "-c"]

# Set shell for Windows OSs:
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

make-day DAY:
    New-Item -Force -ItemType "Directory" -Path "day-$('{0:d2}' -f {{DAY}})"
    Copy-Item -Path "template.py" -Destination "day-$('{0:d2}' -f {{DAY}})/main.py"
    Touch-Item -Path "day-$('{0:d2}' -f {{DAY}})/example.txt"
    Touch-Item -Path "day-$('{0:d2}' -f {{DAY}})/input.txt"