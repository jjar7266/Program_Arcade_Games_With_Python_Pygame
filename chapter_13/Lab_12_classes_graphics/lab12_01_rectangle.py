"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13 - Introduction to Classes

Lab 12.1 - Rectangle Class
"""

# Import modules
import pygame

# CONSTANTS
# These are safe globals because they never change.
# ---------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# ---------------------------------
# 🟥 Rectangle Class
# ---------------------------------
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int):
        """
        When we create a Rectangle object, we give it:
        - an x position
        - a y position
        - a width
        - a height

        These values get stored inside the object so it remembers
        where it should be drawn and how big it is.
        """
        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

    def draw(self, screen):
        """
        Draw the rectangle on the screen.

        pygame.draw.rect() needs:
        - which screen to draw on
        - what color to use
        - a rectangle defined by (x, y, width, height)
        """
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))


# ----------------------
# MAIN PROGRAM
# ----------------------
def main():
    """ Main function for the program. """

    # Initialize pygame inside main() - proper architecture.
    pygame.init()

    # Create the window.
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lab 12.1 - Rectangle Class")

    # Create a Rectangle object.
    # These numbers are just examples:
    # x = 50, y = 50, width = 100, height = 80
    my_rectangle = Rectangle(50, 50, 100, 80)

    # Loop until the user closes the window.
    done = False
    clock = pygame.time.Clock()

    while not done:
        # ----------------------
        # EVENT PROCESSING
        # ----------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # -----------------------
        # GAME LOGIC (none yet)
        # -----------------------

        # -----------------------
        # DRAWING CODE
        # -----------------------
        screen.fill(BLACK)

        # Draw our rectangle object.
        my_rectangle.draw(screen)

        # Update the screen.
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ------------------------
# ENTRY POINT
# ------------------------
if __name__ == "__main__":
    main()

