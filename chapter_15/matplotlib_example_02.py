"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Line chart with four values.
The x-axis defaults to start at zero, but here we provide our own.

matplotlib_example_02.py
"""

# Import the Matplotlib plotting module
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Data to plot
# -------------------------------------------------------------
# x-values represent element positions (1 through 4)
# y-values represent the corresponding element values
x = [1, 2, 3, 4]
y = [1, 3, 8, 4]

# -------------------------------------------------------------
# Create the line plot
# -------------------------------------------------------------
# plt.plot(x, y) draws a line graph using the provided x and y lists.
plt.plot(x, y)

# Label the axes for clarity
plt.ylabel('Element Value')
plt.xlabel('Element Number')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
