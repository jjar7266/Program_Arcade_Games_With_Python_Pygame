"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Create a pie chart

matplotlib_example_11.py
"""

# Import modules
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Labels for the pie chart
# -------------------------------------------------------------
labels = ['C', 'Java', 'Objective-C', 'C++', 'C#', 'PHP', 'Python']

# -------------------------------------------------------------
# Sizes for each slice (percent values)
# -------------------------------------------------------------
sizes = [17, 14, 9, 6, 5, 3, 2.5]

# -------------------------------------------------------------
# Colors for each slice
# -------------------------------------------------------------
colors = [
    'yellowgreen', 'gold', 'lightskyblue',
    'lightcoral', 'darkcyan', 'darkseagreen', 'rosybrown'
]

# -------------------------------------------------------------
# Explode settings (pull a slice outward)
# -------------------------------------------------------------
explode = (0, 0.0, 0, 0, 0, 0, 0.2)

# -------------------------------------------------------------
# Draw pie chart
# -------------------------------------------------------------
# axis('equal') ensures the pie is drawn as a circle.
plt.axis('equal')

plt.pie(
    sizes,
    explode=explode,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',   # Show percentages
    shadow=True,         # Add drop shadow
    startangle=90        # Rotate chart for nicer orientation
)

# -------------------------------------------------------------
# Display the plot window
# -------------------------------------------------------------
plt.show()
