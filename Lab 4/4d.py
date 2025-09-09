# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:55:48 2025

@author: DELL
"""

def frequency_of_elements(my_list):
    freq = {}
    for item in my_list:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 4, 5]
print("Original list:", my_list)
print("Frequency of elements:", frequency_of_elements(my_list))
