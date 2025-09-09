# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 12:04:07 2025

@author: DELL
"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load image
img = Image.open(r'C:\Users\DELL\Documents\WhatsApp Image 2025-08-29 at 15.31.32_1e7437f7.jpg')

# Convert to NumPy array
img_array = np.array(img)

# Split channels
red_channel   = img_array[:, :, 0]
green_channel = img_array[:, :, 1]
blue_channel  = img_array[:, :, 2]

# Plot original + RGB channels
plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(red_channel, cmap="Reds")
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(green_channel, cmap="Greens")
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(blue_channel, cmap="Blues")
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()
