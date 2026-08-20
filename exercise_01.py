"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes

exercise_01.py

1 - Create a class called Cat. Give it attributes for name, color, and weight.
    Give it a method called meow.

2 - Create an instance of the cat class, set the attributes, and call
    the meow method.

3 - Create a class called Monster. Give it an attribute for name and an
    integer attribute for health. Create a method called decrease_health
    that takes in a parameter amount and decreases the health by that much.
    Inside that method, print that the animal died if health goes below zero.
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# ------------------------------------------------------------------
# 🐱 Cat Class
# ------------------------------------------------------------------
class Cat:
    def __init__(self, name: str, color: str, weight: float):
        # When we create a Cat, we give it a name, color, and weight.
        # These pieces of information are stored inside the object.
        self.name   = name
        self.color  = color
        self.weight = weight

    def meow(self):
        # This method makes the cat "speak"
        # It prints a message using the cat's name.
        print(f"{self.name} says: Meow!")


# --------------------------------------------------------------------
# 👾 Monster Class
# --------------------------------------------------------------------
class Monster:
    def __init__(self, name: str, health: int):
        # Each monster has a name and a health value.
        # Health tells us how strong or alive the monster is.
        self.name   = name
        self.health = health

    def decrease_health(self, amount: int):
        # This method lowers the monster's health by a certain amount.
        # The 'amount' is passed in when we call the method.
        self.health -= amount

        # Show the new health value after taking damage.
        print(f"{self.name}'s health is now {self.health}")

        # If health drops to zero or below, the monster has "died".
        if self.health <= 0:
            print(f"{self.name} has died 💀")


# ---------------------------------------------------------------------
# 🧪 Example Usage
# ---------------------------------------------------------------------

# Create a cat named Whiskers.
my_cat = Cat("Whiskers", "gray", 4.2)
# Tell the cat to meow.
my_cat.meow()

# Create a monster named Goblin with 10 health points.
beast = Monster("Goblin", 10)
# Make the monster lose some health.
beast.decrease_health(3)
# Make the monster lose more health until it dies.
beast.decrease_health(8)


