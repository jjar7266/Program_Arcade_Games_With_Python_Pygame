"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

example of importing multiple custom modules and calling their functions

test_04.py
"""

# Import both modules. Each module defines a function named print_report().
# Because we import the *modules* (not the functions directly), each function
# stays inside its own namespace. This prevents collisions even though the
# function names are identical.
import student_functions
import financial_functions

# Call the student report function.
# Accessing the function through the module name keeps the namespace clear.
student_functions.print_report()

# Call the financial report function.
# This works safely because Python keeps each module's functions separate.
financial_functions.print_report()

# Notes:
# - If we used "from student_functions import print_report" and then imported
#   the financial version the same way, the second import would overwrite the
#   first one. That is a namespace collision.
# - Using module-level access (module.function()) avoids that problem entirely.
