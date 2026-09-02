"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

example of using an alias when importing a module

test_03.py
"""

# Import the entire module, but assign it an alias.
# This keeps the namespace clean and short, especially in larger projects.
# Using an alias is common when the module name is long or used frequently.
import my_functions as mf

# Call the foo() function through the alias.
# The alias 'mf' replaces the full module name, but still keeps the origin clear.
mf.foo()

# Notes:
# - This style is useful when a module has many functions you call often.
# - It avoids namespace clutter while still showing where the function came from.
# - Common Python libraries use this pattern (e.g., import numpy as np).
