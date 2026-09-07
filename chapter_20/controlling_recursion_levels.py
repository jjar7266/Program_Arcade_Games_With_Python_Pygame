"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 20: Recursion

controlling_recursion_levels.py

To successfully use recursion, there needs to be a way to prevent the
function from endlessly calling itself over and over again. The example
below counts how many times it has been called, and uses an if statement
to exit once the function has called itself ten times.
"""

def f(level):
    """Print the current recursion level and stop at level 10."""
    print("Recursion call, level", level)

    # If we haven't reached level ten, call the function again
    if level < 10:
        f(level + 1)


# Start the recursive calls at level 1
f(1)
