"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

example of using the import you created

test_02.py
"""

# Import only the foo() function directly from my_functions.py.
# This pulls the function into the local namespace, allowing us to call foo()
# without prefixing it with the module name.
from my_functions import foo

# Call the imported foo() function.
# This style is concise, but in larger projects it can clutter the namespace
# because the origin of the function is less obvious.
foo()

# Alternative (used in test.py):
# import my_functions
# my_functions.foo()
# This keeps the namespace organized and makes it clear where foo() comes from.
