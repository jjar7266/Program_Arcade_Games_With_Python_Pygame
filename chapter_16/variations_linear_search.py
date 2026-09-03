"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 16: Searching

variations_linear_search.py

This file demonstrates several variations of the linear search algorithm.
Instead of searching simple values, we search through a list of objects
(Alien instances) and check whether they match a specific property.

Dr. Paul Vincent Craven uses this example to show how linear search can be
adapted to answer different questions:
    - Does at least one item match?
    - Do all items match?
    - Which items match?
    - Build a new list of matching items.

These patterns appear constantly in game development.
    - filtering sprites
    - selecting enemies in range
    - checking collisions
    - validating inventory items
    - scanning tile maps
"""
# ---------------------------------------------------------------
# Alien class
# ---------------------------------------------------------------

class Alien:
    """
    Simple class representing an alien with a color and weight.
    This gives us an object type to search through instead of
    plain strings or numbers.
    """
    def __init__(self, color, weight):
        """
        Constructor: store the alien's color and weight.
        """
        self.color = color
        self.weight = weight

# -----------------------------------------------------------------
# Predicate function: does this alien have the property?
# -----------------------------------------------------------------

def has_property(my_alien):
    """
    Predicate function used by all search variations.

    Purpose:
        Determine whether a given alien matches the desired property.
        In this example, the property is: "Is the alien green?"

    Why this matters:
        Linear search often relies on a predicate function to decide
        whether an item matches the condition being searched for.
    """
    return my_alien.color.upper() == "GREEN"


# ----------------------------------------------------------------
# Variation 1: Sentinel-style linear search (while loop)
# ----------------------------------------------------------------

def check_if_one_item_has_property_v1(my_list):
    """
    Return True if at least one item in the list matches the property.

    This version uses a classic sentinel-style while loop:
        - Walk through the list index-by-index.
        - Stop early as soon as matching item is found.
        - If the loop finishes without finding a match, return False.

    This is the "traditional" linear search pattern.
    """
    i = 0

    # Continue looping while:
    #  - we haven't reached the end of the list
    #  - AND the current item does NOT have the property
    while i < len(my_list) and not has_property(my_list[i]):
        i += 1

    # If i is still within the list, we found a match.
    return i < len(my_list)


# -------------------------------------------------------------------
# Variation 2: Pythonic early-return search (for loop)
# -------------------------------------------------------------------

def check_if_one_item_has_property_v2(my_list):
    """
    Return True if at least one item matches the property.

    This version uses a simple for-loop with early return.
    It is functionally identical to V1 but cleaner and more readable.

    This is the modern Python way to express:
        "Does any item in this list match the condition?"
    """
    for item in my_list:
        if has_property(item):
            return True
    return False


# --------------------------------------------------------------------
# Variation 3: Check if ALL items match the property
# --------------------------------------------------------------------

def check_if_all_items_have_property(my_list):
    """
    Return True only if EVERY item in the list matches the property.

    This flips the logic:
        - Instead of checking for at least one match,
          we check for any item that does NOT match.
        - If we find a non-matching item, return False immediately.
        - If the loop finishes, all items matched.

    This pattern appears in validation systems, inventory checks,
    and ensuring all sprites meet a condition.
    """
    for item in my_list:
        if not has_property(item):
            return False
    return True


# ------------------------------------------------------------------
# Variation 4: Build a new list of matching items (filter)
# ------------------------------------------------------------------

def get_matching_items(list):
    """
    Return a brand new list containing ONLY the items that match the property.

    This is the 'filter' pattern:
        - Create an empty list.
        - Loop through the original list.
        - Append items that match the predicate.
        - Return the filtered list.

    This is extremly comman in game development:
        - selecting all enemies in range
        - selecting all bullets that collided
        - selecting all platforms in a region
        - selecting all sprites of a certain type
    """
    matching_list = []

    for item in list:
        if has_property(item):
            matching_list.append(item)

    return matching_list


# ------------------------------------------------------------------
# Test the functions
# ------------------------------------------------------------------

def main():
    """
    Create a list of Alien objects and test each search variation.
    This demonstrates how each function behaves with mixed data.
    """
    alien_list = [
        Alien("Green", 42),
        Alien("Red", 40),
        Alien("Blue", 41),
        Alien("Purple", 40),
    ]

    # Test: Does at least one alien match? (while-loop version)
    result = check_if_one_item_has_property_v1(alien_list)
    print("Result of test check_if_one_item_has_property_v1:", result)

    # Test: Does at least one alien match? (for-loop version)
    result = check_if_one_item_has_property_v2(alien_list)
    print("Result of test check_if_one_item_has_property_v2:", result)

    # Test: Do ALL aliens match the property?
    result = check_if_all_items_have_property(alien_list)
    print("Result of test check_if_all_items_have_property:", result)

    # Test: Build a list of all matching aliens
    result = get_matching_items(alien_list)
    print("Number of items returned from test get_matching_items:", len(result))


if __name__ == "__main__":
    main()



