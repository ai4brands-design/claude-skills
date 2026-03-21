# PowerShell script to setup Slidev
$targetDir = Read-Host "Enter the directory name for your presentation (default: my-slides)"
if ([string]::IsNullOrWhiteSpace($targetDir)) {
    $targetDir = "my-slides"
}

if (Test-Path $targetDir) {
    Write-Host "Directory $targetDir already exists. Please choose another name or delete it first."
    exit 1
}

Write-Host "Initializing Slidev project in $targetDir..."
# We use npx to init. The -y flag accepts defaults.
npx -y slidev@latest init $targetDir

Write-Host "Done! To start:"
Write-Host "  cd $targetDir"
Write-Host "  npm run dev"
