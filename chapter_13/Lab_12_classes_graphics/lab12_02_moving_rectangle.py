"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13 - Introduction to Classes

Lab 12.2 - Moving Rectangle
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
# 🟥 Rectangle Class (now with movement!)
# ---------------------------------
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int,
                 change_x: int, change_y: int):

        """
        Store position, size, and movement speed.
        """

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        # --------------------------------------------------------
        # NEW FOR LAB 12.2:
        # We add horizontal and vertical speed values.
        # These control how much the rectangle moves each frame.
        # --------------------------------------------------------
        self.change_x = change_x
        self.change_y = change_y

    # --------------------------------------------------------
    # NEW FOR LAB 12.2:
    # This method updates the rectangle's position each frame.
    # --------------------------------------------------------
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

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
    pygame.display.set_caption("Lab 12.2 - Moving Rectangle")

    # ------------------------------------------
    # MODIFIED FOR LAB 12.2:
    # We now pass movement values (3, 2) to the Rectangle constructor.
    # ------------------------------------------
    my_rectangle = Rectangle(50, 50, 100, 80, 3, 2)

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

        # ----------------------------------------
        # NEW FOR LAB 12.2:
        # Move the rectangle each frame
        # ----------------------------------------
        my_rectangle.move()

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

