"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

This shows how to set line style and markers.

matplotlib_example_06.py
"""

# Import the Matplotlib plotting module
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Data to plot
# -------------------------------------------------------------
x  = [1, 2, 3, 4]
y1 = [1, 3, 8, 4]
y2 = [2, 2, 3, 3]

# -------------------------------------------------------------
# Line style, color, and marker notes
# -------------------------------------------------------------
# Format strings follow this pattern:
#   "<line style><color><marker>"
#
# Line styles:
#   '-'   solid line
#   '--'  dashed line
#   '-.'  dash-dot line
#   ':'   dotted line
#
# Colors (single-letter shortcuts):
#   r = red, g = green, b = blue, c = cyan,
#   m = magenta, y = yellow, k = black, w = white
#
# Marker shapes:
#   o = circle, ^ = triangle-up, s = square, * = star, etc.

# -------------------------------------------------------------
# Create the line plots with style strings
# -------------------------------------------------------------
# '-ro'  → solid red line with circle markers
# '--g^' → dashed green line with triangle-up markers
plt.plot(x, y1, '-ro')
plt.plot(x, y2, '--g^')

# Label the axes
plt.ylabel('Element Value')
plt.xlabel('Element')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
