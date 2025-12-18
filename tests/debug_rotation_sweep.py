
import numpy as np
import soundfile as sf
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from saf_wrapper import SAFRenderer

def run_sweep(sofa_path):
    print("--- ROTATION SWEEP TEST ---")
    
    fs = 48000
    duration_per_pos = 0.5 # seconds
    n_pos = 8 # 8 cardinal points
    # 0: Front(0), 1: FL(45), 2: Left(90), 3: BL(135), 4: Back(180), 5: BR(-135), 6: Right(-90), 7: FR(-45)
    
    angles = np.linspace(0, 2*np.pi, n_pos, endpoint=False)
    
    full_sig = []
    
    renderer = SAFRenderer()
    # Mock load to get SH basis for encoding (Reuse the function? No, it computes Matrix Y. We need vectors.)
    # Let's Implement basic 3rd order Encoder here.
    
    def encode_ambi(order, azi, ele, sig_chunk):
        # SN3D Encoder
        # Y_nm
        # We can use renderer.compute_real_sh_sn3d? Yes.
        # It handles arrays.
        Y = renderer.compute_real_sh_sn3d(order, np.array([azi]), np.array([ele])) 
        # Y shape (1, n_sh)
        # Sig shape (nsamps,)
        
        # Out: (nsamps, n_sh)
        return np.outer(sig_chunk, Y[0])
        
    order = 3 # Test Order 3 for higher resolution
    
    # Generate Input Signal
    input_ambi = []
    labels = []
    
    for i, ang in enumerate(angles):
        t = np.linspace(0, duration_per_pos, int(fs*duration_per_pos))
        # Sine burst
        sig = np.sin(2*np.pi*440*t) * np.hanning(len(t))
        
        chunk = encode_ambi(order, ang, 0, sig)
        input_ambi.append(chunk)
        labels.append(f"{np.rad2deg(ang):.0f} deg")
        
    input_ambi = np.vstack(input_ambi) # (TotalSamples, 4)
    
    # Write Temp Input
    sf.write("tests/sweep_in.wav", input_ambi, fs)
    
    # Run SAF Process
    renderer.load_sofa(sofa_path)
    # Force settings?
    
    renderer.process_file_chunked("tests/sweep_in.wav", "tests/sweep_out.wav")
    
    # Analyze Output
    y, _ = sf.read("tests/sweep_out.wav")
    
    # Split by chunks
    chunk_len = int(fs * duration_per_pos)
    
    print("\n--- RESULTS (RMS dB) ---")
    print(f"{'Angle':<10} | {'Left':<8} | {'Right':<8} | {'Diff (L-R)':<8}")
    
    for i in range(n_pos):
        start = i * chunk_len
        end = start + chunk_len
        if end > len(y): end = len(y)
        
        seg = y[start:end, :]
        rms_l = np.sqrt(np.mean(seg[:, 0]**2))
        rms_r = np.sqrt(np.mean(seg[:, 1]**2))
        
        db_l = 20*np.log10(rms_l + 1e-9)
        db_r = 20*np.log10(rms_r + 1e-9)
        
        print(f"{labels[i]:<10} | {db_l:.1f} dB  | {db_r:.1f} dB  | {db_l - db_r:.1f}")

if __name__ == "__main__":
    run_sweep(sys.argv[1])
