"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 20: Recursion

example that draws lines in a pattern, and recursively keeps drawing
smaller versions of the pattern in each quadrant.

fractal.py
"""

# Import modules
import pygame

# COLORS
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)


# Recursive Drawing Function
def recursive_draw(screen, x, y, width, height, count):
    """
    Draw a simple line pattern, then draw smaller copies of the pattern
    in each quadrant.

    Think of this like splitting a square into four smaller squares:
      - First we draw the pattern in the big square.
      - Then we shrink the square to half size.
      - We keep doing this until 'count' reaches zero.
    """

    # Draw the line pattern inside the current rectangle

    # Horizontal line across the middle
    pygame.draw.line(
        screen,
        BLUE,
        [x + width * 0.25, y + height * 0.5],
        [x + width * 0.75, y + height * 0.5],
        3
    )

    # Left vertical line
    pygame.draw.line(
        screen,
        RED,
        [x + width * 0.25, y + height * 0.25],
        [x + width * 0.25, y + height * 0.75],
        3
    )

    # Right vertical line
    pygame.draw.line(
        screen,
        GREEN,
        [x + width * 0.75, y + height * .25],
        [x + width * 0.75, y + height *  0.75],
        3
    )

    # Recursive step: draw smaller versions in each quadrant
    if count > 0:
        count -= 1

        half_w = width // 2
        half_h = height // 2

        # Top-left quadrant
        recursive_draw(screen, x, y, half_w, half_h, count)

        # Top-right quadrant
        recursive_draw(screen, x + half_w, y, half_w, half_h, count)

        # Bottom-left quadrant
        recursive_draw(screen, x, y + half_h, half_w, half_h, count)

        # Bottom-right quadrant
        recursive_draw(screen, x + half_w, y + half_h, half_w, half_h, count)


# Main Program

def main():
    """ Main game loop that draws the recursive line fractal. """

    pygame.init()

    size = (700, 700)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Recursive Line Fractal")

    done = False
    clock = pygame.time.Clock()

    # ---------- Main Program Loop ----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill(WHITE)

        # Draw the fractal starting at level 3
        fractal_level = 3
        recursive_draw(screen, 0, 0, 700, 700, fractal_level)

        pygame.display.flip()
        clock.tick(20)

    pygame.quit()


# Run program
if __name__ == "__main__":
    main()
