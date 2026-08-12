"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Main Functions and Globals

examples.py

For each of the examples below, think about what would print.
Check to see if you are right. If you didn't guess correctly,
spend to the time to understand why.
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# ---------------------------------
# Example 1
# ---------------------------------
def example1():
    def a():
        print("A")

    def b():
        print("B")

    def c():
        print("C")

    a()

# --------------------------------
# Example 2
# --------------------------------
def example2():
    def a():
        b()
        print("A")

    def b():
        c()
        print("B")

    def c():
        print("C")

    a()

# ---------------------------------
# Example 3
# ---------------------------------
def example3():
    def a():
        print("A")
        b()

    def b():
        print("B")
        c()

    def c():
        print("C")

    a()

# ---------------------------------
# Example 4
# ---------------------------------
def example4():
    def a():
        print("A start")
        b()
        print("A end")

    def b():
        print("B start")
        c()
        print("B end")

    def c():
        print("C start and end")

    a()

# ----------------------------------
# Example 5
# ----------------------------------
def example5():
    def a(x):
        print("A start, x =", x)
        b(x + 1)
        print("A end, x =", x)

    def b(x):
        print("B start, x =", x)
        c(x + 1)
        print("B end, x =", x)

    def c(x):
        print("C start and end, x =", x)

    a(5)

# -----------------------------------
# Example 6
# -----------------------------------
def example6():
    def a(x):
        x = x + 1

    x = 3
    a(x)

    print(x)

# -------------------------------------
# Example 7
# -------------------------------------
def example7():
    def a(x):
        x = x + 1
        return x

    x = 3
    a(x)

    print(x)

# --------------------------------------
# Example 8
# --------------------------------------
def example8():
    def a(x):
        x = x + 1
        return x

    x = 3
    x = a(x)

    print(x)

# ----------------------------------------
# Example 9
# ----------------------------------------
def example9():
    def a(x, y):
        x = x + 1
        y = y + 1
        print(x, y)

    x = 10
    y = 20
    a(y, x)

# -------------------------------------------
# Example 10
# -------------------------------------------
def example10():
    def a(x, y):
        x = x + 1
        y = y + 1
        return x
        return y

    x = 10
    y = 20
    z = a(x, y)

    print(z)

# --------------------------------------------
# Example 11
# --------------------------------------------
def example11():
    def a(x, y):
        x = x + 1
        y = y + 1
        return x, y

    x = 10
    y = 20
    z = a(x, y)

    print(z)

# ---------------------------------------------
# Example 12
# ---------------------------------------------
def example12():
    def a(x, y):
        x = x + 1
        y = y + 1
        return x, y

    x = 10
    y = 20
    x2, y2 = a(x, y)  # Most computer languages don't support this

    print(x2)
    print(y2)

# -----------------------------------------------
# Example 13
# -----------------------------------------------
def example13():
    def a(my_data):
        print("function a, my_data = ", my_data)
        my_data = 20
        print("function a, my_data = ", my_data)

    my_data = 10

    print("global scope, my_data =", my_data)
    a(my_data)
    print("global scope, my_data =", my_data)

# -------------------------------------------------
# Example 14
# -------------------------------------------------
def example14():
    def a(my_list):
        print("function a, list = ", my_list)
        my_list = [10, 20, 30]
        print("function a, list = ", my_list)

    my_list = [5, 2, 4]

    print("global scope, list =", my_list)
    a(my_list)
    print("global scope, list =", my_list)

# ----------------------------------------------------
# Example 15
# ----------------------------------------------------
# New concept!
def example15():
    def a(my_list):
        print("function a, list = ", my_list)
        my_list[0] = 1000
        print("function a, list = ", my_list)

    my_list = [5, 2, 4]

    print("global scope, list =", my_list)
    a(my_list)
    print("global scope, list =", my_list)


if __name__ == "__main__":

    # uncomment to to run the example

    #example1()
    #example2()
    #example3()
    #example4()
    #example5()
    #example6()
    #example7()
    #example8()
    #example9()
    #example10()
    #example11()
    #example12()
    #example13()
    #example14()
    example15()
