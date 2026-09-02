"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Using 'fill' to fill in a graph

matplotlib_example_10.py
"""

# Import modules
import numpy
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Generate x-values
# -------------------------------------------------------------
# numpy.arange(start, stop, step) creates a sequence of values.
# Here we generate values from 0.0 up to (but not including) 2.0
# in increments of 0.001. This gives a smooth curve.
x = numpy.arange(0.0, 2.0, 0.001)

# -------------------------------------------------------------
# Compute y-values
# -------------------------------------------------------------
# y = sin(2πx) produces a standard sine wave over the interval.
y = numpy.sin(2 * numpy.pi * x)

# -------------------------------------------------------------
# Plot the function
# -------------------------------------------------------------
plt.plot(x, y)

# -------------------------------------------------------------
# Fill the area under the curve
# -------------------------------------------------------------
# 'b' means blue. 'alpha' controls transparency (0.0 = invisible,
# 1.0 = fully opaque). This creates a shaded region under the line.
plt.fill(x, y, 'b', alpha=0.3)

# Label the axes
plt.ylabel('Element Value')
plt.xlabel('Element')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
