
import sys
import os
import numpy as np

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from saf_wrapper import SAFRenderer

def test_sh_generation():
    print("Testing SH Generation (SN3D)...")
    renderer = SAFRenderer()
    
    # Test Directions: Front, Left, Up
    # Azi, Ele in Rads
    dirs = np.array([
        [0, 0],         # Front (X)
        [np.pi/2, 0],   # Left (Y) -> AmbiX uses positive Y to left usually? "Positive y-axis points to the left" implies Azi=90.
        [0, np.pi/2]    # Up (Z)
    ], dtype=np.float32)
    
    Y = renderer.compute_real_sh_sn3d(1, dirs[:,0], dirs[:,1])
    
    print("Computed SH (Order 1):")
    print(Y)
    
    # Expected (SN3D/ACN):
    # Order 1: [W, Y, Z, X] -> Indices [0, 1, 2, 3]
    # Front (1,0,0): W=1, X=1, Y=0, Z=0. -> [1, 0, 0, 1]
    # Left (0,1,0): W=1, X=0, Y=1, Z=0. -> [1, 1, 0, 0]
    # Up (0,0,1):   W=1, X=0, Y=0, Z=1. -> [1, 0, 1, 0]
    
    tol = 1e-4
    
    # Check Front
    if not np.allclose(Y[0], [1, 0, 0, 1], atol=tol):
        print("FAIL: Front Direction Incorrect")
        print(f"Got: {Y[0]}")
    else:
        print("PASS: Front Direction")

    # Check Left
    if not np.allclose(Y[1], [1, 1, 0, 0], atol=tol):
        print("FAIL: Left Direction Incorrect")
        print(f"Got: {Y[1]}")
    else:
        print("PASS: Left Direction")

    # Check Up
    if not np.allclose(Y[2], [1, 0, 1, 0], atol=tol):
        print("FAIL: Up Direction Incorrect")
        print(f"Got: {Y[2]}")
    else:
        print("PASS: Up Direction")

if __name__ == "__main__":
    test_sh_generation()
