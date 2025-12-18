
import sys
import numpy as np
import netCDF4

def check_sofa_netcdf(sofa_path):
    print(f"Opening {sofa_path} with netCDF4...")
    try:
        ds = netCDF4.Dataset(sofa_path, 'r')
        
        # Check standard variables
        print("Variables found:", list(ds.variables.keys()))
        
        # 1. Delays
        if 'Data.Delay' in ds.variables:
            delays = ds.variables['Data.Delay'][:]
            print(f"Data.Delay Shape: {delays.shape}")
            print(f"Data.Delay (First 5): \n{delays[:5]}")
            print(f"Delay Min: {np.min(delays)}")
            print(f"Delay Max: {np.max(delays)}")
        else:
            print("Data.Delay MISSING")
            
        # 2. IRs
        if 'Data.IR' in ds.variables:
            ir = ds.variables['Data.IR']
            print(f"Data.IR Shape: {ir.shape}")
        
        # 3. Positions 
        if 'SourcePosition' in ds.variables:
            src = ds.variables['SourcePosition'][:]
            print(f"SourcePosition Shape: {src.shape}")
            print(f"First Source: {src[0]}")
            
        ds.close()
        print("Success.")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    check_sofa_netcdf(sys.argv[1])
