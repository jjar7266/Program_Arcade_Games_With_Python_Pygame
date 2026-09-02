"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Using the numpy package to graph a function over
a range of values

matplotlib_example_09.py
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

# Label the axes
plt.ylabel('Element Value')
plt.xlabel('Element')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
