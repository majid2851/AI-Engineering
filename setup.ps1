# Install dependencies using the project venv (NOT PyCharm's bundled pip)
$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
$Python = Join-Path $ProjectRoot "venv\Scripts\python.exe"

if (-not (Test-Path $Python)) {
    Write-Host "Creating virtual environment..."
    py -m venv (Join-Path $ProjectRoot "venv")
}

Write-Host "Python: $(& $Python --version)"
Write-Host "Upgrading pip..."
& $Python -m pip install --upgrade pip setuptools wheel

Write-Host "Installing requirements (this may take several minutes)..."
& $Python -m pip install -r (Join-Path $ProjectRoot "requirements.txt")

Write-Host ""
Write-Host "Verifying core packages..."
& $Python -c "import numpy; print('numpy OK:', numpy.__version__)"
& $Python -c "import cv2; print('opencv OK:', cv2.__version__)" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "opencv not yet installed or failed" }
& $Python -c "import ultralytics; print('ultralytics OK')" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "ultralytics not yet installed or failed" }

Write-Host ""
Write-Host "Done. Use this interpreter in PyCharm:"
Write-Host "  $Python"
