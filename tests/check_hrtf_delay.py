
import sys
import os
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from saf_wrapper import SAFRenderer

def check_delays(sofa_path):
    renderer = SAFRenderer()
    renderer.load_sofa(sofa_path)
    
    n_sofa = renderer.hSOFA.nSources
    n_receivers = renderer.hSOFA.nReceivers # Should be 2 (Ears)
    
    # Check if DataDelay is NULL
    if renderer.hSOFA.DataDelay == renderer.ffi.NULL:
        print("DataDelay is NULL.")
        return

    # Try using netCDF4 directly
    print("\n--- CHECKING WITH NETCDF4 ---")
    try:
        import netCDF4
        ds = netCDF4.Dataset(sofa_path, 'r')
        if 'Data.Delay' in ds.variables:
            dd = ds.variables['Data.Delay'][:]
            print(f"Data.Delay Shape: {dd.shape}")
            print(f"Data.Delay Values (First 5): \n{dd[:5]}")
            print(f"Max Delay: {np.max(dd)}")
        else:
            print("Data.Delay variable NOT found in netCDF.")
        ds.close()
    except Exception as e:
        print(f"netCDF4 Error: {e}")

    # Inspect first few values
    count = n_sofa * n_receivers
    try:
        # Try FLOAT (float32)
        # delay_ptr = renderer.ffi.buffer(renderer.hSOFA.DataDelay, count * 4)
        # delays = np.frombuffer(delay_ptr, dtype=np.float32).reshape(n_sofa, n_receivers)
        
        # Try DOUBLE (float64)
        print("Attempting to read as DOUBLE (float64)...")
        delay_ptr = renderer.ffi.buffer(renderer.hSOFA.DataDelay, count * 8)
        delays = np.frombuffer(delay_ptr, dtype=np.float64).reshape(n_sofa, n_receivers)
        
        print(f"\n--- SOFA DELAY INSPECTION ---")
        print(f"Shape: {delays.shape}")
        
        print("First 5 Delays (Samples? Seconds?):")
        for i in range(5):
            print(f"[{i}] L={delays[i,0]}, R={delays[i,1]}")
            
        print(f"Max Delay: {np.max(delays)}")
        print(f"Min Delay: {np.min(delays)}")
        
        if np.max(delays) == 0:
            print("DELAYS ARE ALL ZERO. (File is likely Time-Aligned or delay is explicit in IR)")
        else:
            print("NON-ZERO DELAYS FOUND! These MUST be applied.")
            
    except Exception as e:
        print(f"Error reading delays: {e}")
        # Could be (1, R)
        try:
             delay_ptr = renderer.ffi.buffer(renderer.hSOFA.DataDelay, 2 * 4)
             delays = np.frombuffer(delay_ptr, dtype=np.float32)
             print(f"Fallback (1, R) Read: {delays}")
        except:
             pass

if __name__ == "__main__":
    check_delays(sys.argv[1])
