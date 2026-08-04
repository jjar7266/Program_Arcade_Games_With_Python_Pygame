"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 2: Create a custom calculator

calculate_miles_per_gallon.py
"""

# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=JK5ht5_m6Mk

# Calculate Miles Per Gallon
print("This program calculates mpg.")

# Get miles driven from the user
miles_driven = input("Enter miles driven:")

# Convert text entered to a floating point number
miles_driven = float(miles_driven)

# Get gallons used from the user
gallons_used = input("Enter gallons used:")

# Convert text entered to a floating point number
gallons_used = float(gallons_used)

# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)



