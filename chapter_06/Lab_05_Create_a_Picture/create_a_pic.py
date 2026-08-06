"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 6: Introduction to Graphics
Lab 5: Create-a-Picture

Your assignment:
    Draw a pretty picture. The goal of this lab is to get practice using
    functions, using for loops, and introduce computer graphics.

File: create_a_pic.py

Description:
    This program is my Lab 5 submission. It creates a sunset scene using
    Pygame drawing commands. The lab requires multiple colors, multiple
    shape types, and at least one repeating pattern created with a
    for-loop and an offset.
"""

# Import modules
import pygame
import random

# Initialize Pygame
pygame.init()

# Create the Display Window
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lab 5 - Sunset Scene")

# ---------------------------
# COLOR CONSTANTS
# ---------------------------

BLACK           = (  0,   0,   0)
ORANGE          = (255, 179,  71)
PEACH           = (255, 209, 148)
SKY_BLUE        = (135, 206, 235)

OCEAN_BLUE      = ( 30, 144, 255)
WHITE           = (255, 255, 255)

SUN_YELLOW      = (255, 255,   0)

BOARDWALK_BROWN = (139,  69,  19)
PLANK_BROWN     = ( 90,  51,  16)

LAMP_GRAY       = (150, 150, 150)
LAMP_GOLD       = (255, 215,   0)

ISLAND_SAND     = (160, 120,  60)
PALM_TRUNK      = (101,  67,  33)
PALM_LEAF       = ( 34, 139,  34)

# CLOCK
clock = pygame.time.Clock()

FPS = 60  # Frames per second

# ------------------------------
# STAR FIELD (generated once)
# ------------------------------
stars = []

for _ in range(30):  # number of stars
    x = random.randint(0, 800)
    y = random.randint(0, 180)  # only in the upper sky
    size = random.randint(1, 2) # tiny stars look translucent
    stars.append([x, y, size, random.randint(0, 20)])
    # last number = twinkle timer

# -------------------------------
# Main Loop Setup
# -------------------------------
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Drawing Code Goes Here ---

    # ------------------------------
    # SKY GRADIENT
    # ------------------------------
    pygame.draw.rect(screen, SKY_BLUE, (0,   0, 800, 200))
    pygame.draw.rect(screen, PEACH, (0, 200, 800, 200))
    pygame.draw.rect(screen, ORANGE, (0, 350, 800, 150))

    # -------------------------------
    # OCEAN
    # -------------------------------
    pygame.draw.rect(screen, OCEAN_BLUE, (0, 500, 800, 100))

    # -------------------------------
    # WAVES - ROW 1
    # -------------------------------

    # Loop from 0 to 800 in steps of 40.
    # This means we'll draw one wave every 40 pixels horizontally across the screen.
    for i in range(0, 800, 40):

        # Draw a white arc (half-circle) to represent a wave crest.
        # Parameters:
        #   screen -> where to draw (your display surface)
        #   WHITE  -> color constant for the wave
        #   (i, 520, 40, 20) -> rectangle defining the arc's position and size:
        #       i      -> horizontal offset (moves each wave to the right)
        #       520    -> vertical position (controls how high or low the waves sit)
        #       40     -> width of each wave segment
        #       20     -> height of each wave segment
        #   0, 3.14 -> start and end angles in radians (0 to π draws the top half)
        #   2       -> line thickness in pixels
        pygame.draw.arc(screen,
                        WHITE,
                        (i, 520, 40, 20),
                        0,
                        3.14,
                        2)

    # ----------------------------
    # WAVES - ROW 2 (offset)
    # ----------------------------
    for i in range(0, 800, 40):

        # Second row is shifted right by +20 and down by + 20
        pygame.draw.arc(screen,
                        WHITE,
                        (i + 20, 540, 40, 20),  # x = i + 20, y = 540
                        0,
                        3.14,
                        2)

    # ----------------------------
    # (optional) Third row of smaller waves
    # ----------------------------

    for i in range(0, 800, 40):

        pygame.draw.arc(screen,
                        WHITE,
                        (i + 10, 560, 30, 15),
                        0,
                        3.14,
                        1)

    # ----------------------------
    # (optional) BOARDWALK
    # ----------------------------

    #pygame.draw.rect(screen, BOARDWALK_BROWN, (0, 560, 800, 40))

    # ----------------------------
    # (optional) PLANK LINES
    # ----------------------------
    #for x in range(0, 800, 40):
    #    pygame.draw.line(screen, PLANK_BROWN, (x, 560), (x, 600), 3)

    # ----------------------------
    # Beach (soft sand)
    # ----------------------------
    #pygame.draw.rect(screen, (240, 220, 170), (0, 560, 800, 40))

    # -----------------------------
    # ((optional) LAMP POST
    # -----------------------------
    #pygame.draw.rect(screen, LAMP_GRAY, (380, 480, 10, 80))

    # ------------------------------
    # (optional) LAMP HEAD
    # ------------------------------
    #pygame.draw.circle(screen, LAMP_GOLD, (385, 480), 15)

    # -------------------------------
    # BIRDS (simple V-shapes)
    # -------------------------------
    pygame.draw.line(screen, BLACK, (200, 150), (220, 140), 2)
    pygame.draw.line(screen, BLACK, (220, 140), (240, 150), 2)

    # -------------------------------
    # BIRDS - FLOCK
    # -------------------------------
    for x in range(100, 700, 120):  # start at 100, end near 700, step 120
        y = 140 + (x % 60)          # small vertical variation
        pygame.draw.line(screen, BLACK, (x, y), (x + 20, y - 10), 2)
        pygame.draw.line(screen, BLACK, (x + 20, y - 10), (x + 40, y), 2)

    # --------------------------------
    # BIRDS - DISTANT FLOCK
    # --------------------------------
    for x in range(50, 750, 150):
        y = 100
        pygame.draw.line(screen, BLACK, (x, y), (x + 15, y - 8), 1)
        pygame.draw.line(screen, BLACK, (x + 15, y - 8), (x + 30, y), 1)

    # ------------------------------
    # STARS (twinkle effect)
    # ------------------------------
    for star in stars:
        x, y, size, timer = star

        # Twinkle occationally
        if timer == 0:
            size = random.randint(1, 3)       # brief brightness change
            star[2] = size                    # update size
            star[3] = random.randint(10, 40)  # reset timer

        else:
            star[3] -= 1  # countdown

        pygame.draw.circle(screen, WHITE, (x, y), size)

    # -------------------------------
    # (optional) Sun Glow (soft halo)
    # -------------------------------
    pygame.draw.circle(screen, (255, 255, 120), (400, 300), 70)

    # -------------------------------
    # ISLAND
    # -------------------------------
    pygame.draw.ellipse(screen, ISLAND_SAND, (600, 520, 150, 40))

    # -------------------------------
    # PALM TREE 1
    # -------------------------------
    # Trunk
    pygame.draw.rect(screen, PALM_TRUNK, (650, 470, 10, 60))

    # Leaves
    pygame.draw.line(screen, PALM_LEAF, (655, 470), (630, 450), 4)
    pygame.draw.line(screen, PALM_LEAF, (655, 470), (680, 450), 4)
    pygame.draw.line(screen, PALM_LEAF, (655, 470), (655, 445), 4)
    pygame.draw.line(screen, PALM_LEAF, (655, 470), (640, 460), 4)
    pygame.draw.line(screen, PALM_LEAF, (655, 470), (670, 460), 4)

    # -----------------------------------
    # PALM TREE 2
    # -----------------------------------
    # Trunk
    pygame.draw.rect(screen, PALM_TRUNK, (700, 480, 8, 50))

    # Leaves
    pygame.draw.line(screen, PALM_LEAF, (704, 480), (685, 460), 3)
    pygame.draw.line(screen, PALM_LEAF, (704, 480), (723, 460), 3)
    pygame.draw.line(screen, PALM_LEAF, (704, 480), (704, 455), 3)
    pygame.draw.line(screen, PALM_LEAF, (704, 480), (690, 470), 3)
    pygame.draw.line(screen, PALM_LEAF, (704, 480), (718, 470), 3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

