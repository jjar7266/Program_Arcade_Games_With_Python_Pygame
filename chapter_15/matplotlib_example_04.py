"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Line chart with two data sets and a custom legend.

matplotlib_example_04.py
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
# The 'label' parameter assigns a name used in the legend.
plt.plot(x, y1, label="Series 1")
plt.plot(x, y2, label="Series 2")

# -------------------------------------------------------------
# Legend customization
# -------------------------------------------------------------
# Create the legend and store the returned Legend object.
legend = plt.legend(
    loc='upper center',   # Position the legend above the plot
    shadow=True,          # Add a drop shadow
    fontsize='x-large'    # Increase text size
)

# Customize the legend's background color
legend.get_frame().set_facecolor('#00FFCC')

# -------------------------------------------------------------
# Label the axes
# -------------------------------------------------------------
plt.ylabel('Element Value')
plt.xlabel('Element Number')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
