# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:45:33 2025

@author: DELL
"""

# Input length and width from user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display results
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)
