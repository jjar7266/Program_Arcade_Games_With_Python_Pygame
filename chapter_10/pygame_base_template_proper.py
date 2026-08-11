"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 10: Functions - Main Functions and Globals

pygame_base_template_proper.py

Pygame base template for opening a window, done with functions
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

import pygame

# ------------------------------------------------------------------
# TEACHER MODE:
# These are CONSTANTS - values that NEVER change.
# Constants are the ONLY type of global that is safe.
# They make your code readable and avoid magic numbers.
#
# STUDENT MODE (OH WOW I GET IT):
# ohhhh... constants can live at the top of the file because
# they never change. They aren't "evil globals" - they're
# just shared settings the whole program can use safely.
# --------------------------------------------------------------------

# Define some colors as global constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

def main():
    """ Main function for the game. """

    # -------------------------------------------------------------
    # TEACHER MODE:
    # Putting pygame.init() INSIDE main() is proper architecture.
    # It prevents accidental execution when this file is imported.
    # It keeps initialization controlled and avoids global side effects.
    #
    # STUDENT MODE (OH WOW I GET IT):
    # Ohhh... so pygame.init() shouldn't run automatically when
    # the file loads. Putting it in main() means it only runs
    # when I CALL main(). This is how real Python programs work.
    # --------------------------------------------------------------
    pygame.init()

    # Set the width and height of the screen [width, height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop ----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # ALL CODE TO DRAW SHOLD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program with 'hang'
    # on exit if running from IDLE.
    pygame.quit()

# ------------------------------------------------------------------
# TEACHER MODE:
# This is the official Python entry point:
# It ensures main() only runs when THIS file is executed directly.
# If another file imports this one, main() with NOT run.
#
# STUDENT MODE (OH WOW I GET IT):
# Ohhh... so THIS is why Python programs use main().
# It prevents accidental execution and makes the file reusable.
# --------------------------------------------------------------------
if __name__ == "__main__":
    main()



