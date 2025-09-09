# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:10:41 2025

@author: DELL
"""

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])

common = np.intersect1d(arr1, arr2)
print("Common values:", common)
