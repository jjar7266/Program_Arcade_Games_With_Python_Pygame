"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 20: Recursion

example_binary_search.py
"""

# Load the villain names from the text file
name_list = []

with open("super_villains.txt", "r", encoding="utf-8") as file:
    for line in file:
        name_list.append(line.strip())

# Non-recursive binary search

def binary_search_nonrecursive(search_list, key):
    """
    Search for 'key' in 'search_list' using a standard binary search loop.
    """

    lower_bound = 0
    upper_bound = len(search_list) - 1
    found = False

    # Keep searching while the bounds are valid
    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if search_list[middle_pos] < key:
            lower_bound = middle_pos + 1

        elif search_list[middle_pos] > key:
            upper_bound = middle_pos - 1

        else:
            found = True

    if found:
        print( "The name is at position", middle_pos)
    else:
        print( "The name was not in the list." )


# Recursive binary search

def binary_search_recursive(search_list, key, lower_bound, upper_bound):
    """
    Recursively search for 'key' in 'search_list'.
    """

    # Base case: bounds crossed -> not found
    if lower_bound > upper_bound:
        print("The name was not in the list.")
        return

    middle_pos = (lower_bound + upper_bound) // 2

    if search_list[middle_pos] < key:
        binary_search_recursive(
            search_list,
            key,
            middle_pos + 1,
            upper_bound
        )

    elif search_list[middle_pos] > key:
        binary_search_recursive(
            search_list,
            key,
            lower_bound,
            middle_pos - 1
        )

    else:
        print("Found at position", middle_pos)


# Example usage
# Assumes name_list already exists (from previous chapter examples)
binary_search_nonrecursive(name_list, "Morgiana the Shrew")

lower_bound = 0
upper_bound = len(name_list) - 1

binary_search_recursive(
    name_list,
    "Morgiana the Shrew",
    lower_bound,
    upper_bound
)
