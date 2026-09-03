"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 16: Searching

reading_file_example.py
-------------------------------------------------------------------
This small script demonstates how to read data from a text file and
load it into a Python list using the modern 'with open(...)' pattern.

Even though the code is short, it performs several essential tasks:

1. Opens a text file safely
2. Reads the file line-by-line
3. Removes newline characters and extra whitespaces
4. Stores each cleaned line into a Python list
5. Prints each item as it is read
6. Automatically closes the file when finished

The 'with open(...)' structure is preferred because:
- It automatically closes the file
- It prevents resource leaks
- It is cleaner and more Pythonic
- It avoids errors if something goes wrong while reading

"""

# ---------------------------------------------------------------------
# STEP 1: Open the file using 'with open(...)'
# ---------------------------------------------------------------------
# The 'with' statement creates a temporary file-handling block.
# When the block ends, Python automatically closes the file.
#
# 'open("super_villains.txt")' opens the file in read mode ('r')
# which is the default mode when no second argument is provided.
#
# The variable 'file' becomes a file object we can iterate over.
with open("super_villains.txt") as file:

    # -----------------------------------------------------------------
    # STEP 2: Create an empty list to store all villain names
    # -----------------------------------------------------------------
    name_list = []

    # -----------------------------------------------------------------
    # STEP 3: Read the file line-by-line
    # -----------------------------------------------------------------
    # Looping over 'file' gives each line in order.
    # Example raw line: "Dr. Evil\n"
    for line in file:

        # -------------------------------------------------------------
        # STEP 3A: Clean the line
        # -------------------------------------------------------------
        # strip() removes:
        # - newline characters (\n)
        # - leading/trailing spaces
        #
        # After strip(), "Dr. Evil\n" becomes "Dr. Evil"
        clean_name = line.strip()

        # -------------------------------------------------------------
        # STEP 3B: Store the cleaned name in our list
        # -------------------------------------------------------------
        name_list.append(clean_name)

        # -------------------------------------------------------------
        # STEP 3C
        # -------------------------------------------------------------
        print(clean_name)

# ---------------------------------------------------------------------
# STEP 4: File is automatically closed here
# ---------------------------------------------------------------------
# No need to call file.close()
# The 'with' block handles cleanup automatically.

