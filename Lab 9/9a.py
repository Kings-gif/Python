# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 12:14:16 2025

@author: DELL
"""

import pandas as pd

# Create two Pandas Series
s1 = pd.Series([10, 20, 30, 40, 50])
s2 = pd.Series([2, 4, 6, 8, 10])

print("Series 1:\n", s1)
print("\nSeries 2:\n", s2)

# Addition
print("\nAddition of Series:\n", s1 + s2)

# Subtraction
print("\nSubtraction of Series:\n", s1 - s2)

# Multiplication
print("\nMultiplication of Series:\n", s1 * s2)

# Division
print("\nDivision of Series:\n", s1 / s2)
