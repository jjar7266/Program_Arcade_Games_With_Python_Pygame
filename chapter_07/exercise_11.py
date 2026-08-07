"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 7: Back To Looping - Custom Exercise

exercise_11.py
"""
# -------------------------------------------------------------
# PATTERN WE ARE TRYING TO CREATE (Exercise 11)
# -------------------------------------------------------------
# This is a CENTERED PYRAMID made from three parts:
#   1) Leading spaces
#   2) Ascending numbers
#   3) Descending numbers
#
# Each row grows outward symmetrically:
#
#                 1
#               1 2 1
#             1 2 3 2 1
#           1 2 3 4 3 2 1
#         1 2 3 4 5 4 3 2 1
#       1 2 3 4 5 6 5 4 3 2 1
#     1 2 3 4 5 6 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
#
# Notice:
# - Spaces DECREASE each row (centering)
# - Ascending numbers INCREASE each row
# - Descending numbers MIRROR the ascending side
#
# This creates a perfectly centered, symmetrical pyramid.
# -------------------------------------------------------------

for row in range(1, 10):   # Rows 1 through 9

    # ---------------------------------------------------------
    # 1. LEADING SPACES
    # ---------------------------------------------------------
    # The pyramid is centered by printing spaces BEFORE the numbers.
    # As the row increases, the number of spaces decreases.
    #
    # Row 1 -> 8 spaces
    # Row 2 -> 7 spaces
    # Row 3 -> 6 spaces
    # ...
    # Row 9 -> 0 spaces
    #
    # Each space is printed as " " (space) + " " (separator),
    # which keeps the pyramid visually balanced.
    for space in range(9 - row):
        print(" ", end=" ")

    # ---------------------------------------------------------
    # 2. ASCENDING NUMBERS
    # ---------------------------------------------------------
    # Count upward from 1 to the current row number.
    #
    # Row 4 -> 1 2 3 4
    #
    # This builds the left half of the pyramid.
    for num in range(1, row + 1):
        print(num, end=" ")

    # ----------------------------------------------------------
    # DESCENDING NUMBERS
    # ----------------------------------------------------------
    # Mirror the ascending numbers by counting downward.
    #
    # Row 4 -> 3 2 1
    #
    # This builds the right half of the pyramid.
    for num in range(row - 1, 0, -1):
        print(num, end=" ")

    print()  # Move to the next row
