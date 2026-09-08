"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting

examplesC21_03.py
"""
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


# ---------------------------------------------------------------
# Example 1: Print times without formatting
# ---------------------------------------------------------------
def ex_1():
    """
    Print every time from 1:00 to 12:59 using basic formatting.
    Hours range from 1-12
    Minutes range from 0-59.
    This version prints minutes without leading zeros.
    """
    clear_screen()

    # Loop through each hour
    for hours in range(1, 13):
        # Loop through each minute
        for minutes in range(0, 60):
            # Basic formatting: minutes appear as 0, 1, 2, ... 59
            print("Time {}:{}".format(hours, minutes))


# ----------------------------------------------------------------
# Example 2: Print times with zero-padded formatting
# ----------------------------------------------------------------
def ex_2():
    """
    Print every time from 1:00 to 12:59 using formatted output.
    {:02} ensures the value is at least two digits, padded with zeros.
    Example: 0 -> 00, 5 -> 05, 12 -> 12
    This creates clean, clock-style formatting.
    """
    clear_screen()

    for hours in range(1, 13):
        for minutes in range(0, 60):
            # Zero-pad both hours and minutes to 2 digits
            print("Time {:02}:{:02}".format(hours, minutes))


# ----------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Uncomment the example you want to run:
    # ex_1()
    ex_2()
