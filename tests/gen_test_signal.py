
import soundfile as sf
import numpy as np

def generate_test_signal():
    fs = 48000
    duration = 2.0
    t = np.linspace(0, duration, int(fs*duration))
    
    # 1st Order Ambisonics (4 Channels)
    # Ch 0: W (Omni) - Sine Wave 440Hz
    # Ch 1, 2, 3: Y, Z, X - Zeros (Silence)
    
    sig = np.sin(2 * np.pi * 440 * t)
    
    n_ch = 4
    data = np.zeros((len(t), n_ch), dtype=np.float32)
    data[:, 0] = sig * 0.5 # -6dB
    
    # Add a blip in X (Ch 3) at 1s to test directionality
    # ACN 3 is X (Front)
    # data[int(fs*1.0):int(fs*1.1), 3] = 0.5
    
    output_file = "test_input.wav"
    sf.write(output_file, data, fs)
    print(f"Generated {output_file}")

if __name__ == "__main__":
    generate_test_signal()
