"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 6: Introduction to Graphics

6.15 - Drawing an Arc

drawing_arc_6_15.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation Video: https://www.youtube.com/watch?v=Ok3vbJ0cwtk

# Import modules
import pygame
from math import pi  # modernized (not in the book)

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

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

    # ---------------------------------------------------------------

    # NOTE (Modern Pygame Adjustment):
    # The original 2016 book uses the bounding box [100, 100, 250, 200] for
    # arcs. On modern high‑DPI displays, this produces a shape that looks
    # closer to a circle. Increasing the width to 400 restores the elongated
    # oval appearance shown in the book.
    # ----------------------------------------------------------------

    # Angle reference (radians):
    # 0       → right
    # pi/2    → down
    # pi      → left
    # 3*pi/2  → up
    # 2*pi    → full circle

    # Debug: visualize the bounding box (optional)
    pygame.draw.rect(screen, BLACK, [100, 100, 400, 200], 1)

    # Draw an arc as part of an ellipse. Use radians to determine
    # what angle to draw.
    pygame.draw.arc(screen, GREEN, [100, 100, 400, 200], pi/2, pi, 2)
    pygame.draw.arc(screen, BLACK, [100, 100, 400, 200], 0, pi/2, 2)
    pygame.draw.arc(screen, RED, [100, 100, 400, 200], 3*pi/2, 2*pi, 2)
    pygame.draw.arc(screen, BLUE, [100, 100, 400, 200], pi, 3*pi/2, 2)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit:
pygame.quit()

