"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Annotating a graph

matplotlib_example_05.py
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
# Add an annotation to the graph
# -------------------------------------------------------------
# plt.annotate() places text at a specific point on the graph.
# 'xy' marks the point being annotated.
# 'xytext' sets where the annotation text will appear.
# 'arrowprops' defines the arrow style and connection behavior.
plt.annotate(
    'Here',                 # Text label
    xy=(2, 3),              # Point being annotated
    xycoords='data',        # Coordinates are in data units
    xytext=(-40, 20),       # Offset for the annotation text
    textcoords='offset points',
    arrowprops=dict(
        arrowstyle="->",    # Simple arrow
        connectionstyle="arc,angleA=0,armA=30,rad=10"
    ),
)

# -------------------------------------------------------------
# Create the line plot
# -------------------------------------------------------------
plt.plot(x, y)

# Label the axes
plt.ylabel('Element Value')
plt.xlabel('Element')

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
