# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:07:58 2025

@author: DELL
"""

# Input from user
num = int(input("Enter a number: "))

# Handle negative numbers
num = abs(num)

# Find last digit
last_digit = num % 10

# Find first digit
first_digit = num
while first_digit >= 10:
    first_digit //= 10

# Output
print("First digit:", first_digit)
print("Last digit:", last_digit)
