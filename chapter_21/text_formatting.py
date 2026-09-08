"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting

text_formatting.py
"""
# Import modules
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


def formatting_reference():
    clear_screen()

    # ------------------------------------------------------------
    # 1. Demonstrate Python numeric formatting examples
    # ------------------------------------------------------------

    print(f"{'Number':<15}{'Format':<15}{'Output':<15}{'Description'}")
    print("-" * 75)

    print(f"{3.1415926:<15}{'{:.2f}':<15}{format(3.1415926, '.2f'):<15}2 decimal places")
    print(f"{3.1415926:<15}{'{:+.2f}':<15}{format(3.1415926, '+.2f'):<15}2 decimal places with sign")
    print(f"{-1:<15}{'{:+.2f}':<15}{format(-1, '+.2f'):<15}2 decimal places with sign")
    print(f"{3.1415926:<15}{'{:.0f}':<15}{format(3.1415926, '.0f'):<15}No decimal places (will round)")
    print(f"{5:<15}{'{:0>2d}':<15}{format(5, '0>2d'):<15}Pad with zeros on the left")
    print(f"{1000000:<15}{'{:,}':<15}{format(1000000, ','):<15}Number format with comma separator")
    print(f"{0.25:<15}{'{:.2%}':<15}{format(0.25, '.2%'):<15}Format percentage")
    print(f"{1000000000:<15}{'{:.2e}':<15}{format(1000000000, '.2e'):<15}Exponent notation")
    print(f"{11:<15}{'{:>10d}':<15}{format(11, '>10d'):<15}Right aligned")
    print(f"{11:<15}{'{:<10d}':<15}{format(11, '<10d'):<15}Left aligned")
    print(f"{11:<15}{'{:^10d}':<15}{format(11, '^10d'):<15}Center aligned")


if __name__ == "__main__":
    formatting_reference()
