"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13 - Introduction to Classes

Lab 12.3 - Random Rectangle
"""

# Import modules
import pygame
import random

# -------------------------
# CONSTANTS
# -------------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# --------------------------
# 🟥 Rectangle Class
# --------------------------
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

        self.change_x = change_x
        self.change_y = change_y

    def move(self):
        """ Move the rectangle each frame. """
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        """ Draw the rectangle on the screen. """
        pygame.draw.rect(screen, GREEN,
                         (self.x, self.y, self.width, self.height))


# ------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------
def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lab 12.3 - Random Rectangles")

    # ---------------------------------------------------------
    # Instead of ONE rectangle, we create a LIST of rectangles.
    # Each rectangle gets random:
    # - x position
    # - y position
    # - width
    # - height
    # - movement speed (change_x, change_y)
    # ---------------------------------------------------------
    rectangle_list = []

    for i in range(10):  # Create 10 random rectangles
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        width = random.randint(20, 100)
        height = random.randint(20, 100)

        change_x = random.randint(-3, 3)
        change_y = random.randint(-3, 3)

        # Avoid zero movement (boring)
        if change_x == 0:
            change_x = 1
        if change_y == 0:
            change_y = 1

        # Create the rectangle and add it to the list
        rectangle = Rectangle(x, y, width, height, change_x, change_y)
        rectangle_list.append(rectangle)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # --------------------------------------------------------------
        # Move ALL rectangles in the list.
        # --------------------------------------------------------------
        for rect in rectangle_list:
            rect.move()

        screen.fill(BLACK)

        # --------------------------------------------------------------
        # Draw ALL rectangles in the list.
        # --------------------------------------------------------------
        for rect in rectangle_list:
            rect.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
