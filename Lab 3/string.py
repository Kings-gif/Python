# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:55:10 2025

@author: DELL
"""

# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Input from user
input_string = input("Enter a string: ")

# Call the function and print the reversed string
reversed_str = reverse_string(input_string)
print("Reversed string:", reversed_str)
