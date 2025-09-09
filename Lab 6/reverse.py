# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:12:11 2025

@author: DELL
"""

# Input from user
num = int(input("Enter a number: "))

# Handle negative numbers
sign = -1 if num < 0 else 1
num = abs(num)

# Reverse the number
reverse_num = 0
while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

# Restore sign for negative numbers
reverse_num *= sign

# Output
print("Reversed number:", reverse_num)
