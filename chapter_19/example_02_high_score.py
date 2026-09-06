"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 19: Exceptions

Example: This shows how to save a high score between games.
         The score is stored in a file called high_score.txt.

example_02_high_score.py
"""

# ----------------------------------------------------------------
# This program shows how to remember a high score by saving it
# in a file. When the game starts, we try to read the score.
# When the player gets a new high score, we save it.
# ----------------------------------------------------------------

def get_high_score():
    # Start with a default high score of 0.
    high_score = 0

    try:
        # Try to open the file that stores the high score.
        # "with open" automatically closes the file for us.
        with open("high_score.txt", "r") as high_score_file:
            # Read the number inside the file.
            high_score = int(high_score_file.read())

        # Show the high score we found.
        print("The high score is:", high_score)

    except IOError:
        # This happens if the file doesn't exist yet.
        print("There is no high score yet.")

    except ValueError:
        # This happens if the file exists but the text inside
        # is not a number we can understand.
        print("I'm confused. Starting with no high score.")

    # Give back the high score we found (or 0 if there was a problem).
    return high_score


def save_high_score(new_high_score):
    try:
        # Try to open the file so we can write the new high score.
        # "with open" makes sure the file closes automatically.
        with open("high_score.txt", "w") as high_score_file:
            # Write the number as text.
            high_score_file.write(str(new_high_score))

    except IOError:
        # This happens if Python can't write to the file.
        print("Unable to save the high score.")


def main():
    """ Main program is here. """

    # First, get the high score from the file
    high_score = get_high_score()

    # Ask the player for their score from this game.
    current_score = 0

    try:
        # Try to turn what they typed into a number.
        current_score = int(input("What is your score? "))

    except ValueError:
        # This happens if they typed something that isn't a number.
        print("I don't understand what you typed.")

    # Check if the player beat the high score.
    if current_score > high_score:
        print("Yea! New high score!")

        # Save the new high score to the file.
        save_high_score(current_score)
    else:
        print("Better luck next time.")

# Entry point: Start the program
if __name__ == "__main__":
    main()

