"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 12: Bitmapped Graphics and Sound

Show how to run background music in Pygame.

background_music.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import pygame
from pathlib import Path  # Not used by the Author/Instructor

# Base directory for assets (using pathlib to load)
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"

# Define RGB Colors
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Set up the display window
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 12: Adding Background Music")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Play "O Fortuna" by MIT Choir
# Available from:
# https://freemusicarchive.org/music/MIT_Concert_Choir/Carmina_Burana_Carl_Orff/01_1355
music1_path = SOUND_DIR / "MIT Concert Choir - O Fortuna.mp3"
pygame.mixer.music.load(str(music1_path))
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# ---------- Main Program Loop ----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop

        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            #
            # Next, play "Alone" by Saito Koji
            music2_path = SOUND_DIR / "Saito_Koji_-_01_-_Alone.ogg"
            pygame.mixer.music.load(str(music2_path))
            pygame.mixer.music.play()

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program with 'hang'
# on exit if running from IDLE.
pygame.quit()
