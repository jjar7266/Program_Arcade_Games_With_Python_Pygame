"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting - Printing Dollars and Cents

examplesC21_05.py
"""

# Import modules
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


# ------------------------------------------------------------------
# Example 01: Basic dollar formatting
# ------------------------------------------------------------------
def ex_01():
    """
    Demonstrate formatting dollars and cents using {:5.2f}.
    {:5.2f}  -> width 5, two digits after the decimal.
    This example prints cost, tax, and total for a single item.
    """
    clear_screen()

    cost1  = 3.07
    tax1   = cost1 * 0.06
    total1 = cost1 + tax1

    print("Cost:  ${0:5.2f}".format(cost1))
    print("Tax:    {0:5.2f}".format(tax1))
    print("-------------")
    print("Total:  ${0:5.2f}".format(total1))


# --------------------------------------------------------------
# Example 02: Multiple items + grand total
# --------------------------------------------------------------
def ex_02():
    """
    Print cost, tax, and total for two items, then compute a grand total.
    Uses {:5.2f} formatting for aligned dollar amounts.
    """
    clear_screen()

    # First item
    cost1  = 3.07
    tax1   = cost1 * 0.06
    total1 = cost1 + tax1

    print("Cost:  ${0:5.2f}".format(cost1) )
    print("Tax:    {0:5.2f}".format(tax1) )
    print("------------")
    print("Total: ${0:5.2f}".format(total1) )

    # Second item
    cost2  = 5.07
    tax2   = cost2 * 0.06
    total2 = cost2 + tax2

    print()
    print("Cost:  ${0:5.2f}".format(cost2) )
    print("Tax:    {0:5.2f}".format(tax2) )
    print("------------")
    print("Total: ${0:5.2f}".format(total2) )

    # Grand total
    print()
    grand_total = total1 + total2
    print("Grand total: ${0:5.2f}".format(grand_total) )


# ---------------------------------------------------------------
# Example 03: Using round() for tax calculations
# ---------------------------------------------------------------
def ex_03():
    """
    Same as Example 02, but uses round() to ensure tax values
    are rounded to exactly two decimal places before printing.
    This avoids floating-point precision issues.
    """
    clear_screen()

    # First item
    cost1 = 3.07
    tax1 = round(cost1 * 0.06, 2)
    total1 = cost1 + tax1

    print("Cost:  ${0:5.2f}".format(cost1) )
    print("Tax:    {0:5.2f}".format(tax1) )
    print("------------")
    print("Total: ${0:5.2f}".format(total1) )

    # Second item
    cost2 = 5.07
    tax2 = round(cost2 * 0.06,2)
    total2 = cost2 + tax2

    print()
    print("Cost:  ${0:5.2f}".format(cost2) )
    print("Tax:    {0:5.2f}".format(tax2) )
    print("------------")
    print("Total: ${0:5.2f}".format(total2) )

    # Grand total
    print()
    grand_total = total1 + total2
    print("Grand total: ${0:5.2f}".format(grand_total) )


# -----------------------------------------------------------
# Example 04: Demonstrate round() with positive/negative precision
# -----------------------------------------------------------
def ex_04():
    """
    Show how round() behaves with different precision values.
    round(x, 2)  -> round to 2 decimal places
    round(x, 1)  -> round to 1 decimal place
    round(x, 0)  -> round to nearest whole number
    round(x, -1) -> round to nearest 10
    round(x, -2) -> round to nearest 100
    """
    clear_screen()

    x = 1234.5678

    print(round(x, 2))   # 1234.57
    print(round(x, 1))   # 1234.6
    print(round(x, 0))   # 1235.0
    print(round(x, -1))  # 1230.0
    print(round(x, -2))  # 1200.0


# ----------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Uncomment the example you want to run:
    # ex_01()
    # ex_02()
    # ex_03()
    ex_04()


