
import sys
import os
import numpy as np
import argparse

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from saf_wrapper import SAFRenderer

def check_sofa_coords(sofa_path):
    renderer = SAFRenderer()
    renderer.load_sofa(sofa_path)
    
    # Dump first 5 source positions
    n_sofa = renderer.hSOFA.nSources
    src_pos_flat = np.frombuffer(renderer.ffi.buffer(renderer.hSOFA.SourcePosition, n_sofa*3*4), dtype=np.float32)
    sofa_pos = src_pos_flat.reshape(n_sofa, 3)
    
    print("\n--- SOFA POSITIONS INSPECTION ---")
    print("First 5 Positions:")
    for i in range(5):
        print(f"[{i}] {sofa_pos[i]}")
        
    # Check max range to infer units
    max_val = np.max(np.abs(sofa_pos))
    print(f"Max Coordinate Value: {max_val}")
    if max_val > 2*np.pi:
        print("Likely DEGREES.")
    else:
        print("Likely RADIANS (or Normalized Cartesian).")
        
    # Coordinate Logic in Wrapper
    is_degrees = max_val > 2*np.pi
    azi = sofa_pos[:, 0].copy()
    ele = sofa_pos[:, 1].copy()
    
    if is_degrees:
        azi_rad = np.deg2rad(azi)
        ele_rad = np.deg2rad(ele)
    else:
        azi_rad = azi
        ele_rad = ele
        
    print(f"First 5 Converted to Radians (Azi, Ele):")
    for i in range(5):
        print(f"[{i}] Azi: {azi_rad[i]:.4f}, Ele: {ele_rad[i]:.4f}")


def check_sh_math():
    print("\n--- SH MATH VERIFICATION ---")
    renderer = SAFRenderer()
    
    # 1. Front (0, 0)
    # 2. Left (90, 0) -> +Y
    # 3. Back (180, 0) -> -X
    # 4. Right (-90, 0) -> -Y
    # 5. Up (0, 90) -> +Z
    
    test_dirs = [
        ("Front (+X)", 0, 0),
        ("Left (+Y)", np.pi/2, 0),
        ("Back (-X)", np.pi, 0),
        ("Right (-Y)", -np.pi/2, 0),
        ("Up (+Z)", 0, np.pi/2)
    ]
    
    for name, az, el in test_dirs:
        Y = renderer.compute_real_sh_sn3d(1, np.array([az]), np.array([el]))
        # Round for readability
        Y_r = np.round(Y[0], 3)
        print(f"{name}: {Y_r}  (Expected: [1, Y, Z, X] Mapping)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sofa", required=True)
    args = parser.parse_args()
    
    check_sh_math()
    check_sofa_coords(args.sofa)
