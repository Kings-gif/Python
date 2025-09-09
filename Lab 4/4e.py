# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:56:34 2025

@author: DELL
"""

def common_items(list1, list2):
    return list(set(list1) & set(list2))  # intersection of sets

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print("List 1:", list1)
print("List 2:", list2)
print("Common items:", common_items(list1, list2))
