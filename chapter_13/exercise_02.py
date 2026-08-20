"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes

exercise_02.py

This file contains two small class exercises:

1. A Star class that prints a message when created.
2. A Monster class that uses a constructor to set name and health.
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# ------------------------------------------------------------
# ⭐ Star Class
# ------------------------------------------------------------
class Star:
    def __init__(self):
        # This code runs automatically whenever a new Star object is created.
        # It prints a message to show that a new star has appeared.
        print("A star is born!")



# ------------------------------------------------------------
# 👾 Monster Class
# ------------------------------------------------------------
class Monster:
    def __init__(self, name: str, health: int):
        # Store the monster's name.
        # This lets us know which monster we are working with.
        self.name = name

        # Store the monster's health.
        # Health tells us how strong or alive the monster is.
        self.health = health

        # Print a message showing that the monster has been created.
        print(f"Monster '{self.name}' created with {self.health} health.")


# ----------------------------------------------------------------
# 🧪 Example Usage
# ----------------------------------------------------------------

# Create a Star object. This will automatically print the message.
new_star = Star()

# Create a Monster named Dragon with 50 health.
dragon = Monster("Dragon", 50)

