# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:09:42 2025

@author: DELL
"""

# Input from user
num = int(input("Enter a number: "))

# Convert to string for easier manipulation
num_str = str(abs(num))  # handle negatives

# If the number has only one digit, no swap needed
if len(num_str) == 1:
    swapped_num_str = num_str
else:
    swapped_num_str = num_str[-1] + num_str[1:-1] + num_str[0]

# Convert back to integer
swapped_num = int(swapped_num_str)

# Preserve sign if original was negative
if num < 0:
    swapped_num = -swapped_num

# Output
print("Number after swapping first and last digits:", swapped_num)
