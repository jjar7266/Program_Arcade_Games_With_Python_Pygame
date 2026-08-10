"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Lab 6: Loopy Lab: 6.2 Part 2

lab_6_2.py
"""
# ============================================================
# Draw a box made of 'o' characters, size n
# ============================================================

# Ask the user for the size of the box.
# This number controls how tall the box is.
n = int(input("Enter the size of the box (n): "))

# The width of the box must be wider than the height.
# Notice in the examples:
#
# n = 3  -> width = 6
#
#          E.g. n = 3
#
#            oooooo
#            o    o
#            oooooo
#
# n = 8  -> width = 16
#
#          E.g. n = 8
#
#       oooooooooooooooo
#       o              o
#       o              o
#       o              o
#       o              o
#       o              o
#       o              o
#       oooooooooooooooo
#
# The pattern is: width = n * 2
width = n * 2

# -----------------------------------------------------------
# Step 1: Print the TOP of the box
# This is a solid line of o's with no spaces.
# Example: 000000 (when n = 3)
# -----------------------------------------------------------
print("o" * width)

# -----------------------------------------------------------
# Step 2: Print the MIDDLE of the box
# These rows have:
# - one 'o' on the left
# - spaces in the middle
# - one 'o' on the right
#
# We print (n - 2) middle rows because the top and bottom
# rows are already accounted for.
# ------------------------------------------------------------
for _ in range(n - 2):
    # One 'o' on the left
    # Spaces in the middle (width - 2 spaces)
    # One 'o' on the right
    print("o" + " " * (width - 2) + "o")

# -------------------------------------------------------------
# Step 3: Print the BOTTOM of the box
# Same as the top: a solid line of o's.
# -------------------------------------------------------------
print("o" * width)

