"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Function Parameters

test_02.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=b8qQFifS2G0


# --------------------------------------------------------------
# NOTE ABOUT BOOK VS VIDEO VERSION
# --------------------------------------------------------------
# The BOOK uses the correct mathematical formula for the VOLUME
# of a cylinder:
#
#       V = π * r^2 * h
#
# The VIDEO version accidentally switches to the SURFACE AREA
# formula:
#
#       A = 2 * π * r * (r + h)
#
# The video also uses 'return' instead of 'print', because the
# instructor is demonstrating how functions can return values.
#
# IMPORTANT:
# We are following the BOOK version here, because it uses the
# correct formula for actual cylinder volume.
# --------------------------------------------------------------


# Function that prints the volume of a cylinder
def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height

    print("The volume is", volume)


volume_cylinder(12, 3)

