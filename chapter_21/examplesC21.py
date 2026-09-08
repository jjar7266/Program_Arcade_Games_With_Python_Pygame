"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting

examplesC21.py
"""
# import modules
import random
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


def ex_1():
    clear_screen()
    for i in range(10):
        x = random.randrange(20)
        print(x)


def ex_2():
    clear_screen()
    for i in range(10):
        x = random.randrange(20)
        print("{}".format(x))


def ex_3():
    clear_screen()
    for i in range(10):
        x = random.randrange(20)
        print("{:2}".format(x))


def ex_4():
    clear_screen()
    for i in range(10):
        x = random.randrange(100000)
        print("{:6}".format(x))


def ex_5():
    clear_screen()
    for i in range(10):
        x = random.randrange(100000)
        print("{:6,}".format(x))


def ex_6():
    clear_screen()
    x = 5
    y = 66
    z = 777
    print("A - '{}' B - '{}' C - '{}'".format(x, y, z))
    print("\nC - '{2}' A - '{0}' B - '{1}' C again - '{2}'".format(x, y, z))
    print("\nC - '{2:4}' A - '{0:4}' B - '{1:4}' C again - '{2:4}'".format(x, y, z))


if __name__ == "__main__":
    # ex_1()
    # ex_2()
    # ex_3()
    ex_4()
    # ex_5()
    # ex_6()




