"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 6: Introduction to Graphics

5.11 - Drawing Lines

drawing_lines_5_11.py

Use the base template from the prior example and add the code to draw lines.
Read the comments to figure out exactly where to put the code.
Try drawing lines with different thicknesses, colors, and locations.
Draw several lines.
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)  # Added a new color

# Initialize Pygame
pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ------ Main Program Loop ------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should be here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing
    # the background image.
    screen.fill(WHITE)

    # --- Drawing code should go here

    # Draw on the screen line from (0, 0) to (100, 100)
    # that is 5 pixels wide.
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)

    # Draw a blue line
    pygame.draw.line(screen, BLUE, [100, 100], [300, 50], 10)

    # Draw a red line
    pygame.draw.line(screen, RED, [300, 50], [200, 300], 12)

    # Draw a black line
    pygame.draw.line(screen, BLACK, [300, 300], [100, 350], 25)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit:
pygame.quit()

