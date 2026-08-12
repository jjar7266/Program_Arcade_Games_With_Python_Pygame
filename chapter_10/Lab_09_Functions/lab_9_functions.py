"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 10: Functions

lab_9_functions.py
"""

# Import modules
import random

# ------------------------------------------------------------------
# Lab 9: Functions
# Part 1. Create a function called min3 that returns
# the smallest of three values using if/elif/else.
# ------------------------------------------------------------------

def min3(a, b, c):
    """
    This function receives three values: a, b, and c.
    Our job is to compare them and return the smallest one.
    We are NOT allowed to use Python's built-in min() function,
    because the purpose of this lab is to practice writing
    our own comparison logic using if/elif/else.

    The plan:
    1. First check if 'a' is less than or equal to BOTH 'b' and 'c'.
       If true, then 'a' must be the smallest.

    2. If 'a' is NOT the smallest, then check if 'b' is less than
       or equal to BOTH 'a' and 'c'.
       If true, then 'b' is the smallest.

    3. If neither 'a' nor 'b' is the smallest, then the ONLY
       remaining possibility is 'c'. So we return 'c'.

    This logic works for:
      - integers
      - floats
      - negative numbers
      - strings (alphabetical comparison)
    """

    # Check if 'a' is the smallest.
    # We use <= so ties still count as "smallest".
    if a <= b and a <= c:
        return a

    # If 'a' was not the smallest, check if 'b' is the smallest.
    elif b <= a and b <= c:
        return b

    # If neither 'a' nor 'b' is smallest, then 'c' must be smallest.
    else:
        return c

# -------------------------------------------------------------
# Required test cases from the lab instructions.
# These MUST remain in the program so the instructor can verify
# that the function works correctly.
# -------------------------------------------------------------

# uncomment to run print statement

#print(min3(4, 7, 5))        # Expected: 4
#print(min3(4, 5, 5))        # Expected: 4
#print(min3(4, 4, 4))        # Expected: 4
#print(min3(-2, -6, -100))   # Expected: -100
#print(min3("Z", "B", "A"))  # Expected: A


# ---------------------------------------------------------------
# Lab 9: Functions
# Part 2: Create a function called box that prints a box
# made of '*' characters using a given height and width.
# ---------------------------------------------------------------

def box(height, width):
    """
    This function prints a solid box made of '*' characters.
    The box has 'height' rows, and each row is 'width' stars wide.

    Example:
    box(3, 5) prints:

        *****
        *****
        *****

    The plan:
    1. Use a loop to repeat something 'height' times.
    2. Inside the loop, print one row of stars.
       We create a row by multiplying "*" by the width.
    """

    # Loop 'height' times to print each row of the box
    for i in range(height):
        # Print one row of 'width' stars
        print("*" * width)


# ---------------------------------------------------------------
# Part 2 output
# uncomment to run
# ---------------------------------------------------------------
#print("--- Part 2: Box Function ---")

# Required test cases from the lab instructions

#box(7, 5)
#print()

#box(3, 2)
#print()

#box(3, 10)


# ----------------------------------------------------------------
# Lab 9: Functions
# Part 3: Create a function called find that searches a list
# for a given key value and prints the index of each match.
# ----------------------------------------------------------------

def find(my_list, key):
    """
    This function searches through a list of numbers and prints
    the index (position) of every occurrence of the value 'key'.

    The plan:
    1. Use a for-loop with an index variable.
       This is the Chapter 8 pattern: range(len(my_list)).

    2. For each index 'i', look at my_list[i].

    3. If the value equals the key, print the position.

    Important:
      - We print the index, not the value.
      - If the key appears multiple times, we print multiple lines.
      - If the key never appears, we print nothing.
    """

    # Loop through the list using an index
    for i in range(len(my_list)):
        # Get the current element
        value = my_list[i]

        # Check if it matches the key
        if value == key:
            print(f"Found {key} at position {i}")

# -------------------------------------------------------------------
# Part 3 output
# uncomment to run
# -------------------------------------------------------------------
#print("--- Part 3: Find Function ---")

# Required test cases from the lab instructions

#my_list = [
#    36, 31, 79, 96, 36,
#    91, 77, 33, 19, 3,
#    34, 12, 70, 12, 54,
#    98, 86, 11, 17, 17
#]

#find(my_list, 12)
#find(my_list, 91)
#find(my_list, 80)


# ---------------------------------------------------------------------
# Part 4: Function 1 - Create_list
# ---------------------------------------------------------------------
def create_list(size):
    """
    This function creates and returns a list containing 'size'
    random integers between 1 and 6.

    The plan:
    1. Start with an empty list.
    2. Loop 'size' times.
    3. Each time, generate a random number from 1 to 6.
    4. Append it to the list.
    5. Return the completed list.
    """

    my_list = []

    for i in range(size):
        number = random.randint(1, 6)
        my_list.append(number)

    return my_list

# Test code required by the lab
# uncomment to run
#print("--- Testing create_list ---")
#my_list = create_list(5)
#print(my_list)     # Should print 5 random numbers from 1-6
#print()


# -----------------------------------------------------------------
# Part 4: Function 2 - count_list
# -----------------------------------------------------------------
def count_list(my_list, key):
    """
    This function counts how many times 'key' appears in 'my_list'.

    The plan:
    1. Start a counter at 0.
    2. Loop through each element in the list.
    3. If the element equals the key, increment the counter.
    4. Return the final count.
    """

    count = 0

    for value in my_list:
        if value == key:
            count += 1

    return count

# Test code required by the lab
# uncomment to run
#print("--- Testing count_list ---")
#count = count_list([1, 2, 3, 3, 3, 4, 2, 1], 3)
#print(count)     # Expected: 3
#print()


# -----------------------------------------------------------------------
# Part 4: Function 3 - average_list
# -----------------------------------------------------------------------
def average_list(my_list):
    """
    This function returns the average of all numbers in 'my_list'.

    The plan:
    1. Add up all numbers using a loop.
    2. Count how many numbers are in the list.
    3. Divide total by count.
    4. Return the average.
    """

    total = 0

    for value in my_list:
        total += value

    count = len(my_list)

    # Avoid division by zero (not needed here, but good practice)
    if count == 0:
        return 0

    return total / count

# Test code required by the lab
# uncomment to run
#print("--- Testing average_list ---")
#avg = average_list([1, 2, 3])
#print(avg)   # Expected: 2
#print()


# ---------------------------------------------------------------------
# Part 4: Main Program
# ---------------------------------------------------------------------

def main():
    print("--- Part 4: Main Program ---")

    # Step 1: Create a list of 10,000 random numbers from 1-6
    big_list = create_list(10000)

    # Step 2: Print the count of each number 1 through 6
    print("Counts of numbers 1 through 6:")
    for n in range(1, 7):
        print(f"{n}: {count_list(big_list, n)}")

    # Step 3: Print the average of all 10,000 numbers
    average = average_list(big_list)
    print("\nAverage of all 10,000 numbers: ", average)

# Only run main() if this file is executed directly
if __name__ == "__main__":
    main()

