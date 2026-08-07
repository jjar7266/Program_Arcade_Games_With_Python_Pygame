"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 7: Back To Looping - Custom Exercise

exercise_10.py
"""
# ------------------------------------------------------------------
# EXERCISE 10
# Multiplication table with alignment.
# We print a 9x9 table where each cell is row * col.
# ------------------------------------------------------------------

#  1  2  3  4  5  6  7  8  9
#  2  4  6  8 10 12 14 16 18
#  3  6  9 12 15 18 21 24 27
#  4  8 12 16 20 24 28 32 36
#  5 10 15 20 25 30 35 40 45
#  6 12 18 24 30 36 42 48 54
#  7 14 21 28 35 42 49 56 63
#  8 16 24 32 40 48 56 64 72
#  9 18 27 36 45 54 63 72 81

for row in range(1, 10):          # Rows 1 through 9

    for col in range(1, 10):      # Columns 1 through 9

        value = row * col         # Compute the multiplication result

        # -----------------------------------------------------------
        # ALIGNMENT LOGIC
        # -----------------------------------------------------------
        # If the number is a single digit (1-9), print ONE space
        # BEFORE the number. This pushes single-digit numbers to the right
        # so that all columns line up evenly.
        #
        # Example:
        #  3  6  9 12 15
        #
        # Notice how 3, 6, 9 have a leading space.
        if value < 10:
            print(" ", end="")   # Leading space for single digits

        # Print the number itself, followed by ONE space.
        print(value, end=" ")

    print()  # Move to the next row
