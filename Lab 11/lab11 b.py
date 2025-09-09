# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 12:02:38 2025

@author: DELL
"""

from PIL import Image, ImageOps

# Load image
img = Image.open(r'C:\Users\DELL\Documents\WhatsApp Image 2025-08-29 at 15.31.32_1e7437f7.jpg')

# Padding size (left, top, right, bottom)
padding = (50, 50, 50, 50)  # 50 pixels on all sides

# Add black padding
padded_img = ImageOps.expand(img, border=padding, fill="black")

# Show and save result
padded_img.show()
padded_img.save("padded_output.jpg")
