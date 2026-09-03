"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 16: Searching

linear_search_algoritthm.py
-----------------------------------------------------------------------
This script demonstrates a classic "linear search" algorithm.

A linear search checks each item in a list one-by-one until it
either finds the target value (the "key") or reaches the end of
the list.

This version uses the modern 'with open(...)' pattern, which:
- automatically closes the file
- prevents resource leaks
- is cleaner and more Pythonic
- is the recommended approach in modern Python
"""

# ------------------------------------------------------------------
# STEP 1: Read the file and load names into a list
# ------------------------------------------------------------------
# 'with open(...)' creates a safe file-handling block.
# When the block ends, Python automatically closes the file
name_list = []

with open("super_villains.txt") as file:

    # Loop through each line in the file
    for line in file:

        # Remove newline characters and extra whitespace
        clean_name = line.strip()

        # Add the cleaned name to our list
        name_list.append(clean_name)

# -------------------------------------------------------------------
# STEP 2: Linear Search
# -------------------------------------------------------------------
# The "key" is the item we want to find in the list.
key = "Morgiana the Shrew"

# Start searching at index 0
i = 0

# ----------------------------------------------------------------------
# The search loop:
# ----------------------------------------------------------------------
# Continue looping WHILE:
#   - i is still inside the list
#   - AND the current item is NOT equal to the key
#
# This is the classic linear search condition.
while i < len(name_list) and name_list[i] != key:
    i += 1  # Move to the next index

# ---------------------------------------------------------------------
# STEP 3: Check if the key was found
# ---------------------------------------------------------------------
# If i is still inside the list, we found the key.
if i < len(name_list):
    print( "The name is at position", i)

# Otherwise, the loop reached the end without finding it.
else:
    print( "The name was not in the list." )
