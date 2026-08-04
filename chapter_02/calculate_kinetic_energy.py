"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 2: Create a custom calculator

calculate_kinetic_energy.py
"""

# Sample Python/Pygame Programs
# http://programarcadegames.com/


# Calculate Kinetic Energy

print("This program calculates the kinetic energy of a moving object.")

m_string = input("Enter the object's mass in kilograms: ")
m = float(m_string)

v_string = input("Enter the object's speed in meters per second: ")
v = float(v_string)

e = 0.5 * m * v * v
print(f"The object has {e} joules of energy.")  # f string not used in the book

