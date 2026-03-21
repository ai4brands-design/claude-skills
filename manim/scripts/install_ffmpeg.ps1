# PowerShell script to download and install FFmpeg manually
$ffmpegUrl = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z"
$destFile = "$PWD\ffmpeg.7z"
$installDir = "$PWD\ffmpeg_tool"

Write-Host "Downloading FFmpeg from $ffmpegUrl..."
# Use GitHub release mirror if gyan is slow/blocked, but gyan is standard.
# Adding UserAgent to avoid some blocks.
Invoke-WebRequest -Uri $ffmpegUrl -OutFile $destFile -UserAgent "Mozilla/5.0"

Write-Host "Download complete. Extracting..."
# Windows 10/11 has tar but not 7z by default usually. 
# We'll try to use 7z if available, or assume the user has a way to extract 7z.
# Actually, gyan provides a zip file too. Let's use the zip for easier extraction with Powershell.
$ffmpegZipUrl = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.zip"
$destZip = "$PWD\ffmpeg.zip"

Write-Host "Switching to ZIP for easier extraction..."
Invoke-WebRequest -Uri $ffmpegZipUrl -OutFile $destZip -UserAgent "Mozilla/5.0"

Write-Host "Extracting ZIP..."
Expand-Archive -LiteralPath $destZip -DestinationPath $installDir -Force

$binPath = Get-ChildItem -Path $installDir -Recurse -Filter "ffmpeg.exe" | Select-Object -ExpandProperty DirectoryName -First 1

if ($binPath) {
    Write-Host "FFmpeg binary found at: $binPath"
    
    # Adding to User PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($currentPath -notlike "*$binPath*") {
        Write-Host "Adding to Path..."
        [Environment]::SetEnvironmentVariable("Path", "$currentPath;$binPath", "User")
        Write-Host "Added to User Path. You may need to restart your terminal."
    }
    else {
        Write-Host "Already in Path."
    }
}
else {
    Write-Host "Could not find ffmpeg.exe in extracted folder."
}
