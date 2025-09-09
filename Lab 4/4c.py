# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:55:07 2025

@author: DELL
"""

def remove_duplicates(my_list):
    return list(set(my_list))  # convert to set then back to list

# Example usage
my_list = [1, 2, 3, 2, 4, 1, 5, 3]
print("Original list:", my_list)
print("List after removing duplicates:", remove_duplicates(my_list))
