"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 18: Sorting

swapping_values.py
"""

# A simple list of integers. In sorting algorithms, lists like this
# are repeatedly rearranged to place items in the correct order.
my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

# The goal: swap the values at index 0 and index 2.
# Before the swap:
#  my_list[0] == 15
#  my_list[2] == 14
#
# Many sorting algorithms (like bubble sort or selective sort)
# rely on this exact operation: comparing two values and swapping
# them if they are out of order.

# Store the value at index 0 in a temporary variable.
# This prevents the original value from being overwritten.
temp = my_list[0]

# Move the value from index 2 into index 0.
my_list[0] = my_list[2]

# Move the saved value (original index 0) into index 2.
my_list[2] = temp

# After the swap:
#  my_list[0] == 14
#  my_list[2] == 15
# The rest of the list remains unchanged.
print(my_list)

# Python provides a built-in shortcut for swapping values.
# It does the same thing as the temp-variable method, but in one line.

my_list[0], my_list[2] = my_list[2], my_list[0]

# This works because Python evaluates the right-hand side first,
# creates a temporary tuple (my_list[2], my_list[0]),
# then unpacks it back into the left-hand side.
#
# It's clean, safe, and commonly used in modern Python code.
print(my_list)  # back to the original list
