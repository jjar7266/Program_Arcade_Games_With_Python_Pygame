"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Main Functions and Globals

mudball.py

This is a sample text-only game that demonstrates the use of functions.
The game is called "Mudball" and the players take turns lobbing mudballs
at each other until someone gets hit.
"""

# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import math
import random
import subprocess  # used to clear screen

# Clear screen function added
def clear_screen():
    # Windows uses 'cls' macOS/Linux use 'clear'
    command = "cls" if subprocess.os.name == "nt" else "clear"
    subprocess.run(command, shell=True)


def print_instructions():
    """ This function prints the instructions. """

    # You can use the triple-quote string in a print statement to
    # print multiple lines.
    print("""
    Welcome to Mudball! The idea is to hit the other player with a mudball.
    Enter your angle (in degrees) and the amount of PSI to charge your gun with.
    """)


def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance


def get_user_input(name):
    """ Get the user input for psi and angle. Return as a list of two numbers. """
    # Later on in the 'exceptions' chapter, we will learn how to modify
    # this code to not crash the game if the user types in something that
    # isn't a valid number.

    # FIXED INVALID ENTRY
    while True:
        try:
            psi = float(input(name + " charge the gun with how many psi? "))
            angle = float(input(name + " move the gun at what angle? "))
            return psi, angle

        except ValueError:
            print("Please enter a valid number.\n")

    #psi = float(input(name + " charge the gun with how many psi? "))
    #angle = float(input(name + " move the gun at what angle? "))
    #return psi, angle


def get_player_names():
    """ Get a list of names from the players. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True

    print()
    return players


def process_player_turn(player_name, distance_apart):
    """ The code runs the turn for each player.
    if it returns False, keep going with the game.
    If it returns True, someone has won, so stop.
    """
    psi, angle = get_user_input(player_name)

    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart

    # By looking ahead to the chapter on print formatting, these
    # lines could be made to print the numbers in a nice formatted manner
    if difference > 1:
        print("You went", difference, "yards too far!")

    elif difference < -1:
        print("You were", difference * -1, "yards too short!")

    else:
        print("Hit!", player_name, "wins!")
        return True

    print()
    return False


def main():
    """ Main program. """

    # Get the game started.
    clear_screen()  # use our clear screen function

    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)

    # Keep lobbing until someone wins
    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # Process their turn
            done = process_player_turn(player_name, distance_apart)
            # If someone won, 'break' out of this loop and end the game.
            if done:
                break

if __name__ == "__main__":
    main()






