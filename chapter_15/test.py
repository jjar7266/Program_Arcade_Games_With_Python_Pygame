"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

example of using the import you created

test.py
"""
# Import the module so we can access its functions.
# This loads the entire my_functions.py file as a module.
# Python looks for my_functions.py in the same folder as this script.
# If it isn't found, Python will search the system path and installed packages.
import my_functions

# Call the foo() functions that lives inside my_functions.py.
# Using module.function() keeps the namespace clean and avoids name collisions.
# This pattern scales well as your project grows and you add more functions.
my_functions.foo()


