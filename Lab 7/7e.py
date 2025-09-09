# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:11:41 2025

@author: DELL
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print("Size of each element in bytes:", arr.itemsize)
print("Total memory size in bytes:", arr.size * arr.itemsize)
