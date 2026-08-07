"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 7: Back To Looping - Custom Exercise

exercise_9_4ways.py
"""
# Import modules
import subprocess  # Used to clear the terminal screen

# Clears the terminal screen
def clear_screen():
    subprocess.run("cls", shell=True)

# EXERCISE 9
# --------------------------------------------------------
# COMBINATION 1: (original exercise)
# Spaces FIRST, Numbers SECOND
# This creates a RIGHT-JUSTIFIED shrinking triangle.
# --------------------------------------------------------

# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0

def exercise9():
    clear_screen()
    for i in range(10):

        # Print spaces first.
        # More spaces each row -> numbers shift right.
        for s in range(i):
            print(" ", end=" ")

        # Print shrinking numbers.
        # Row 0 prints 10 numbers, row 1 prints 9, etc.
        for j in range(10 - i):
            print(j, end=" ")

        print()

# ==================================================================
# COMBINATION 2
# Numbers FIRST, Spaces SECOND
# This creates a LEFT-JUSTIFIED shrinking triangle.
# ------------------------------------------------------------------

# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

def exercise9_2():
    clear_screen()
    for i in range(10):

        # Print shrinking numbers first.
        # Because numbers come first, they stay left-aligned.
        for j in range(10 - i):
            print(j, end=" ")

        # Print spaces AFTER the numbers.
        # These do not affect alignment.
        for s in range(i):
            print(" ", end=" ")

        print()

# ==================================================================
# COMBINATION 3
# Reverse Numbers FIRST, Spaces SECOND
# This creates a LEFT-JUSTIFIED triangle with DESCENDING numbers.
# ------------------------------------------------------------------

# 9 8 7 6 5 4 3 2 1 0
# 8 7 6 5 4 3 2 1 0
# 7 6 5 4 3 2 1 0
# 6 5 4 3 2 1 0
# 5 4 3 2 1 0
# 4 3 2 1 0
# 3 2 1 0
# 2 1 0
# 1 0
# 0

def exercise9_3():
    clear_screen()
    for i in range(10):

        # Print reversed shrinking numbers.
        # Row 0: 9 8 7 6 5 4 3 2 1 0
        # Row 1: 8 7 6 5 4 3 2 1 0
        # Row 2: 7 6 5 4 3 2 1 0
        for j in range(9- i, -1, -1):
            print(j, end=" ")

        # Spaces come AFTER numbers.
        for s in range(i):
            print(" ", end=" ")

        print()

# ==================================================================
# COMBINATION 4
# Spaces FIRST, Reverse Numbers SECOND
# This creates a RIGHT-JUSTIFIED triangle with DESCENDING numbers.
# ------------------------------------------------------------------

# 9 8 7 6 5 4 3 2 1 0
#   8 7 6 5 4 3 2 1 0
#     7 6 5 4 3 2 1 0
#       6 5 4 3 2 1 0
#         5 4 3 2 1 0
#           4 3 2 1 0
#             3 2 1 0
#               2 1 0
#                 1 0
#                   0

def exercise9_4():
    clear_screen()
    for i in range(10):

        # Print spaces first.
        # More spaces each row -> numbers shift right.
        for s in range(i):
            print(" ", end=" ")

        # Print reversed shrinking numbers.
        for j in range(9 - i, -1, -1):
            print(j, end=" ")

        print()











# Uncomment the exercise you want to run

#exercise9()
#exercise9_2()
#exercise9_3()
#exercise9_4()
