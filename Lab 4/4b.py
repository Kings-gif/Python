# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:54:16 2025

@author: DELL
"""

def find_largest(numbers):
    largest = numbers[0]   # assume first element is the largest
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Example usage
my_list = [10, 25, 3, 99, 42]
print("The largest number in the list is:", find_largest(my_list))
