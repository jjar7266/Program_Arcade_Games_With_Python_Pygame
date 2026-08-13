"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 11: Controllers and Graphics

stick_figure.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]
RED   = [255,   0,   0]

# Set the height and width of the screen
size = [400, 500]
screen = pygame.display.set_mode(size)

# Function that always draws a stickfigure in the same place

def draw_stick_figure(screen, x, y):
    """
    Draw a stick figure whose parts are positioned *relative* to (x, y).

    (x, y) acts as the anchor point for the entire figure.
    Every coordinate uses +x and +y so the whole figure can be moved
    simply by changing the (x, y) values when calling the function.
    """

    # ----------------------------------------------------------------
    # HEAD
    # ----------------------------------------------------------------
    # The head is a small 10x10 circle.
    # It is drawn at (x + 1, y), meaning:
    #  - 1 pixel to the right of the anchor point
    #  - exactly at the anchor's vertical position
    pygame.draw.ellipse(screen, BLACK, [1 + x, y, 10, 10], 0)

    # -----------------------------------------------------------------
    # LEGS
    # -----------------------------------------------------------------
    # Both legs start at the bottom of the body: (5 + x, 17 + y)
    # They angle outward to create a simple walking stance.
    #
    # Right leg: angles down-right
    pygame.draw.line(screen, BLACK,
                    [5 + x, 17 + y],    # hip joint
                    [10 + x, 27 + y],   # foot
                    2)

    # Left leg: angles down-left
    pygame.draw.line(screen, BLACK,
                    [5 + x, 17 + y],    # hip joint
                    [x, 27 + y],        # foot
                    2)

    # ------------------------------------------------------------------
    # BODY
    # ------------------------------------------------------------------
    # The body is a vertical line from:
    #   (5 + x, 17 + y) -> bottom of body
    #   (5 + x, 7 + y)  -> top of body
    #
    # This places the body directly under the head and centered.
    pygame.draw.line(screen, RED,
                    [5 + x, 17 + y],    # bottom of body
                    [5 + x, 7 + y],     # top of body
                    2)

    # ------------------------------------------------------------------
    # ARMS
    # ------------------------------------------------------------------
    # Arms connect at the top of the body: (5 + x, 7 + y)
    # They angle outward to match the leg style.
    #
    # Right arm: angles down-right
    pygame.draw.line(screen, RED,
                    [5 + x, 7 + y],     # shoulder
                    [9 + x, 17 + y],    # hand
                    2)

    # Left arm: angels down-left
    pygame.draw.line(screen, RED,
                    [5 + x, 7 + y],     # shoulder
                    [1 + x, 17 + y],    # hand
                    2)


# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Clear the screen and set the screen background
    screen.fill(WHITE)

    draw_stick_figure(screen, 10, 10)
    draw_stick_figure(screen, 200, 50)
    draw_stick_figure(screen, 50, 50)
    draw_stick_figure(screen, 50, 300)


    # Go ahead and update the screen with what we've drawn
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()


