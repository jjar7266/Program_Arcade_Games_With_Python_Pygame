"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes
Lab 12.8 — Random Everything (Dynamic Window Version)
"""

# Import modules
import pygame
import random

# --------------------------------------------------------------------
# CONSTANTS
# --------------------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)


# ------------------------------------------------------------
# 🟥 Rectangle Class
# ------------------------------------------------------------
class Rectangle:
    def __init__(self, x: float, y: float,
                 width: float, height: float,
                 change_x: float, change_y: float,
                 color: tuple):
        """
        Store position, size, movement speed, and color.

        - All attributes are randomized in main()
        - Class simply stores them
        """

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        self.change_x = change_x
        self.change_y = change_y

        self.color = color

    def move(self, screen_width: int, screen_height: int):
        """
        Move the rectangle and bounce off edges.

        Bounce logic now uses dynamic screen size.
        """

        self.x += self.change_x
        self.y += self.change_y

        # Bounce left or right
        if self.x < 0:
            self.x = 0
            self.change_x *= -1

        if self.x + self.width > screen_width:
            self.x = screen_width - self.width
            self.change_x *= -1

        # Bounce top or bottom
        if self.y < 0:
            self.y = 0
            self.change_y *= -1

        if self.y + self.height > screen_height:
            self.y = screen_height - self.height
            self.change_y *= -1

    def draw(self, screen):
        """ Draw the rectangle using its random color. """
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))


# -----------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------
def main():
    pygame.init()

    # -------------------------------------------------------------
    # Window size is now fully dynamic.
    # Change WIDTH and HEIGHT and everything still works.
    # -------------------------------------------------------------
    WIDTH  = 800
    HEIGHT = 600
    size = (WIDTH, HEIGHT)

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lab 12.8 - Random Everything (Dynamic Window)")

    rectangle_list = []

    # --------------------------------------------------------------
    # Random EVERYTHING:
    # - random count of rectangles
    # - random size
    # - random speed
    # - random color
    # ---------------------------------------------------------------
    num_rectangles = random.randint(10, 25)

    for i in range(num_rectangles):

        # Random size
        width  = random.randint(20, 120)
        height = random.randint(20, 120)

        # Random position (must fit inside window)
        x = random.randint(0, WIDTH - width)
        y = random.randint(0, HEIGHT - height)

        # Random speed (floats)
        change_x = random.uniform(-4.0, 4.0)
        change_y = random.uniform(-4.0, 4.0)

        # Avoid zero movement
        if abs(change_x) < 0.2:
            change_x = 0.5
        if abs(change_y) < 0.2:
            change_y = 0.5

        # Random color
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        rectangle = Rectangle(x, y, width, height,
                              change_x, change_y, color)
        rectangle_list.append(rectangle)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Move all rectangles (pass dynamic window size)
        for rect in rectangle_list:
            rect.move(WIDTH, HEIGHT)

        screen.fill(BLACK)

        # Draw all rectangles
        for rect in rectangle_list:
            rect.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

