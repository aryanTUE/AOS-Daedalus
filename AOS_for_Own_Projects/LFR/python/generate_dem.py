# Run this once to generate a placeholder dem.obj
# Save as generate_dem.py in your LFR/python folder and run it

import numpy as np
from PIL import Image
import os

# Load the dem.png to get dimensions
dem_png_path = r"..\data\F0\DEM\dem.png"
img = Image.open(dem_png_path)
w, h = img.size
print(f"DEM image size: {w} x {h}")

# Generate a flat OBJ mesh at z=0 with correct proportions
out_path = r"..\data\F0\DEM\dem.obj"

with open(out_path, 'w') as f:
    f.write("# Flat placeholder DEM mesh\n")
    # Write vertices (4 corners of a flat plane)
    f.write(f"v 0 0 0\n")
    f.write(f"v {w} 0 0\n")
    f.write(f"v {w} {h} 0\n")
    f.write(f"v 0 {h} 0\n")
    # Write faces (2 triangles)
    f.write("f 1 2 3\n")
    f.write("f 1 3 4\n")

print(f"Generated placeholder dem.obj at {out_path}")
