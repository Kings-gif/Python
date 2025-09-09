# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:10:48 2025

@author: DELL
"""

# Input from user
num = int(input("Enter a number: "))

# Handle negative numbers
num = abs(num)

product = 1

# Special case for 0
if num == 0:
    product = 0
else:
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10

# Output
print("Product of digits:", product)
