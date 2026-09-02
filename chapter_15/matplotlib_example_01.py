"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Line chart with four values.
The x-axis defaults to start at zero.

matplotlib_example_01.py
"""

# Import the Matplotlib plotting module
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Data to plot
# -------------------------------------------------------------
# A simple list of four values. Matplotlib will automatically
# use the index positions (0, 1, 2, 3) as the x-axis values.
y = [1, 3, 8, 4]

# -------------------------------------------------------------
# Create the line plot
# -------------------------------------------------------------
# plt.plot() draws a line graph using the y-values above.
plt.plot(y)

# Label the axes for clarity
plt.ylabel('Element Value')
plt.xlabel('Element Number')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
