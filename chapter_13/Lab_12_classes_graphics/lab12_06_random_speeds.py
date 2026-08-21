"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Classes
Lab 12.6 — Random Speeds
"""

# Import modules
import pygame
import random

# -----------------------------------------------------------------
# CONSTANTS
# -----------------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)


# ------------------------------------------------------------
# 🟥 Rectangle Class
# ------------------------------------------------------------
class Rectangle:
    def __init__(self, x: int, y: int, width: int, height: int,
                 change_x: float, change_y: float):
        """ Store position, size, movement speed, and color. """

        self.x      = x
        self.y      = y
        self.width  = width
        self.height = height

        self.change_x = change_x
        self.change_y = change_y

        # Same random color logic
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    def move(self):
        """
        Move the rectangle each frame.
        Bounce off edges
        """

        self.x += self.change_x
        self.y += self.change_y

        # -------------------------------------------------------------
        # Bounce Logic
        # -------------------------------------------------------------
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
        """ Draw the rectangle using its random color. """
        pygame.draw.rect(screen, self.color,
                         (self.x, self.y, self.width, self.height))


# ------------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------------
def main():
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lab 12.6 - Random Speeds")

    rectangle_list = []

    # ---------------------------------------------------------------
    # Each rectangle gets a random speed magnitude.
    # We randomize boty direction and speed using floats.
    # ---------------------------------------------------------------
    for i in range(10):
        x = random.randint(0, 600)
        y = random.randint(0, 400)
        width = random.randint(20, 100)
        height = random.randint(20, 100)

        # Random speed magnitude between 0.5 and 3.0
        speed_x = random.uniform(-3.0, 3.0)
        speed_y = random.uniform(-3.0, 3.0)

        # Avoid zero movement
        if abs(speed_x) < 0.2:
            speed_x = 0.5
        if abs(speed_y) < 0.2:
            speed_y = 0.5

        rectangle = Rectangle(x, y, width, height, speed_x, speed_y)
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

        # Draw all rectangles
        for rect in rectangle_list:
            rect.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
    
