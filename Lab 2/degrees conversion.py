# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:50:21 2025

@author: DELL
"""

# This program converts temperature from Celsius to Fahrenheit
# Formula: F = (C × 9/5) + 32

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print(f"{celsius}°C is equal to {fahrenheit}°F")
