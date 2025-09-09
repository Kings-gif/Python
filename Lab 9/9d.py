# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 12:16:17 2025

@author: DELL
"""

import pandas as pd

# Create two Series
s1 = pd.Series([1, 2, 3, 4])
s2 = pd.Series([5, 6, 7, 8])

print("Series 1:\n", s1, "\n")
print("Series 2:\n", s2, "\n")

# 1. Stack Vertically (one below another → like concatenation)
vertical_stack = pd.concat([s1, s2])
print("Stacked Vertically:\n", vertical_stack, "\n")

# 2. Stack Horizontally (side by side → like columns)
horizontal_stack = pd.concat([s1, s2], axis=1)
print("Stacked Horizontally:\n", horizontal_stack)
