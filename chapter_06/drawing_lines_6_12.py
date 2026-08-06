"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 6: Introduction to Graphics

6.12 - Drawing Lines With Loops and Offsets

drawing_lines_6_12.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import pygame
import math

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

    # --------------------------------------------------------------
    # Draw on the screen several lines from (0, 10) to (100, 110)

    # 5 pixels wide using a while loop
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 100 + y_offset], 5)
        y_offset = y_offset + 10

    # ---------------------------------------------------------------
    # Draw on the screen several lines from (0, 150) to (120, 250)

    # 5 pixels wide using a for loop.
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, BLUE, [0, 150 + y_offset], [100, 250 + y_offset], 5)

    # ----------------------------------------------------------------
    # Complex offsets

    # For this code, make sure to have a line that says
    # "import math" at the top of your program. Otherwise
    # it won't know what math.sin is.

    for i in range(200):

        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x, y], [x + 5, y], 5)

    # ----------------------------------------------------------------
    # Drawing a series of x's

    for x_offset in range(400, 650, 30):
        pygame.draw.line(screen, BLACK, [x_offset, 100], [x_offset - 10, 90], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset - 10, 100], 2)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit:
pygame.quit()

