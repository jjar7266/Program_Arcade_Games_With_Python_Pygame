"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 7: Back To Looping - Custom Exercise

exercise_13.py
"""
# ------------------------------------------------------------------
# EXERCISE 13
# ------------------------------------------------------------------
#
# Full diamond pattern using numbers.
# This combines two pyramids:
#   - Top half: grows outward (ascending + descending numbers)
#   - Bottom half: shrinks inward (ascending + descending numbers)
#
# The result is a perfectly symmetrical diamond.
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
#   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
#     1 2 3 4 5 6 7 6 5 4 3 2 1
#       1 2 3 4 5 6 5 4 3 2 1
#         1 2 3 4 5 4 3 2 1
#           1 2 3 4 3 2 1
#             1 2 3 2 1
#               1 2 1
#                 1
# ------------------------------------------------------------------

# ------------------------------------------------------------
# PART 1: TOP HALF OF THE DIAMOND
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

    # Print spaces to center the pyramid.
    # The top row has the most spaces.
    for s in range(10 - i):
        print(" ", end=" ")

    # Print ascending numbers (left side)
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print descending numbers (right side)
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # Move to next row

# ------------------------------------------------------------
# PART 2: BOTTOM HALF OF THE DIAMOND
# ------------------------------------------------------------
#
# This prints rows 8 down to 1:
#
#    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
#      1 2 3 4 5 6 7 6 5 4 3 2 1
#        1 2 3 4 5 6 5 4 3 2 1
#          1 2 3 4 5 4 3 2 1
#            1 2 3 4 3 2 1
#              1 2 3 2 1
#                1 2 1
#                  1
#
# This mirrors the top half, but counts DOWN instead of UP.
#
for i in range(8, 0, -1):

    # Print spaces to center the shrinking rows.
    for s in range(10 - i):
        print(" ", end=" ")

    # Print ascending numbers (left side)
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print descending numbers (right side)
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # Next row
