"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Lab 6: Loopy Lab: 6.3 Part 3

lab_6_3.py

# =================================================================
# Symmetric odd-number box pattern
# =================================================================

E.g. n = 3

1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1

E.g. n = 5

1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1
"""
# =================================================================

# -----------------------------------------------------------------
# Step 1: Ask the user for input
# -----------------------------------------------------------------
# We need a positive integer n.
# This n controls:
#   - How many rows appear in the top half
#   - How many rows appear in the bottom half
#   - The largest odd number printed (which is 2*n - 1)
#   - The width of the pattern
n = int(input("Enter n: "))

# =================================================================
# PART 1: TOP HALF (Row 0 up to n-1)
# =================================================================
# We loop upward: i = 0, 1, 2 ..., n-1
# Each row i determines:
#   - The starting odd number (2*i + 1)
#   - How many spaces appear in the middle
#   - How far the left and right sides extend
# =================================================================
for i in range(n):

    # -------------------------------------------------------------
    # Compute the first odd number for this row.
    # Example:
    #   i = 0 -> start_num = 1
    #   i = 1 -> start_num = 3
    #   i = 2 -> start_num = 5
    # -------------------------------------------------------------
    start_num = 2 * i + 1

    # -------------------------------------------------------------
    # LEFT SIDE: Count upward by 2s
    # -------------------------------------------------------------
    # We print odd numbers starting at start_num,
    # increasing by 2 each time, stopping before 2*n.
    #
    # Example for n = 5:
    #   Row i = 0 -> print: 1 3 5 7 9
    #   Row i = 1 -> print: 3 5 7 9
    #   Row i = 2 -> print: 5 7 9
    #
    # This creates the shrinking left side.
    # -------------------------------------------------------------
    for k in range(start_num, 2 * n, 2):
        print(k, end=" ")

    # -------------------------------------------------------------
    # MIDDLE SPACES
    # -------------------------------------------------------------
    # The middle gap grows as i increases.
    # Each "slot" is printed as two spaces ("  ").
    #
    # Why 2*i?
    #   - Row 0 -> 0 spaces
    #   - Row 1 -> 2 spaces
    #   - Row 2 -> 4 spaces
    #
    # This creates the widening hollow center.
    # -------------------------------------------------------------
    print("  " * (2 * i), end="")

    # -------------------------------------------------------------
    # RIGHT SIDE: Count downward by 2s
    # -------------------------------------------------------------
    # We print odd numbers starting from the largest (2*n - 1),
    # decreasing by 2 each time, stopping just above start_num.
    #
    # Example for n = 5:
    #   Row i = 0 -> print: 9 7 5 3 1
    #   Row i = 1 -> print: 9 7 5 3
    #   Row i = 2 -> print: 9 7 5
    #
    # This mirrors the left side.
    # -------------------------------------------------------------
    for k in range(2 * n - 1, start_num - 1, -2):
        print(k, end=" ")

    # End the row and move to the next line
    print()

# =================================================================
# PART 2: BOTTOM HALF (Row n-1 down to 0)
# =================================================================
# This is almost identical to the top half,
# except we loop downward to mirror the pattern.
#
# Rows:
#   i = n-1, n-2, ..., 1, 0
# =================================================================
for i in range(n - 1, -1, -1):

    # Same starting odd number formula as before
    start_num = 2 * i + 1

    # LEFT SIDE (same logic as top half)
    for k in range(start_num, 2 * n, 2):
        print(k, end=" ")

    # MIDDLE SPACES (same logic as top half)
    print("  " * (2 * i), end="")

    # RIGHT SIDE (same logic as top half)
    for k in range(2 * n - 1, start_num - 1, -2):
        print(k, end=" ")

    # End the row
    print()

