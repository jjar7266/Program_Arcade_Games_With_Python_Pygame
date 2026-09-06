"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 19: Exceptions

example_01.py

Example: Handling different types of errors
"""

# Import modules
import sys

# -------------------------------------------------------------
# This program shows how Python handles mistakes (called "errors").
# Instead of crashing, we can catch the error and print a message.
# -------------------------------------------------------------

try:
    # Try to open a file named "myfile.txt".
    # If the file is missing, Python will complain.
    with open("myfile.txt", "r") as my_file:
        # Read one line of text from the file.
        my_line = my_file.readline()

    # Take away extra spaces or newlines from the text.
    cleaned = my_line.strip()

    # Try to turn the cleaned text into a number.
    # If the text is not a number, Python will raise an error.
    my_int = int(cleaned)

    # Try to divide 101 by the number we got.
    # If the number is zero, dividing will cause an error.
    my_calculated_value = 101 / my_int

    # If everything worked, show the answer.
    print("Calculated value:", my_calculated_value)

# --------------------------------------------------------------------
# These blocks catch a different kinds of errors.
# Each one prints a message so the program doesn't crash.
# --------------------------------------------------------------------

except IOError:
    # This happens when the file can't be opened.
    print("I/O error: Could not open 'myfile.txt'.")

except ValueError:
    # This happens when the text can't be turned into a number
    print("ValueError: Could not convert file data to an integer.")

except ZeroDivisionError:
    # This happens when we try to divide by zero.
    print("ZeroDivisionError: Division by zero is not allowed.")

except Exception:
    # This catches any other error we didn't expect.
    print("Unexpected error:", sys.exc_info()[0])


