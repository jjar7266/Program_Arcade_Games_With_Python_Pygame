"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 7: Back To Looping

Advanced Looping Problems
"""

# Import modules
import subprocess  # Used to clear the terminal screen

# Clears the terminal screen
def clear_screen():
    subprocess.run("cls", shell=True)

# -----------------------------------------------------------------
# 1. Write code that will print 10 asterisks(*) like the following
# -----------------------------------------------------------------

#    * * * * * * * * * *

def exercise1():
    clear_screen()
    for i in range(10):
        print("*", end=" ")
    print()

# -------------------------------------------------------------------
# 2 write code that will print the following:
# -------------------------------------------------------------------

#   * * * * * * * * * *
#   * * * * *
#   * * * * * * * * * * * * * * * * * * * *

def exercise2():
    clear_screen()

    # Line 1
    for i in range(10):
        print("*", end=" ")
    print()

    # Line 2
    for i in range(5):
        print("*", end=" ")
    print()

    # Line 3
    for i in range(20):
        print("*", end=" ")
    print()

# -----------------------------------------------------------------
# 3. Use two for loops, one of them nested inside the other,
# to print the following 10x10 rectangle:
# ------------------------------------------------------------------

#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *
#   * * * * * * * * * *

def exercise3():
    clear_screen()
    for row in range(10):
        for i in range(10):
            print("*", end=" ")
        print()

# -------------------------------------------------------------
# 4. Use two for loops, one of them nested, to print
# the following 5x10 rectangle:
# -------------------------------------------------------------

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def exercise4():
    clear_screen()
    for row in range(10):
        for i in range(5):
            print("*", end=" ")
        print()

# ----------------------------------------------------------
# 5. Use two for loops, one of them nested, to print the
# following 20x5 rectangle:

# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * * *

def exercise5():
    clear_screen()
    for row in range(5):
        for col in range(20):
            print("*", end=" ")
        print()

# --------------------------------------------------------------
# 6. Write code that will print the following:
# --------------------------------------------------------------

# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9
# 0 1 2 3 4 5 6 7 8 9

def exercise6():
    clear_screen()
    for i in range(10):
        for j in range(10):
            print(j, end=" ")
        print()

# -------------------------------------------------------------
# 7. Adjust the prior program to print:
# -------------------------------------------------------------
# 0 0 0 0 0 0 0 0 0 0
# 1 1 1 1 1 1 1 1 1 1
# 2 2 2 2 2 2 2 2 2 2
# 3 3 3 3 3 3 3 3 3 3
# 4 4 4 4 4 4 4 4 4 4
# 5 5 5 5 5 5 5 5 5 5
# 6 6 6 6 6 6 6 6 6 6
# 7 7 7 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9 9

def exercise7():
    clear_screen()
    for i in range(10):
        for j in range(10):
            print(i, end=" ")
        print()

# --------------------------------------------------------
# 8. Write code that will print the following:
# --------------------------------------------------------

# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4
# 0 1 2 3 4 5
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5 6 7
# 0 1 2 3 4 5 6 7 8
# 0 1 2 3 4 5 6 7 8 9

def exercise8():
    clear_screen()
    for i in range(10):
        for j in range(i + 1):
            print(j, end=" ")
        print()

# --------------------------------------------------------
# 9 Write code that will print the following:
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
# This one is difficult. Tip: Two loops are needed inside the outer loop
# that controls each row. First, a loop prints spaces, then a loop
# prints the numbers. Loop both these for each row. To start with,
# try writing just one inside loop that prints:

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

# Then once that is working, add a loop after the outside loop starts
# and before the already existing inside loop. Use this new loop to
# print enough spaces to right justify the other loops.

def exercise9():
    clear_screen()
    for i in range(10):
        for s in range(i):
            print(" ", end=" ")
        for j in range(10 - i):
            print(j, end=" ")
        print()

# -------------------------------------------------------
# 10.Write code that will print the following
# (Getting the alignment is hard, at least get the numbers):
# --------------------------------------------------------

# 1   2   3   4   5   6   7   8   9
# 2   4   6   8  10  12  14  16  18
# 3   6   9  12  15  18  21  24  27
# 4   8  12  16  20  24  28  32  36
# 5  10  15  20  25  30  35  40  45
# 6  12  18  24  30  36  42  48  54
# 7  14  21  28  35  42  49  56  63
# 8  16  24  32  40  48  56  64  72
# 9  18  27  36  45  54  63  72  81

# Tip: Start by adjusting the code in problem 1 to print:

# 0  0  0  0  0  0  0  0  0  0
# 0  1  2  3  4  5  6  7  8  9
# 0  2  4  6  8  10  12  14  16  18
# 0  3  6  9  12  15  18  21  24  27
# 0  4  8  12  16  20  24  28  32  36
# 0  5  10  15  20  25  30  35  40  45
# 0  6  12  18  24  30  36  42  48  54
# 0  7  14  21  28  35  42  49  56  63
# 0  8  16  24  32  40  48  56  64  72
# 0  9  18  27  36  45  54  63  72  81

# Then adjust the code to print:

# 1  2  3  4  5  6  7  8  9
# 2  4  6  8  10  12  14  16  18
# 3  6  9  12  15  18  21  24  27
# 4  8  12  16  20  24  28  32  36
# 5  10  15  20  25  30  35  40  45
# 6  12  18  24  30  36  42  48  54
# 7  14  21  28  35  42  49  56  63
# 8  16  24  32  40  48  56  64  72
# 9  18  27  36  45  54  63  72  81

# Finally, use an if to print spaces if the number being
# printed is less than 10.

def exercise10():
    clear_screen()
    for row in range(1, 10):
        for col in range(1, 10):
            value = row * col
            if value < 10:
                print(" ", end="")  # Leading space for single digits

            # Print the number itself, followed by ONE space
            print(value, end= " ")

        print()  # Move to the next row

# ------------------------------------------------------
# 11. Write code that will print the following:
# ------------------------------------------------------
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

# Tip: first write code to print:

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

# Then write code to print:

# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 5 6 5 4 3 2 1
# 1 2 3 4 5 6 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

# Then finish by adding spaces to print the final answer.

def exercise11():
    clear_screen()

    # We will print 9 rows total.
    # Each row builds a bigger pyramid.
    for i in range(1, 10):

        # ---------------------------------------------------
        # 1. PRINT LEADING SPACES
        # ---------------------------------------------------
        # The pyramid needs to be centered.
        # The top row has the MOST spaces.
        # The bottom row has the FEWEST spaces.
        #
        # Example:
        # Row 1 -> lots of spaces
        # Row 2 -> fewer spaces
        # Row 9 -> almost no spaces
        #
        # We print (10 - i) spaces to push the numbers to the right.
        for s in range(10 - i):
            print(" ", end=" ")

        # ------------------------------------------------------
        # 2. PRINT ASCENDING NUMBERS (LEFT SIDE)
        # ------------------------------------------------------
        # This prints:
        # Row 1: 1
        # Row 2: 1 2
        # Row 3: 1 2 3
        # ...
        # Row i: 1 2 3 ... i
        #
        # This builds the left half of the pyramid.
        for j in range(1, i + 1):
            print(j, end=" ")

        # ------------------------------------------------------
        # 3. PRINT DESCENDING NUMBERS (RIGHT SIDE)
        # ------------------------------------------------------
        # This mirrors the left side.
        #
        # Row 1: (nothing)
        # Row 2: 2 1
        # Row 3: 3 2 1
        # Row 4: 4 3 2 1
        #
        # Notice we start at (i - 1) because the peak number
        # should not be printed twice.
        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        # --------------------------------------------------------
        # 4. MOVE TO THE NEXT LINE
        # --------------------------------------------------------
        print()

# ----------------------------------------------------------------
# 12. Write code that will print the following:
# ----------------------------------------------------------------
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
# This can be done by combining problems 11 and 9.

def exercise12():
    clear_screen()

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

        print()  # Next row

# ------------------------------------------------------------------
# 13. Write code that will print the following:
# ------------------------------------------------------------------
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

def exercise13():
    clear_screen()

    # ------------------------------------------------------------
    # PART 1: TOP HALF OF THE DIAMOND (Problem 11)
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

        # Print the left side: 1 up to i
        for j in range(1, i + 1):
            print(j, end=" ")

        # Print the right side: i-1 down to 1
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
    # This is the same logic as the top half,
    # but counting DOWN instead of UP.
    #
    for i in range(8, 0, -1):

        # Print spaces to center the shrinking rows.
        for s in range(10 - i):
            print(" ", end=" ")

        # Print the left side: 1 up to i
        for j in range(1, i + 1):
            print(j, end=" ")

        # Print the right side i-1 down to 1
        for j in range(i - 1, 0, -1):
            print(j, end=" ")

        print()  # Next row


# Uncomment the exercise you want to run

#exercise1()
#exercise2()
#exercise3()
#exercise4()
#exercise5()
#exercise6()
#exercise7()
#exercise8()
#exercise9()
#exercise10()
#exercise11()
#exercise12()
#exercise13()
