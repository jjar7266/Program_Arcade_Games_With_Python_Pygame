"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes
Lab 12.5 — Random Colors
"""

# Import modules
import pygame
import random

# -------------------------------------------
# CONSTANTS
# -------------------------------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)


# ------------------------------------------------------------
# 🟥 Rectangle Class
# ------------------------------------------------------------
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int,
                 change_x: int, change_y: int):
        """ Store position, size, movement speed, and now color. """

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        self.change_x = change_x
        self.change_y = change_y

        # ------------------------------------------------------
        # Each rectangle gets its own random RGB color.
        # Values range from 0-255.
        # ------------------------------------------------------
        self.color = (
            random.randint(0, 255),    # Red
            random.randint(0, 255),    # Green
            random.randint(0, 255)     # Blue
        )

    def move(self):
        """
        Move the rectangle each frame.
        Bounce off edges
        """

        # Move first
        self.x += self.change_x
        self.y += self.change_y

        # -------------------------------------------------------
        # Bounce Logic
        # -------------------------------------------------------

        # Bounce left or right
        if self.x < 0:
            self.x = 0
            self.change_x *= -1
            if self.change_x == 0:
                self.change_x = 1

        if self.x + self.width > 700:
            self.x = 700 - self.width
            self.change_x *= -1
            if self.change_x == 0:
                self.change_x = 1

        # Bounce top or bottom
        if self.y < 0:
            self.y = 0
            self.change_y *= -1
            if self.change_y == 0:
                self.change_y = 1

        if self.y + self.height > 500:
            self.y = 500 - self.height
            self.change_y *= -1
            if self.change_y == 0:
                self.change_y = 1

    def draw(self, screen):
        """
        Draw the rectangle on the screen.

        Use the rectangle's random color instead of a fixed color.
        """
        pygame.draw.rect(screen, self.color,
                        (self.x, self.y, self.width, self.height))


# ---------------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------------
def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lab 12.5 - Random Colors")

    rectangle_list = []

    # Same random rectangle creation
    for i in range(10):
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        width = random.randint(20, 100)
        height = random.randint(20, 100)

        change_x = random.randint(-3, 3)
        change_y = random.randint(-3, 3)

        if change_x == 0:
            change_x = 1
        if change_y == 0:
            change_y = 1

        rectangle = Rectangle(x, y, width, height, change_x, change_y)
        rectangle_list.append(rectangle)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Move all rectangles
        for rect in rectangle_list:
            rect.move()

        screen.fill(BLACK)

        # Draw all rectangles (now with random colors)
        for rect in rectangle_list:
            rect.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()


