"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

How to do a bar chart.

matplotlib_example_07.py
"""

# Import the Matplotlib plotting module
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Data to plot
# -------------------------------------------------------------
# x-values represent element positions (1 through 4)
x = [1, 2, 3, 4]

# y-values represent the corresponding element values
y = [1, 3, 8, 4]

# -------------------------------------------------------------
# Create the bar chart
# -------------------------------------------------------------
# plt.bar() draws vertical bars at each x position with heights y.
plt.bar(x, y)

# Label the axes
plt.ylabel('Element Value')
plt.xlabel('Element')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
