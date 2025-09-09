# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:49:18 2025

@author: DELL
"""

# This program calculates z = (x + y) * (x + y) - 2 * x * y
# Mathematically, (x + y)^2 - 2xy simplifies to x^2 + y^2

# Input values for x and y
x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))

# Calculate z
z = (x + y) * (x + y) - 2 * x * y

# Display result
print(f"z = {z}")
