"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes
Lab 12.9 — Colorful Bouncing Shapes (Rectangles + Ellipses using Inheritance)
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
    def __init__(self, x: float, y: float,
                 width: float, height: float,
                 change_x: float, change_y: float,
                 color: tuple):
        """ Store position, size, movement speed, and color. """

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        self.change_x = change_x
        self.change_y = change_y

        self.color = color

    def move(self, screen_width: int, screen_height: int):
        """ Move the shape and bounce off edges dynamically. """

        self.x += self.change_x
        self.y += self.change_y

        # Bounce horizontally
        if self.x < 0:
            self.x = 0
            self.change_x *= -1

        if self.x + self.width > screen_width:
            self.x = screen_width - self.width
            self.change_x *= -1

        # Bounce vertically
        if self.y < 0:
            self.y = 0
            self.change_y *= -1

        if self.y + self.height > screen_height:
            self.y = screen_height - self.height
            self.change_y *= -1

    def draw(self, screen):
        """ Draw a rectangle. """
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))


# ------------------------------------------------------------
# 🟣 Subclass: Ellipse (inherits from Rectangle)
# ------------------------------------------------------------
class Ellipse(Rectangle):
    def draw(self, screen):
        """ Draw an ellipse using the same attriutes. """
        pygame.draw.ellipse(screen, self.color,
                           (self.x, self.y, self.width, self.height))


# --------------------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------------------
def main():
    pygame.init()

    # Dynamic window size - change these anytime
    WIDTH:  int = 800
    HEIGHT: int = 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Colorful Bouncing Shapes")

    shape_list: list = []

    # -------------------------------------------------------------
    # Create random rectangles and ellipses
    # -------------------------------------------------------------
    num_rectangles: int = 10
    num_ellipses:   int = 10

    for i in range(num_rectangles + num_ellipses):

        width:  float = random.randint(20, 120)
        height: float = random.randint(20, 120)

        x: float = random.randint(0, WIDTH - width)
        y: float = random.randint(0, HEIGHT - height)

        # Random speed
        change_x: float = random.uniform(-3.0, 3.0)
        change_y: float = random.uniform(-3.0, 3.0)

        # Avoid zero movement
        if abs(change_x) < 0.2:
            change_x = 0.5
        if abs(change_y) < 0.2:
            change_y = 0.5

        # Random color
        color: tuple = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        # First half rectangles, second half ellipses
        if i < num_rectangles:
            shape = Rectangle(x, y, width, height,
                              change_x, change_y, color)
        else:
            shape = Ellipse(x, y, width, height,
                            change_x, change_y, color)

        shape_list.append(shape)

    done: bool = False
    clock = pygame.time.Clock()

    # --------------------------------------------------------------
    # Main Loop
    # --------------------------------------------------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(BLACK)

        # Move and draw all shapes
        for shape in shape_list:
            shape.move(WIDTH, HEIGHT)
            shape.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

