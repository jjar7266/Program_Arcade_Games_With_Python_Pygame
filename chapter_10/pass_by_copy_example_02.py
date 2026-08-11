"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Variable Scope

Pass-by-copy

pass_by_copy_example_02.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/


# Explanation video: https://www.youtube.com/watch?v=_zE5zs_hleQ


# Define a simple function that prints x
def f(x):
    # --------------------------------------------------------------
    # TEACHER MODE:
    # Even though the GLOBAL variable is also named x,
    # the function parameter x is a completely DIFFERENT variable.
    #
    # When we call f(x), Python does this internally:
    #       x_local = x_global
    #       x_local = 10
    #
    # The parameter x (inside the function) is a NEW, LOCAL variable.
    # It *shadows* the global x, meaning the local one temporarily
    # hides the global one while inside the function.
    #
    # STUDENT MODE (OH WOW I GET IT):
    # Ohhhh… so even if the names MATCH, they are NOT the same x!
    # The function creates its OWN x, using the value I passed in.
    #
    # So inside the function:
    #       x starts as 10
    #       x becomes 11
    #       print(x) prints 11
    #
    # But the global x OUTSIDE the function never changes.
    # --------------------------------------------------------------
    x += 1
    print(x)

# Set x
x = 10

# Call the function
f(x)      # This creates a NEW local x = 10 inside the function

# Print x to see if it changed
print(x)  # This prints the ORIGINAL global x, still 10
