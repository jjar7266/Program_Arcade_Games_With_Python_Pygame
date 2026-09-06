"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 18: Sorting

selection_sort.py
"""

# Import modules
import random

def selection_sort(my_list):
    """ Sort a list using the selection sort algorithm.

    This function modifies the list in-place, arranging the values
    in ascending order.

    Core idea:
    - For each position in the list (from left to right), find the
      smallest value in the remaining unsorted portion.
    - Swap that smallest value into the current postion.
    """

    # The outer loop moves from left to right across the list.
    # cur_pos represents the position where the next smallest
    # value should be placed.
    for cur_pos in range(len(my_list)):

        # Assume the current position holds the smallest value.
        # min_pos will track the index of the smallest value found
        # during the inner scan.
        min_pos = cur_pos

        # The inner loop scans the rest of the list (to the right of cur_pos)
        # to find the true smallest value.
        for scan_pos in range(cur_pos + 1, len(my_list)):

            # Compare the value at scan_pos with the current minimum.
            # If a smaller value is found, undate min_pos.
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        # After the inner loop finishes. min_pos holds the index of
        # the smallest value in the unsorted portion of the list.

        # Swap the value at min_pos with the value at cur_pos so that
        # the smallest value moves into its correct postion.
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

        # At this point:
        # - All positions before cur_pos are sorted.
        # - Positions from cur_pos onward are still being processed.


def print_list(my_list):
    """
    Print the contents of a list in a compact, formatted way.

    Each item is printed with a width of 3 characters, side by side.
    This makes it easy to visually compare the list before and after sorting.
    """
    for item in my_list:
        # "{:3}".format(item) formats the number in a field of width 3.
        # end="" prevents automatic newlines between items.
        print("{:3}".format(item), end="")

    # Print a final new line after the entire list
    print()


# Only run this test code when the file is executed directly,
# NOT when imported by another module.
if __name__ == "__main__":

    # Create a list of random numbers to demonstrate the sort.
    my_list = []

    # Generate 10 random integers between 0 and 99.
    for i in range(10):
        my_list.append(random.randrange(100))

    # Show the list before sorting
    print("Before sorting:")
    print_list(my_list)

    # Sort the list using selection sort.
    selection_sort(my_list)

    # Show the list after sorting.
    print_list(my_list)
