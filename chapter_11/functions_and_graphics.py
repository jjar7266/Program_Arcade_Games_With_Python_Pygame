"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 11: Controllers and Graphics

functions_and_graphics.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: http://youtu.be/_XdrKSDmzqA

# Import modules
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]

# Set the height and width of the screen
size = [400, 500]
screen = pygame.display.set_mode(size)

def draw_snowman(screen, x, y):
    """
    Draw a snowman whose parts are positioned *relative* to (x, y)

    Think of (x, y) as the snowman's "anchor point."
    Every ellipse uses +x and +y so the entire snowman can be moved
    anywhere on the screen simple by changing the (x, y) values.
    """

    # --- Head ---
    # [local_x + x, local_y + y, width, height]
    # local_x = 35, local_y = 0 -> head sits 35px right of the anchor
    pygame.draw.ellipse(screen, WHITE, [35 + x, 0 + y, 25, 25])

    # --- Upper Body ---
    # local_x = 23, local_y = 20 -> slightly left and below the head
    pygame.draw.ellipse(screen, WHITE, [23 + x, 20 + y, 50, 50])

    # --- Lower Body ---
    # local_x = 0, local_y = 65 -> centerd under the upper body
    pygame.draw.ellipse(screen, WHITE, [0 + x, 65 + y, 100, 100])


# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    # Snowman in upper left
    draw_snowman(screen, 10, 10)

    # Snowman in upper right
    draw_snowman(screen, 300, 10)

    # Snowman in lower left
    draw_snowman(screen, 10, 300)

    # Go ahead and update the screen with what we've drawn
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()


