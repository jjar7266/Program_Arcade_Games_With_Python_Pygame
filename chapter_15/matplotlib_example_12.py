"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Create a candlestick chart for a stock
Modernized version using yfinance + Matplotlib
"""

# ------------------------------------------------------------
# Import required modules
# ------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd  # ✅ Added: needed for MultiIndex detection

# Date formatting utilities from Matplotlib
from matplotlib.dates import (
    DateFormatter,
    WeekdayLocator,
    DayLocator,
    MONDAY,
    date2num
)

# Modern Yahoo Finance downloader
import yfinance as yf

# Modern Matplotlib-compatible candlestick function
from mplfinance.original_flavor import candlestick_ohlc


# ------------------------------------------------------------
# Define the date range for the stock data
# ------------------------------------------------------------
start_date = "2014-10-13"
end_date = "2014-11-13"


# ------------------------------------------------------------
# Download historical OHLC data for Apple (AAPL)
# ------------------------------------------------------------
data = yf.download("AAPL", start=start_date, end=end_date)

print("Rows in data:", len(data))

if data.empty:
    raise SystemExit("No stock data returned. Check ticker or date range.")


# ------------------------------------------------------------
# Flatten multi-level columns if present
# ------------------------------------------------------------
# yfinance sometimes returns columns like ('Open', 'AAPL')
# This ensures we have simple column names: 'Open', 'High', 'Low', 'Close'
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)


# ------------------------------------------------------------
# Convert DataFrame to list of tuples for candlestick_ohlc
# ------------------------------------------------------------
ohlc = []
for date, row in data.iterrows():
    ohlc.append((
        date2num(date),          # Convert datetime → Matplotlib float
        float(row["Open"]),      # Convert to float
        float(row["High"]),
        float(row["Low"]),
        float(row["Close"])
    ))

print("Rows in ohlc:", len(ohlc))


# ------------------------------------------------------------
# Set up Matplotlib figure and axes
# ------------------------------------------------------------
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)  # Extra space for rotated date labels


# ------------------------------------------------------------
# Configure tick marks (same as original book)
# ------------------------------------------------------------
mondays = WeekdayLocator(MONDAY)
ax.xaxis.set_major_locator(mondays)

alldays = DayLocator()
ax.xaxis.set_minor_locator(alldays)

weekFormatter = DateFormatter('%b %d')  # Example: Jan 12
ax.xaxis.set_major_formatter(weekFormatter)
ax.xaxis_date()


# ------------------------------------------------------------
# Draw the candlestick chart
# ------------------------------------------------------------
candlestick_ohlc(ax, ohlc, width=0.6, colorup='g', colordown='r')


# ------------------------------------------------------------
# Final formatting
# ------------------------------------------------------------
ax.autoscale_view()

# Rotate date labels for readability
plt.setp(plt.gca().get_xticklabels(),
         rotation=45,
         horizontalalignment='right')

# Optional: match instructor’s gray background
fig.patch.set_facecolor('lightgray')

# Display the chart
plt.show()
