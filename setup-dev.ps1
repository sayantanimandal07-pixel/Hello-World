# ================================================
# Dev Environment Setup Script
# Installs Git + Node.js + npm + Freebuff
# Fixes PATH automatically
# Windows 10/11
# ================================================

Write-Host "====================================="
Write-Host "Installing Development Environment..."
Write-Host "====================================="

# Check Winget
if (!(Get-Command winget -ErrorAction SilentlyContinue)) {
    Write-Host "Winget is not installed."
    Write-Host "Install App Installer from Microsoft Store."
    exit
}

# Install Git
Write-Host ""
Write-Host "Installing Git..."

winget install --id Git.Git -e --source winget --accept-package-agreements --accept-source-agreements

# Install Node.js LTS
Write-Host ""
Write-Host "Installing Node.js LTS..."

winget install --id OpenJS.NodeJS.LTS --source winget --accept-package-agreements --accept-source-agreements

# Wait
Start-Sleep -Seconds 5

# Git Path
$gitPath = "C:\Program Files\Git\cmd"

if (Test-Path $gitPath) {

    $machine = [Environment]::GetEnvironmentVariable("Path","Machine")

    if ($machine -notlike "*$gitPath*") {
        [Environment]::SetEnvironmentVariable(
            "Path",
            $machine + ";" + $gitPath,
            "Machine"
        )
    }

    $env:Path += ";$gitPath"
}

# Node Path
$nodePath = "C:\Program Files\nodejs"

if (Test-Path $nodePath) {

    $machine = [Environment]::GetEnvironmentVariable("Path","Machine")

    if ($machine -notlike "*$nodePath*") {
        [Environment]::SetEnvironmentVariable(
            "Path",
            $machine + ";" + $nodePath,
            "Machine"
        )
    }

    $env:Path += ";$nodePath"
}

Write-Host ""
Write-Host "Refreshing Environment..."

$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [Environment]::GetEnvironmentVariable("Path","User")

Write-Host ""
Write-Host "Checking Git..."

if (Get-Command git -ErrorAction SilentlyContinue) {
    git --version
}
else {
    & "C:\Program Files\Git\cmd\git.exe" --version
}

Write-Host ""
Write-Host "Checking Node..."

if (Get-Command node -ErrorAction SilentlyContinue) {
    node --version
}

Write-Host ""
Write-Host "Checking npm..."

if (Get-Command npm -ErrorAction SilentlyContinue) {
    npm --version
}

Write-Host ""
Write-Host "Installing Freebuff..."

npm install -g freebuff

Write-Host ""
Write-Host "Checking Freebuff..."

freebuff --version

Write-Host ""
Write-Host "====================================="
Write-Host "Setup Completed Successfully!"
Write-Host "====================================="
Write-Host ""
Write-Host "Git:"
git --version

Write-Host ""
Write-Host "Node:"
node --version

Write-Host ""
Write-Host "npm:"
npm --version

Write-Host ""
Write-Host "Freebuff:"
freebuff --version

Write-Host ""
Write-Host "Restart Windows Terminal once."