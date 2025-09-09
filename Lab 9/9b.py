# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 12:15:11 2025

@author: DELL
"""

import pandas as pd

# Create a dictionary
data = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

print("Dictionary:\n", data)

# Convert dictionary to Pandas Series
series = pd.Series(data)

print("\nPandas Series:\n", series)
