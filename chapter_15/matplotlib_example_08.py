"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

How to add x axis value labels

matplotlib_example_08.py
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
# Create the line plot
# -------------------------------------------------------------
plt.plot(x, y)

# -------------------------------------------------------------
# Custom x-axis labels
# -------------------------------------------------------------
# plt.xticks() replaces the numeric x-values with text labels.
# The first argument is the list of positions.
# The second argument is the list of labels to display.
labels = ['Frogs', 'Hogs', 'Bogs', 'Slogs']
plt.xticks(x, labels)

# Label the axes
plt.ylabel('Element Value')
plt.xlabel('Element')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
