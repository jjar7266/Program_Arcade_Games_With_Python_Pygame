"""
Chapter 20 Worksheet
Program Arcade Games With Python and Pygame
Fourth Edition
Jose 'Joe' Ruiz

This file contains the worksheet questions and fully commented solutions.
"""

# Import modules
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)

def q7():
    clear_screen()

    # -----------------------------------------------------------
    # 7. Write a recursive function f(n) that takes in a value n
    #    and returns the value for f, given the definition below:
    #
    #       fₙ = 6                if n = 1
    #       fₙ = ½·fₙ₋₁ + 4       if n > 1
    #
    #    Then write a for loop that prints out the answers for
    #    values of n from 1 to 10. It should look like:
    #
    #    n= 1 , a= 6
    #    n= 2 , a= 7.0
    #    n= 3 , a= 7.5
    #    n= 4 , a= 7.75
    #    n= 5 , a= 7.875
    #    n= 6 , a= 7.9375
    #    n= 7 , a= 7.96875
    #    n= 8 , a= 7.984375
    #    n= 9 , a= 7.9921875
    #    n= 10 , a= 7.99609375
    #
    #    The function should not have any print statements inside it,
    #    nor a loop. The for loop that is written should be outside
    #    the function and call the function to get the results and
    #    print them.
    # ------------------------------------------------------------

    def f(n):
        # Base case
        if n == 1:
            return 6
        # Recursive case
        return 0.5 * f(n - 1) + 4

    for n in range(1, 11):
        a = f(n)
        print(f"n= {n}, a= {a}")


def q8():
    clear_screen()

    # ------------------------------------------------------------
    # 8. Write recursive code that will print out the first 10 terms
    #    of the sequence below:
    #
    #       fₙ = 1                if n = 1
    #       fₙ = 1                if n = 2
    #       fₙ = f(n‑1) + f(n‑2)  if n > 2
    #
    # ------------------------------------------------------------

    def f(n):
        # Base cases
        if n == 1 or n == 2:
            return 1
        # Recursive case
        return f(n - 1) + f(n - 2)

    # Print first 10 terms
    for n in range(1, 11):
        print(f"n= {n} , a= {f(n)}")




if __name__ == "__main__":
    # q7()    # <- run Question 7
    q8()    # <- run Question 8

