# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 12:01:16 2025

@author: DELL
"""

from PIL import Image
import numpy as np

# Load image
img = Image.open(r'C:\Users\DELL\Documents\WhatsApp Image 2025-08-29 at 15.31.32_1e7437f7.jpg')

# Convert to NumPy array for analysis
img_array = np.array(img)

# (a) Dimension of the image
dimension = img.size   # (width, height)

# (b) Shape of the image
shape = img_array.shape   # (rows, cols, channels)

# (c) Minimum pixel value at channel B (Blue = index 2)
min_blue = img_array[:, :, 2].min()

# Display results
print("Dimension of Image (width, height):", dimension)
print("Shape of Image (rows, cols, channels):", shape)
print("Minimum pixel value at Blue channel:", min_blue)
