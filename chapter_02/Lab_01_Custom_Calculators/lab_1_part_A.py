"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Lab 1: Custom Calculators

lab_1_part_A.py

Create a program that asks the user for a temperature in Fahrenheit, and then
prints the temperature in Celsius.

Sample run:

Enter temperature in Fahrenheit: 32
The temperature in Celsius: 0.0

Sample run:

Enter temperature in Fahrenheit: 72
The temperature in Celsius: 22.2222222222
"""

f_temp = (float(input("Enter a number in Fahrenheit: ")))

c_temp = (f_temp - 32) * 5 / 9

print(f"The temperature in Celsius: {c_temp:.1f}")



