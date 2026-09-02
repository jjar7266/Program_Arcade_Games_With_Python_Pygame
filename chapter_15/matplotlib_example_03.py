"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Line chart with two data sets.
The x-axis defaults to start at zero, but here we provide our own.

matplotlib_example_03.py
"""

# Import the Matplotlib plotting module
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Data to plot
# -------------------------------------------------------------
# x-values represent element positions (1 through 4)
x  = [1, 2, 3, 4]

# First data series
y1 = [1, 3, 8, 4]

# Second data series
y2 = [2, 2, 3, 3]

# -------------------------------------------------------------
# Create the line plots
# -------------------------------------------------------------
# Each call to plt.plot() adds another line to the same axes.
plt.plot(x, y1)
plt.plot(x, y2)

# Label the axes for clarity
plt.ylabel('Element Value')
plt.xlabel('Element Number')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
