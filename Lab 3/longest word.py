# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:58:41 2025

@author: DELL
"""

# Function to find the longest word in a sentence
def longest_word(sentence):
    words = sentence.split()
    longest = max(words, key=len)
    return longest

# Input from user
input_sentence = input("Enter a sentence: ")

# Find and print the longest word
longest = longest_word(input_sentence)
print(f'The longest word is: "{longest}"')
