# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 12:15:43 2025

@author: DELL
"""

import pandas as pd
import numpy as np

# 1. Create a Series from a Python list
list_data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(list_data)
print("Series from List:\n", series_from_list, "\n")

# 2. Create a Series from a NumPy array
array_data = np.array([100, 200, 300, 400, 500])
series_from_array = pd.Series(array_data)
print("Series from NumPy Array:\n", series_from_array, "\n")

# 3. Create a Series from a Dictionary
dict_data = {'a': 1, 'b': 2, 'c': 3}
series_from_dict = pd.Series(dict_data)
print("Series from Dictionary:\n", series_from_dict)
