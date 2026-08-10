"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 9: Introduction to Animation

animating_snow.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=Gkhz3FuhGoI

# Import modules
import pygame
import random

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Create an empty array
star_list = []

for i in range(50):
            x = random.randrange(0, 700)
            y = random.randrange(0, 500)
            star_list.append([x, y])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

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
    screen.fill(BLACK)

    for item in star_list:

            # Create falling snow
            item[1] += 1
            pygame.draw.circle(screen, WHITE, item, 2)

            if item[1] > 500:
                  item[1] = random.randrange(-20, -5)  #
                  item[0] = random.randrange(700)

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit:
pygame.quit()

