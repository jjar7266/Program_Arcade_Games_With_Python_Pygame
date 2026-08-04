"""
Program Arcade Games With Python and Pygame
Fourth Edition
Author: Dr. Paul Vincent Craven

coded along by: Jose 'Joe' Ruiz

Lab 1: Custom Calculators

lab_1_part_B.py

Create a new program that will ask the user for the information needed
to find the area of a trapezoid, and then print the area. The formula
for the area of a trapezoid is:

A = 1/2 (x1 + x2)h

Sample run:

Area of a trapezoid
Enter the height of the trapezoid: 5
Enter the length of the bottom base: 10
Enter the length of the top base: 7
The area is: 42.5
"""

height = (float(input("Enter the height of the trapezoid: ")))

base_a = (float(input("Enter the length of the bottom base: ")))

base_b = (float(input("Enter the length of the top base: ")))

area = ((base_a + base_b) / 2) * height

print(f"The area is: {area:.2f}")
