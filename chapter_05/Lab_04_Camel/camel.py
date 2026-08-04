"""
Program Arcade Games With Python and Pygame
Fourth Edition
Author: Dr. Paul Vincent Craven
Copyright 2016

coded (2026) along by: Jose 'Joe' Ruiz

Lab 4: Camel

camel.py

Description of the Camel Game:
    - The idea is to ride your camel across the desert while being chased.
    - You need to manage your thirst, how tired the camel is, and how far
    - ahead of the natives you are.

Sample Run of Camel:

Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and outrun the natives.

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
Your choice? C

You traveled 12 miles.

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
Your choice? C

You traveled 17 miles.

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
Your choice? e

Miles traveled:  29
Drinks in canteen:  3
The natives are 31 miles behind you.

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
Your choice? b

You traveled 6 miles.

...and so on until...

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
Your choice? C

You traveled 12 miles.
The natives are getting close!

A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
Your choice? C

You traveled 11 miles.
The natives are getting close!
You made it across the desert! You won!
"""
# Import modules
import subprocess
import random

# Game State Variable
canteen_drinks = 3
thirst = 0
camel_tiredness = 0
miles_traveled = 0
natives_distance = -20


# Clears the terminal screen
def clear_screen():
    subprocess.run("cls", shell=True)

clear_screen()

print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down!")
print("Survive your desert trek and outrun the natives")
print()

done = False

while not done:

    # Menu
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    choice = input("Your choice? ").upper()

    if choice == "A":
        if thirst == 0:
            print("You're not thirsty yet.")
        elif canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
            print("You take a drink from your canteen.")
        else:
            print("Your canteen is empty!")

    elif choice == "B":
        miles = random.randint(5, 12)
        miles_traveled += miles
        print(f"You traveled {miles} miles at moderate speed.")

        thirst += 1
        camel_tiredness += 1

        natives_distance += random.randint(7, 14)

    elif choice == "C":
        miles = random.randint(10, 20)
        miles_traveled += miles
        print(f"You traveled {miles} miles at full speed!")

        thirst += 2
        camel_tiredness += random.randint(1, 3)

        natives_distance += random.randint(7, 14)

    elif choice == "D":
         print("You stop for the night.")

         rest_amount = random.randint(2, 4)
         camel_tiredness = max(0, camel_tiredness - rest_amount)
         print(f"Your camel rests and recovers {rest_amount} tiredness.")

         natives_distance += random.randint(7, 14)

    elif choice == "E":
         print(f"Miles traveled: {miles_traveled}")
         print(f"Drinks in canteen: {canteen_drinks}")
         print(f"Camel tiredness: {camel_tiredness}")

         distance_behind = miles_traveled - natives_distance
         print(f"The natives are {distance_behind} miles behind you.")

    elif choice == "Q":
            done = True
            print("You quit the game.")
            break

    # -- Danger Checks --

    # Thirst danger
    if thirst > 6:
         print("You died of thirst!")
         done = True

    elif thirst > 4:
         print("You are thirsty!")

    # Camel tiredness danger
    if camel_tiredness > 8:
         print("Your camel has died of exhaustion.")
         done = True

    # Natives catching you
    if natives_distance >= miles_traveled:
         print("The natives have caught you!")
         done = True
    else:
         distance_behind = miles_traveled - natives_distance
         if distance_behind < 15:
              print("The natives are getting close!")

    # Win condition
    if miles_traveled >= 200:
         print("You made it across the desert! You won!")
         done = True







