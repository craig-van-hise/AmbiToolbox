
import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from saf_wrapper import SAFRenderer

def check_energy(sofa_path):
    renderer = SAFRenderer()
    renderer.load_sofa(sofa_path)
    renderer.prepare(1) # Order 1
    
    print(f"Sample Rate: {renderer.sofa_data['fs']}")
    
    # sh_hrtfs: (4, 2, 128) for Order 1
    # 0: W
    # 1: Y (Left)
    # 2: Z (Up)
    # 3: X (Front)
    
    filters = renderer.sh_hrtfs
    
    print("\n--- HRTF SH ENERGY ANALYSIS ---")
    
    # Function to get energy in dB
    def get_energy(h):
        e = np.sum(h**2)
        return e
        
    labels = ["W (Omni)", "Y (Left)", "Z (Up)", "X (Front)"]
    
    for i in range(4):
        e_L = get_energy(filters[i, 0, :])
        e_R = get_energy(filters[i, 1, :])
        print(f"Ch {i} [{labels[i]}]: L={e_L:.4f}, R={e_R:.4f}")
        
    # Check Symmetry
    # Y (Left) Dipole:
    # Left Ear should correlate positively with Y (Positive on left).
    # Right Ear should correlate negatively? 
    # Energies might be similar if head is symmetric, but signs differ.
    
    # Check Dominance
    e_Y = get_energy(filters[1])
    e_Z = get_energy(filters[2])
    e_X = get_energy(filters[3])
    
    print(f"\nTotal Energy: Y(LR)={e_Y:.4f}, Z(LR)={e_Z:.4f}, X(LR)={e_X:.4f}")
    
    if e_Z > e_X and e_Z > e_Y:
        print("WARNING: Z (Up) Channel has highest energy. Possible Axis Swap?")
    else:
        print("Energy distribution looks plausible (Horizontal > Vertical).")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 check_hrtf_energy.py <sofa>")
        sys.exit(1)
    check_energy(sys.argv[1])
