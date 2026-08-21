"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes
Lab 12.10 — Colorful Shapes - Rectangles + Ellipses using Inheritance
"""

# Import modules
import pygame
import random

# ------------------------------------------------------------
# CONSTANTS
# ------------------------------------------------------------
BLACK = (0, 0, 0)


# ------------------------------------------------------------
# 🟥 Base Class: Rectangle
# ------------------------------------------------------------
class Rectangle:
    def __init__(self, x, y, width, height, color):
        """ Store position, size, and color. """

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        self.color  = color

    def draw(self, screen):
        """ Draw a rectangle. """
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))


# ------------------------------------------------------------
# 🟣 Subclass: Ellipse (inherits from Rectangle)
# ------------------------------------------------------------
class Ellipse(Rectangle):
    def draw(self, screen):
        """ Draw an ellipse using the same attributes. """
        pygame.draw.ellipse(screen, self.color,
                            (self.x, self.y, self.width, self.height))


# -------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------
def main():
    pygame.init()

    # Dynamic window size - change these anytime
    WIDTH  = 900
    HEIGHT = 700
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Colorful Shapes - Rectangles + Ellipses")

    shape_list = []

    # -----------------------------------------------------------
    # Create LOTS of shapes (rectangles + ellipses)
    # -----------------------------------------------------------
    num_rectangles = 500
    num_ellipses   = 500

    # Random rectangles
    for i in range(num_rectangles):
        width  = random.randint(10, 120)
        height = random.randint(10, 120)

        x = random.randint(0, WIDTH - width)
        y = random.randint(0, HEIGHT - height)

        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        rect = Rectangle(x, y, width, height, color)
        shape_list.append(rect)

    # Random ellipses
    for i in range(num_ellipses):
        width  = random.randint(10, 120)
        height = random.randint(10, 120)

        x = random.randint(0, WIDTH - width)
        y = random.randint(0, HEIGHT - height)

        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        ellipse = Ellipse(x, y, width, height, color)
        shape_list.append(ellipse)

    # ----------------------------------------------------------------
    # Main Loop
    # ----------------------------------------------------------------
    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        # Draw all shapes
        for shape in shape_list:
            shape.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

