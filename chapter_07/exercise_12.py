"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 7: Back To Looping - Custom Exercise

exercise_12.py
"""
# ------------------------------------------------------------------
# EXERCISE 12
# ------------------------------------------------------------------
#
# Combined pyramid pattern:
# - Top half: full pyramid (ascending + descending numbers)
# - Bottom half: shrinking pyramid (ascending numbers only)
#
# This is created by combining:
#   - Problem 11 (full pyramid)
#   - Problem 9 (shrinking pyramid)
#
# ------------------------------------------------------------------
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
#   1 2 3 4 5 6 7 8
#     1 2 3 4 5 6 7
#       1 2 3 4 5 6
#         1 2 3 4 5
#           1 2 3 4
#             1 2 3
#               1 2
#                 1
#
# Notice:
# - The top half grows outward symmetrically.
# - The bottom half shrinks inward symmetrically.
# - Each row is centered using spaces.
# ------------------------------------------------------------------
# ------------------------------------------------------------
# PART 1: PRINT THE TOP HALF (the big pyramid from problem 11)
# ------------------------------------------------------------
#
# This prints rows 1 through 9:
#
#                   1
#                 1 2 1
#               1 2 3 2 1
#             1 2 3 4 3 2 1
#           1 2 3 4 5 4 3 2 1
#        1 2 3 4 5 6 5 4 3 2 1
#      1 2 3 4 5 6 7 6 5 4 3 2 1
#    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
#  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
#
for i in range(1, 10):

    # Print spaces to push the row to the right.
    # As i gets smaller, we print more spaces.
    for s in range(10 - i):
        print(" ", end=" ")

    # Print the left side: 1 up to i
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print the right side: i-1 down to 1
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # Move to next row

# ------------------------------------------------------------
# PART 2: PRINT THE BOTTOM HALF (the shrinking pyramid)
# ------------------------------------------------------------
#
# This prints rows 8 down to 1:
#
#    1 2 3 4 5 6 7 8
#      1 2 3 4 5 6 7
#        1 2 3 4 5 6
#          1 2 3 4 5
#            1 2 3 4
#              1 2 3
#                1 2
#                  1
#
# Notice: this is just problem 9, but with numbers instead of 0–9.
#
for i in range(8, 0, -1):

    # Print spaces to push the row to the right.
    # As i gets smaller, we print more spaces.
    for s in range(10 - i):
        print(" ", end=" ")

    # Print numbers from 1 up to i
    for j in range(1, i + 1):
        print(j, end=" ")

    print()

