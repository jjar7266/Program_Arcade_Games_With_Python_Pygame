"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 17: Functions - Array-Backed Grids

array_backed_grid.py
"""

import pygame

# ---------------------------------------------------------------------------
# COLOR CONSTANTS
# ---------------------------------------------------------------------------
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

# ---------------------------------------------------------------------------
# GRID CONSTANTS
# ---------------------------------------------------------------------------
WIDTH  = 20     # Width of each cell in pixels
HEIGHT = 20     # Height of each cell in pixels
MARGIN = 5      # Space between cells and screen edges

def main():
    """ Main function for the game. """

    pygame.init()

    # -----------------------------------------------------------------------
    # WINDOW SETUP
    # -----------------------------------------------------------------------
    size = [255, 255]                     # Window size (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Array Backed Grid Example")

    # -----------------------------------------------------------------------
    # GRID SETUP (LOGIC SECTION)
    # Create a 10x10 array filled with zeros.
    # This grid persists for the entire program and stores cell states.
    # -----------------------------------------------------------------------
    grid = []
    for row in range(10):
        grid.append([])                   # Create a new row list
        for column in range(10):
            grid[row].append(0)           # Initialize each cell to 0

    # Example: manually activate one cell
    grid[1][5] = 1

    # -----------------------------------------------------------------------
    # MAIN LOOP CONTROL
    # -----------------------------------------------------------------------
    done = False                          # Loop flag
    clock = pygame.time.Clock()           # Frame rate controller

    # -----------------------------------------------------------------------
    # MAIN PROGRAM LOOP
    # -----------------------------------------------------------------------
    while not done:

        # -------------------------------------------------------------------
        # EVENT PROCESSING
        # -------------------------------------------------------------------
        for event in pygame.event.get():

            # Window close button
            if event.type == pygame.QUIT:
                done = True

            # Mouse click event
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Get pixel coordinates of the click
                pos = pygame.mouse.get_pos()
                print("Click:", pos)

                # Convert pixel coordinates → grid coordinates
                column = pos[0] // (WIDTH + MARGIN)
                row    = pos[1] // (HEIGHT + MARGIN)
                print("Row:", row, "Column:", column)

                # Only update grid if click is inside valid bounds
                if row < 10 and column < 10:
                    grid[row][column] = 1     # Activate the clicked cell

        # -------------------------------------------------------------------
        # GAME LOGIC (none yet for this chapter)
        # -------------------------------------------------------------------



        # -------------------------------------------------------------------
        # DRAWING SECTION
        # -------------------------------------------------------------------
        screen.fill(BLACK)                # Clear screen each frame

        # Draw each cell in the grid
        for row in range(10):
            for column in range(10):

                # Select color based on stored grid value
                color = WHITE
                if grid[row][column] == 1:
                    color = GREEN

                # Draw the cell rectangle
                pygame.draw.rect(
                    screen,
                    color,
                    [
                        (WIDTH  + MARGIN) * column + MARGIN,  # X position
                        (HEIGHT + MARGIN) * row    + MARGIN,  # Y position
                        WIDTH,
                        HEIGHT
                    ]
                )

        # Update the display
        pygame.display.flip()

        # Maintain 60 FPS
        clock.tick(60)

    # -----------------------------------------------------------------------
    # CLEAN EXIT
    # -----------------------------------------------------------------------
    pygame.quit()

# ---------------------------------------------------------------------------
# PYTHON ENTRY POINT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()
