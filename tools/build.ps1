$ErrorActionPreference = "stop"

Push-Location "${PSScriptRoot}/.."
pyinstaller "shuttle.spec"
Remove-Item -Path "./build" -Recurse -Force
Pop-Location
