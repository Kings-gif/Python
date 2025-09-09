# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:57:23 2025

@author: DELL
"""

# Function to check if the string contains only digits
def is_digits_only(s):
    return s.isdigit()

# Input from user
input_string = input("Enter a string: ")

# Check and print result
if is_digits_only(input_string):
    print(f'The string "{input_string}" contains only digits.')
else:
    print(f'The string "{input_string}" does not contain only digits.')
