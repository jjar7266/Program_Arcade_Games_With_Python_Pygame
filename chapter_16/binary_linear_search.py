"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 16: Searching

binary_linear_search.py
"""

# --- Load the text file into a list
# Using 'with open' ensures the file is automatically closed, even if errors occur.

name_list = []

# Open the file in read mode with UTF-8 encoding for safety.
# The file must be in the same directory as this script.
with open("super_villains.txt", "r", encoding="utf-8") as file:
    for line in file:
        # Strip newline and surrounding whitespace, then store the name.
        name_list.append(line.strip())

# At this point, 'name_list' is a fully populated, sorted list of villain names.


# --- Binary search -----------------------------------------------

key = "Brutus the Gruesome"       # The name we want to locate
lower_bound = 0                   # Start index of the search range
upper_bound = len(name_list) -1   # End index of the search range
found = False                     # Flag to indicate success

# Continue searching while the bounds are valid AND the item hasn't been found.
while lower_bound <= upper_bound and not found:

    # Middle index of the current search range.
    middle_pos = (lower_bound + upper_bound) // 2
    middle_value = name_list[middle_pos]

    # Compare the middle value with the key.
    if middle_value < key:
        # The key must be in the upper half.
        lower_bound = middle_pos + 1

    elif middle_value > key:
        # The key must be in the lower half.
        upper_bound = middle_pos - 1

    else:
        # Exact match found.
        found = True

# --- Final result --------------------------------------------------

if found:
    print( "The name is at position", middle_pos)
else:
    print( "The name was not in the list.")

