"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Function Parameters

test.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=b8qQFifS2G0

# --------------------------------------------------------------
# NOTE ABOUT BOOK VS VIDEO VERSION
# --------------------------------------------------------------
# The BOOK uses the correct formula for the VOLUME of a sphere:
#       V = (4 / 3) * π * r^3
#
# The VIDEO version uses the SURFACE AREA formula instead:
#       A = 4 * π * r^2
#
# The video also hardcodes the radius (3) and omits parameters,
# because the instructor is demonstrating basic function syntax.
#
# We are following the BOOK version here, since it is both
# mathematically correct and reusable for any radius value.
# --------------------------------------------------------------

# Function that prints the volume of a sphere
def volume_sphere(radius):
    pi = 3.141592653589
    volume = (4 / 3) * pi * radius ** 3
    print("The volume is", volume)
    #return volume

#for i in range(20):
#    v = volume_sphere(i)
#    print(v)

volume_sphere(22)
