"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) by: Jose 'Joe' Ruiz

Chapter 16: Lab 15 - Spell Check

lab15_spell_check.py
"""

# --- Import modules ---
import re  # Regular expressions are used to split text into words.

# --- Function: split_line ---
#
# This function takes a line of text and returns a list of words.
# It removes punctuation and keeps only alphabetic sequences.
# The regex also supports words with apostrophes (like "Dinah'll")
#
# We place this function at the top of the file because functions
# should always be defined before they are used.
# ======================================================================

def split_line(line):
    return re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", line)

# --- Step 1: Load dictionary.txt into a list name dictionary_list
#
# We use 'with open' so the files closes automatically.
# Each word is stripped of whitespace and converted to uppercase.
# Uppercase makes searching easier because comparisons are consistent.
# ======================================================================

dictionary_list = []

with open("dictionary.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Remove whitespace/newline and convert to uppercase
        dictionary_list.append(line.strip().upper())


# --- Step 2: Linear Search Spell Check
# ======================================================================

print("--- Linear Search ---")

# open the first chapter of Alice in Wonderland.
# We do NOT load the entire file into a list - we process it line by line.
with open("AliceInWonderLand200.txt", "r", encoding="utf-8") as file:

    # Track which line number we are currently reading.
    line_number = 0

    # Loop through each line in the stroy.
    for line in file:
        line_number += 1

        # Split the current line into individual words.
        # The split_line function returns a list of cleaned words.
        words = split_line(line)

        # Loop through each word in the current line.
        for word in words:

            # Convert the current word to uppercase for comparison.
            key = word.upper()

            # --- Linear Search ---
            i = 0
            found = False

            # Walk through dictionary_list until we find the word
            # or reach the end of the dictionary.
            while i < len(dictionary_list) and dictionary_list[i] != key:
                i += 1

            # If i is still inside the list, the word was found.
            if i < len(dictionary_list):
                found = True

            # If not found, print the line number and the word.
            if not found:
                print(f"Line {line_number} possible misspelled word: {word}")


# --- Step 3: Binary Search Spell Check
# ===================================================================

print("--- Binary Search ---")

with open("AliceInWonderLand200.txt", "r", encoding="utf-8") as file:

    line_number = 0

    for line in file:
        line_number += 1
        words = split_line(line)

        for word in words:

            key = word.upper()

            # --- Binary Search ---
            lower_bound = 0
            upper_bound = len(dictionary_list) -1
            found = False

            # Continue searching while the bounds are valid.
            while lower_bound <= upper_bound and not found:

                middle_pos = (lower_bound + upper_bound) // 2
                middle_value = dictionary_list[middle_pos]

                if middle_value == key:
                    found = True

                elif key < middle_value:
                    upper_bound = middle_pos - 1

                else:
                    lower_bound = middle_pos + 1

            # If not found, print the line number and the word.
            if not found:
                print(f"Line {line_number} possible misspelled word: {word}")

                

