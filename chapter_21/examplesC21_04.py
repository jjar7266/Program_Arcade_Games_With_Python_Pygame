"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting - Floating Point Numbers

examplesC21_04.py
"""

# Import modules
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


# ----------------------------------------------------------------
# Example 01: Floating-point formatting with precision
# ----------------------------------------------------------------
def ex_01():
    """
    Demonstrate floating-point formatting using both {:.N} and {:.Nf}.

    {:.N}   -> formats the number with N significant digits.
    {:.Nf}  -> formats the number with N digits *after* the decimal point.

    This example prints the same two numbers using increasing precision
    so you can see how formatting affects the output.
    """
    clear_screen()

    # Two sample floating-point values
    x = 0.1
    y = 123.456789

    # Print using significant-digit formatting
    print("{:.1}  {:.1}".format(x, y))
    print("{:.2}  {:.2}".format(x, y))
    print("{:.3}  {:.3}".format(x, y))
    print("{:.4}  {:.4}".format(x, y))
    print("{:.5}  {:.5}".format(x, y))
    print("{:.6}  {:.6}".format(x, y))

    print()  # Blank line for readability

    # Print using fixed-decimal formatting
    print("{:.1f}  {:.1f}".format(x, y))
    print("{:.2f}  {:.2f}".format(x, y))
    print("{:.3f}  {:.3f}".format(x, y))
    print("{:.4f}  {:.4f}".format(x, y))
    print("{:.5f}  {:.5f}".format(x, y))
    print("{:.6f}  {:.6f}".format(x, y))


# ---------------------------------------------------------------
# Example 02: Floating-point formatting with width + precision
# ---------------------------------------------------------------
def ex_02():
    """
    Demonstrate floating-point formatting using width and precision.

    '{:10.3}'   -> total width 10, 3 significant digits.
    '{:10.3f}'  -> total width 10, 3 digits after the decimal.

    width formatting is useful for aligning columns of numbers.
    """
    clear_screen()

    x = 0.1
    y = 123.456789

    # Significant-digit formatting with width
    print("'{:10.1}'  '{:10.1}'".format(x, y))
    print("'{:10.2}'  '{:10.2}'".format(x, y))
    print("'{:10.3}'  '{:10.3}'".format(x, y))
    print("'{:10.4}'  '{:10.4}'".format(x, y))
    print("'{:10.5}'  '{:10.5}'".format(x, y))
    print("'{:10.6}'  '{:10.6}'".format(x, y))

    print()  # Blank line for readability

    # Fixed-decimal formatting with width
    print("'{:10.1f}'  '{:10.1f}'".format(x, y))
    print("'{:10.2f}'  '{:10.2f}'".format(x, y))
    print("'{:10.3f}'  '{:10.3f}'".format(x, y))
    print("'{:10.4f}'  '{:10.4f}'".format(x, y))
    print("'{:10.5f}'  '{:10.5f}'".format(x, y))
    print("'{:10.6f}'  '{:10.6f}'".format(x, y))


# ----------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Uncomment the example you want to run:
    # ex_01()
    ex_02()
