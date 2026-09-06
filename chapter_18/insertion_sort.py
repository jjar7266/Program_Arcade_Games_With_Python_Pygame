"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 18: Sorting

insertion_sort.py

This example demonstrates the insertion sort algorithm. It reuses the
print_list() helper from the previous sorting example to avoid repeating
the same formatting code.
"""

# Import modules
import random
from selection_sort import print_list  # Reuse the existing helper


def insertion_sort(my_list):
    """
    Sort a list using the insertion sort algorithm.

    Concept:
    - The left side of the list becomes a growing sorted section.
    - Each new value (the key) is inserted into its correct position
      inside that sorted section.
    - Larger values shift right to make space for the key.

    This algorithm is efficient for small lists or lists that are
    already mostly sorted.
    """

    # Start at index 1 because index 0 is already "sorted" by definition.
    for key_pos in range(1, len(my_list)):

        # Store the value we want to insert into the sorted portion.
        key_value = my_list[key_pos]

        # Begin scanning leftward from the position just before key_pos.
        scan_pos = key_pos - 1

        # Shift values to the right until the correct spot for
        # key_value is found
        #
        # Conditions:
        # - scan_pos >= 0 keeps us inside the list.
        # - my_list[scan_pos] > key_value means the current value is too large
        #   and must be moved right.
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        # Insert key_value into the correct sorted position.
        my_list[scan_pos + 1] = key_value


# Create a list of random numbers to demonstrate the sort.
my_list = [random.randrange(100) for _ in range(10)]

print("Before sorting:")
print_list(my_list)

insertion_sort(my_list)

print("After sorting:")
print_list(my_list)

