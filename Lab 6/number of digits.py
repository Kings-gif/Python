# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:07:00 2025

@author: DELL
"""

def count_digits(number):
    # Handle negative numbers
    number = abs(number)

    # Special case for 0
    if number == 0:
        return 1

    count = 0
    while number > 0:
        count += 1
        number //= 10  # Remove the last digit
    return count


# Example usage
num = int(input("Enter a number: "))
print("Number of digits:", count_digits(num))
