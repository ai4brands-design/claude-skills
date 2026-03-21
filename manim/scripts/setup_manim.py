import subprocess
import sys
import shutil

def install_package(package):
    print(f"Installing {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

def check_ffmpeg():
    if shutil.which("ffmpeg"):
        print("FFmpeg is found on PATH.")
    else:
        print("WARNING: FFmpeg not found on PATH. Manim requires FFmpeg.")
        print("Please download it from https://ffmpeg.org/download.html and add it to your PATH.")

def main():
    print("Setting up Manim environment...")
    
    # Install Manim Community
    install_package("manim")
    
    # Check for FFmpeg
    check_ffmpeg()
    
    print("\nSetup complete (with potential warnings above).")
    print("Try running the example in SKILL.md to verify.")

if __name__ == "__main__":
    main()
