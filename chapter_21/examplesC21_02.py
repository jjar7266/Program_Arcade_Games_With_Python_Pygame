"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting

examplesC21_02.py
"""
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


# ------------------------------------------------------------------
# Example 1: Basic printing without formatting
# ------------------------------------------------------------------
def ex_1():
    """
    Print fruit names and their calorie counts using basic print().
    No alignment or formatting is applied here.
    """
    clear_screen()

    # Lists of fruit names and their corresponding calorie values
    my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
    my_calories = [4, 300, 70, 30]

    # Loop through each index and print the values directly
    for i in range(4):
        print(my_fruit[i], "are", my_calories[i], "calories.")


# ---------------------------------------------------------------------
# Example 2: Width formatting using format()
# ---------------------------------------------------------------------
def ex_2():
    """
    Print fruit names and calories using width formatting.
    {:7} ensures the fruit name takes up at least 7 characters.
    {:3} ensures the calorie number takes up at least 3 characters.
    This creates aligned columns.
    """
    clear_screen()

    my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
    my_calories = [4, 300, 70, 30]

    for i in range(4):
        print("{:7} are {:3} calories.".format(my_fruit[i], my_calories[i]))


# -------------------------------------------------------------------
# Example 3: Left and right alignment
# -------------------------------------------------------------------
def ex_3():
    """
    Demonstrate left and right alignment using format().
    {:>7}  -> right-align the fruit name within 7 spaces.
    {:<3}  -> left-align the calorie number within 3 spaces.
    This shows how alignment affects column layout.
    """
    clear_screen()

    my_fruit = ["Apples", "Oranges", "Grapes", "Pears"]
    my_calories = [4, 300, 70, 30]

    for i in range(4):
        print("{:>7} are {:<3} calories.".format(my_fruit[i], my_calories[i]))


# ------------------------------------------------------------------
# Entry point
# ------------------------------------------------------------------

if __name__ == "__main__":
    # Uncomment the example you want to run:
    # ex_1()
    # ex_2()
    ex_3()

