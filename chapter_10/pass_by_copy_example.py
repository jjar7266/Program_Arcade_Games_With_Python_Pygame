"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Variable Scope

Pass-by-copy

pass_by_copy_example.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/


# Explanation video: https://www.youtube.com/watch?v=_zE5zs_hleQ


# Define a simple function that prints x
def f(x):
    # ---------------------------------------------------------------
    # TEACHER MODE:
    # When we write "def f(x:)", we are telling Python:
    #   "This function needs a value, and whatever value is passed
    #    in will be stored in a NEW, LOCAL variable named x."
    #
    # So when we later call f(y), Python does this internally:
    #       x = y
    #       x = 10
    #
    # STUDENT MODE (OH WOW I GET IT):
    # ohhhh... x *does* exist! I don't define x myself - the
    # function call f(y) DEFINES x by giving it the value of y.
    #
    # x is NOT y. x is just a COPY of y.
    # Changing x does NOT change y.
    # ----------------------------------------------------------------
    x += 1
    print(x)


# Set y
y = 10

# Call the function
f(y)      # This makes x = 10 inside the function

# Print y to see if it changed
print(y)  # y stays 10 because only x was changed
