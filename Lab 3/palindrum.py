# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:56:22 2025

@author: DELL
"""

# Function to check palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate checking
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Input from user
input_string = input("Enter a string: ")

# Check and print result
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
