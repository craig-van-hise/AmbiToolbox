import sys
import os
import numpy as np

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from saf_wrapper import SAFRenderer

def test_saf():
    print("Testing SAF Renderer...")
    
    # 1. Initialize
    try:
        renderer = SAFRenderer()
        print("Initialization Success.")
    except Exception as e:
        print(f"Initialization Failed: {e}")
        sys.exit(1)
        
    # 2. Load SOFA
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sofa_path = os.path.join(base_dir, "..", "assets", "hrtf", "Neumann_KU100_THK.sofa")
    
    if not os.path.exists(sofa_path):
        print(f"Skipping SOFA test (File not found: {sofa_path})")
    else:
        try:
            renderer.load_sofa(sofa_path)
            print("SOFA Load Success.")
        except Exception as e:
            print(f"SOFA Load Failed: {e}")
            sys.exit(1)

        # 3. Prepare Grid (Order 1 -> 4 channels)
        try:
            renderer.prepare(order=1)
            print("Grid Preparation Success.")
        except Exception as e:
            print(f"Grid Preparation Failed: {e}")
            # Do not exit, try to continue? No, fatal.
            sys.exit(1)
            
        # 4. Process Silence (WAV)
        import soundfile as sf
        dummy_wav = "test_silence.wav"
        out_wav = "test_out.wav"
        
        # Create 1 second 4ch silent wav
        data = np.zeros((48000, 4), dtype=np.float32)
        sf.write(dummy_wav, data, 48000)
        
        try:
            renderer.process_file_chunked(dummy_wav, out_wav)
            print("Processing Success.")
            if os.path.exists(out_wav):
                 print("Output file created.")
        except Exception as e:
             print(f"Processing Failed: {e}")
             sys.exit(1)
        finally:
             if os.path.exists(dummy_wav): os.remove(dummy_wav)
             if os.path.exists(out_wav): os.remove(out_wav)

if __name__ == "__main__":
    test_saf()
