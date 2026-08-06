"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 6: Introduction to Graphics

6.13 - Drawing a Rectangle

drawing_rectangle_6_13.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=53ucZ6_7_t4&t=6s

# Import modules
import pygame

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

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

    for x in range(0, 100, 20):
        pygame.draw.line(screen, GREEN, [x, 0], [x, 100], 5)

    # Draw a rectangle
    pygame.draw.rect(screen, BLACK, [150, 50, 250, 100], 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit:
pygame.quit()

