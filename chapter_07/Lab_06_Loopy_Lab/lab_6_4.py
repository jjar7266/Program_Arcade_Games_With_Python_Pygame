"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Lab 7: Loopy Lab: 6.4 Part 4

lab_6_4.py
"""

# ------------------------------------------------------------
# STEP 1: Import Pygame
# ------------------------------------------------------------
import pygame

# ------------------------------------------------------------
# STEP 2: Initialize Pygame
# ------------------------------------------------------------
# This sets up all internal modules (graphics, input, timing, etc.)
pygame.init()

# ------------------------------------------------------------
# STEP 3: Define Colors
# ------------------------------------------------------------
# We will use a list of colors to create a rainbow pattern.
# Each color is an RGB tuple: (Red, Green, Blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RAINBOW = [
    (255,   0,   0),   # Red
    (255, 165,   0),   # Orange
    (255, 255,   0),   # Yellow
    (  0, 255,   0),   # Green
    (  0, 127, 255),   # Blue
    ( 75,   0, 130),   # Indigo
    (148,   0, 211),   # Violet
]

# ------------------------------------------------------------
# STEP 4: Create the Window
# ------------------------------------------------------------
# The window size is given as (width, height)
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Lab 6.4 Part 4 - Rainbow Grid")

# ------------------------------------------------------------
# STEP 5: Main Loop Control
# ------------------------------------------------------------
done = False
clock = pygame.time.Clock()

# ============================================================
# STEP 6: Main Program Loop
# ============================================================
# This loop runs over and over until the user closes the window.
while not done:

    # --------------------------------------------------------
    # EVENT HANDLING
    # --------------------------------------------------------
    # Pygame collects events (mouse clicks, key presses, window close)
    # into a queue. We loop through them and respond accordingly.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  # Exit the loop

    # --------------------------------------------------------
    # CLEAR THE SCREEN
    # --------------------------------------------------------
    # Before drawing anything new, we clear the screen to white.
    # If you draw BEFORE clearing, your drawings will be erased.
    screen.fill(WHITE)

    # ============================================================
    # DRAWING SECTION — Rainbow Rectangle Grid
    # ============================================================
    # This lab teaches nested loops:
    #
    #   • Outer loop → rows (vertical movement)
    #   • Inner loop → columns (horizontal movement)
    #
    # The idea:
    #   We move across the screen in small steps, drawing a rectangle
    #   at each step. The step size is (rect_size + spacing).
    #
    # Rectangle position:
    #   x = col
    #   y = row
    #
    # Color pattern:
    #   We cycle through the RAINBOW list using modular arithmetic.
    #
    # ============================================================

    # Size of each rectangle
    rect_width  = 5
    rect_height = 5

    # Space between rectangles
    spacing = 2

    # ------------------------------------------------------------
    # OUTER LOOP — Controls vertical movement (rows)
    # ------------------------------------------------------------
    # range(start, stop, step)
    #
    # We start at row = 0
    # We stop at row = size[1] (screen height)
    # We move down by (rect_height + spacing) each time
    #
    # Example:
    #   row = 0, 7, 14, 21, ...
    #
    # This determines how many rows of rectangles we draw.
    # ------------------------------------------------------------
    for row in range(0, size[1], rect_height + spacing):

        # --------------------------------------------------------
        # INNER LOOP — Controls horizontal movement (columns)
        # --------------------------------------------------------
        # Same idea as the row loop, but moving left → right.
        #
        # Example:
        #   col = 0, 7, 14, 21, ...
        #
        # Each (row, col) pair represents the top-left corner
        # of a rectangle.
        # --------------------------------------------------------
        for col in range(0, size[0], rect_width + spacing):

            # ----------------------------------------------------
            # COLOR SELECTION — Rainbow Cycling
            # ----------------------------------------------------
            # We want the colors to repeat in a pattern.
            #
            # First, compute how many "steps" we have moved:
            #   row_step = row // (rect_height + spacing)
            #   col_step = col // (rect_width + spacing)
            #
            # Add them together to get a diagonal pattern.
            #
            # Then use modulo (%) to wrap around the RAINBOW list.
            #
            # Example:
            #   If color_index becomes 12 and len(RAINBOW) = 7,
            #   12 % 7 = 5 → valid index inside the list.
            # ----------------------------------------------------
            color_index = (
                row // (rect_height + spacing)
                + col // (rect_width + spacing)
            ) % len(RAINBOW)

            color = RAINBOW[color_index]

            # ----------------------------------------------------
            # DRAW THE RECTANGLE
            # ----------------------------------------------------
            # pygame.draw.rect(surface, color, (x, y, width, height))
            #
            # This draws a filled rectangle at the given position.
            # ----------------------------------------------------
            pygame.draw.rect(screen, color, (col, row, rect_width, rect_height))

    # --------------------------------------------------------
    # UPDATE THE SCREEN
    # --------------------------------------------------------
    pygame.display.flip()

    # --------------------------------------------------------
    # FRAME RATE LIMIT
    # --------------------------------------------------------
    # This keeps the loop running at 60 frames per second.
    clock.tick(60)

# ------------------------------------------------------------
# CLEAN SHUTDOWN
# ------------------------------------------------------------
pygame.quit()
