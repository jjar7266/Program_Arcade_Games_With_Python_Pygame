"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Example using the third‑party library OpenPyXL to create
and populate an Excel worksheet.

OpenPyXL_Example.py
"""

# Import the OpenPyXL Workbook class.
# This is a third‑party library, so it must be installed in the venv.
from openpyxl import Workbook

# Standard library import for generating random numbers.
import random

# Create a new Excel workbook object.
wb = Workbook()

# Get the active worksheet. OpenPyXL creates one by default.
ws = wb.active

# Assign a value directly to a specific cell.
ws["A1"] = "This is a test"

# Append 200 rows of random numbers.
# Each append call adds a new row to the worksheet.
for i in range(200):
    ws.append([random.randrange(1000)])

# Save the workbook to disk.
wb.save("Sample.xlsx")
