# Set shell for non-Windows OSs:
set shell := ["powershell", "-c"]

# Set shell for Windows OSs:
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

make-day DAY:
    Copy-Item -Recurse -Path "template/" -Destination "day-$('{0:d2}' -f {{DAY}})"
