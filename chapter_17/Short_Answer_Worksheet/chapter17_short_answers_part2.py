"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 17: Functions - Array-Backed Grids
Short Answer Worksheet - Part 2

This file contains the solution for Worksheet Question #2:
* Implements a celebrity-finding function using a matrix (list-of-lists).
* A celebrity is known by everyone, but knows no one except themselves.
* Includes multiple test cases provided in the worksheet.

chapter17_short_answers_part1.py
"""

def check_celebrity(grid):
    """ Given an n x n matrix, print all celebrities. """

    n = len(grid)

    for person in range(n):
        knows_no_one = True
        known_by_everyone = True

        # Check if person knows anyone besides themselves
        for other in range(n):
            if other != person and grid[person][other] == 1:
                knows_no_one = False

        # Check if everyone knows this person
        for other in range(n):
            if grid[other][person] == 0:
                known_by_everyone = False

        if knows_no_one and known_by_everyone:
            print(person, "is a celebrity.")
            return

    print("No celebrities found.")


print("Test 1, Should show #2 is a celebrity.")
grid = [ [1, 1, 1, 0],
         [0, 1, 1, 0],
         [0, 0, 1, 0],
         [1, 0, 1, 1] ]
check_celebrity(grid)

print("\nTest 2, Should show no one is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0],
         [1, 0, 0, 1, 1],
         [1, 0, 0, 1, 1] ]
check_celebrity(grid)

print("\nTest 3, Should show #2 is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [0, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1] ]
check_celebrity(grid)

print("\nTest 4, Should show no one is a celebrity.")
grid = [ [1, 1, 1, 0, 1],
         [0, 1, 1, 0, 1],
         [1, 0, 1, 0, 0],
         [0, 0, 1, 0, 1],
         [1, 0, 1, 1, 1] ]
check_celebrity(grid)
