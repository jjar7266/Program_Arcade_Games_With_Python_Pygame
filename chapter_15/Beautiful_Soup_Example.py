"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 15: Libraries and Modules

Example showing how to read in from a web page

Beautiful_Soup_Example.py
"""

from bs4 import BeautifulSoup
import urllib.request

# -------------------------------------------------------------
# Target URL
# -------------------------------------------------------------
# This page contains a standard HTML table that BeautifulSoup
# can parse without any JavaScript processing.
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

# -------------------------------------------------------------
# Build the request
# -------------------------------------------------------------
# Some websites reject requests that do not include a User-Agent.
# Adding one makes the request look like it came from a browser.
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

# -------------------------------------------------------------
# Fetch and parse the page
# -------------------------------------------------------------
# urlopen() retrieves the raw HTML.
# BeautifulSoup loads and parses that HTML into a searchable tree.
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page.read(), "html.parser")

# -------------------------------------------------------------
# Locate the first table on the page
# -------------------------------------------------------------
# Wikipedia pages often contain multiple tables, but for this
# example we simply grab the first one.
table = soup.find("table")

# -------------------------------------------------------------
# Ensure the table exists and contains a <tbody> section
# -------------------------------------------------------------
if table and table.tbody:
    rank = table.tbody

    # ---------------------------------------------------------
    # Extract all table rows
    # ---------------------------------------------------------
    rows = rank.find_all("tr")

    # ---------------------------------------------------------
    # Loop through each row and print its cells
    # ---------------------------------------------------------
    for row in rows:

        # Each row may contain <td> (data cells) or <th> (header cells)
        cells = row.find_all(["td", "th"])

        # Print the text content of each cell
        for cell in cells:
            print(cell.text, end=", ")

        # Blank line between rows for readability
        print()

else:
    print("No table found on this page.")
