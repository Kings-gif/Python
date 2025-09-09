# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:59:43 2025

@author: DELL
"""

# Function to find the length of the last word
def length_of_last_word(sentence):
    words = sentence.strip().split()
    if words:
        return len(words[-1])
    else:
        return 0  # No words in the sentence

# Input from user
input_sentence = input("Enter a sentence: ")

# Find and print the length of the last word
length = length_of_last_word(input_sentence)
print(f'The length of the last word is: {length}')
