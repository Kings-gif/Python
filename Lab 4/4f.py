# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:57:00 2025

@author: DELL
"""

def list_to_integer(my_list):
    return int("".join(map(str, my_list)))

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)
print("Converted integer:", list_to_integer(my_list))
