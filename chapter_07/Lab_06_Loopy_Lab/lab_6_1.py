"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Lab 6: Loopy Lab: 6.1 Part 1

lab_6_1.py

--------------------------------------------------------
Write a Python program that will print the following:

10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36 37
38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54

--------------------------------------------------------
"""

# We begin with the number the triangle should start printing.
# The assignment says the first printed number must be 10.
current_number = 10


# The outer loop controls HOW MANY ROWS we print.
# The pattern shows 9 rows total, so we loop from 1 through 9.
# We start at 1 because the first row prints 1 number,
# the second row prints 2 numbers, the third prints 3, etc.
for row in range(1, 10):  # range(1, 9 + 1) also works
    # The inner loop prints the numbers inside each row.
    # The number of items printed in each row equals the row number.
    # Example: row 3 -> print 3 numbers.
    for _ in range(row):
        # Print the current number, but stay on the same line.
        # end=" " keeps the numbers spaced horizontally.
        print(current_number, end=" ")

        # Increase the number so the next print shows the next value.
        # This is the key idea: the counter is independent of the loops.
        current_number += 1

    # After finishing one row, print a blank newline
    # so the next row starts on its own line.
    print()
