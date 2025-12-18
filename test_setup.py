import sys
import os
import shutil
from PyQt6.QtWidgets import QApplication

# Add src to path
sys.path.append(os.path.join(os.getcwd(), 'src'))

from common_ui import AssetManager

def test_assets():
    print("--- Testing AssetManager ---")
    
    # Initialize App for QFontDatabase
    app = QApplication(sys.argv)
    
    print("Running AssetManager.ensure_assets()...")
    AssetManager.ensure_assets()
    
    # Verify files
    assets_dir = AssetManager.ASSET_DIR
    fonts = AssetManager.FONTS.keys()
    
    missing = []
    for f in fonts:
        path = os.path.join(assets_dir, f)
        exists = os.path.exists(path)
        print(f"File {f}: {'FOUND' if exists else 'MISSING'} ({path})")
        if not exists:
            missing.append(f)
            
    if missing:
        print("FAIL: Assets missing.")
    else:
        print("PASS: All assets present.")

def test_ffmpeg():
    print("\n--- Testing FFmpeg Capabilities ---")
    import subprocess
    
    try:
        result = subprocess.run(['ffmpeg', '-filters'], capture_output=True, text=True)
        if result.returncode != 0:
            print("FAIL: ffmpeg command returned error.")
            return

        has_sofalizer = "sofalizer" in result.stdout
        print(f"Filter 'sofalizer' found: {has_sofalizer}")
        
        if not has_sofalizer:
            print("WARNING: 'sofalizer' is missing. The App will show a Critical Error on launch.")
        else:
            print("PASS: FFmpeg is ready for HRTF.")
            
    except FileNotFoundError:
        print("FAIL: ffmpeg binary not found in PATH.")

if __name__ == "__main__":
    test_assets()
    test_ffmpeg()
