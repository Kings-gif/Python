# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:05:32 2025

@author: DELL
"""

# Input from the user
n = int(input("Enter a positive number: "))

# Initialize sum
total = 0
num = 1

# While loop to add numbers
while num <= n:
    total += num
    num += 1

# Display result
print("The sum of natural numbers from 1 to", n, "is:", total)
