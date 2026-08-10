"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 9: Introduction to Animation

lab_8_animation.py

Description:
    This program is my lab 8 submission. It takes the sunset scene from
    Chapter 6: Lab 5 and adds animation. The goal is to demonstrate movement,
    timing, and creative flair using Pygame's drawing and update loop.
"""

# Import modules
# pygame -> handles graphics, window, drawing, animation
# random -> used later for any random movement or flair effects
import pygame
import random

# Initialize Pygame
# This activates all the internal systems Pygame needs (graphics, events, etc.)
pygame.init()

# Create the display window
# This sets the size of our game window and gives it a title.
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lab 8 - Animation")

# Color constants
WHITE       = (255, 255, 255)  # waves and stars
BLACK       = (  0,   0,   0)  # birds

# Sky gradient colors
SKY_BLUE    = (135, 206, 235)
PEACH       = (255, 209, 148)
ORANGE      = (255, 179,  71)

# Ocean
OCEAN_BLUE  = ( 30, 144, 255)

# Sun glow
SUN_YELLOW  = (255, 255,   0)

# Island + palm trees
ISLAND_SAND = (160, 120,  60)
PALM_TRUNK  = (101,  67,  33)
PALM_LEAF   = ( 34, 139,  34)



# Main loop function
# This function holds our animation logic and all drawing code.
def main():
    done = False
    clock = pygame.time.Clock()

    # Animation variables
    # These control movement for our first animated object: the main bird.
    bird_x = 200      # starting horizontal position
    bird_y = 150      # vertical position stays constant for now
    bird_speed = 2    # how many pixels the bird moves each frame

    wing_offset = 0
    wing_direction = 1

    wave_offset1 = 0  # top row (fastest)
    wave_offset2 = 0  # middle row (medium)
    wave_offset3 = 0  # bottom row (slowest)


    # Main loop
    while not done:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # -----------------------------
        # Animation updates
        # -----------------------------
        # Move the main bird across the sky
        bird_x += bird_speed

        # Reset bird when it flies off the right side
        if bird_x > 850:
            bird_x = -50

        # Animate wing flapping
        # wing_offset moves up/down each frame to create a flap motion
        wing_offset += wing_direction

        # Reverse direction when reaching flap limits
        # Wings flap between -10 (down) and +10 (up).
        if wing_offset > 10:
            wing_direction = -1

        if wing_offset < -10:
            wing_direction = 1

        # -----------------------
        # Drawing section
        # -----------------------
        # Draw sky gradient
        # We draw three rectangles from top to bottom to create a sunset gradient.
        pygame.draw.rect(screen, SKY_BLUE, (0, 0, 800, 200))   # top sky
        pygame.draw.rect(screen, PEACH,    (0, 200, 800, 200)) # middle sky
        pygame.draw.rect(screen, ORANGE,   (0, 350, 800, 150)) # lower sky

        # Draw ocean
        # A solid rectangle for the water area.
        pygame.draw.rect(screen, OCEAN_BLUE, (0, 500, 800, 100))

        # ----------------------------------------------------------
        # WAVES (ANIMATED WITH DIFFERENT SPEEDS)
        # ----------------------------------------------------------
        # Each wave row gets its own offset so they move at different
        # speeds. This creates a parallax effect: closer waves move
        # faster, distant waves move slower.
        #
        # wave_offset1 = fastest (top row)
        # wave_offset2 = medium  (middle row)
        # wave_offset3 = slowest (bottom row)
        #
        # All offsets loop every 40 pixels because each wave repeats
        # every 40 pixels horizontally.
        wave_offset1 = (wave_offset1 + 1.5) % 40   # fastest
        wave_offset2 = (wave_offset2 + 1) % 40   # medium
        wave_offset3 = (wave_offset3 + 0.5) % 40 # slowest

        # ------------------------------------------------------------
        # WAVES - ROW 1 (main wave, fastest)
        # ------------------------------------------------------------
        # These are the largest waves. They sit highest in the water.
        # Each wave is drawn as the top half of a circle (an arc).
        for i in range(0, 800, 40):
            pygame.draw.arc(
                screen,
                WHITE,
                (i + wave_offset1, 520, 40, 20),    # x shifted by wave_offset
                0,
                3.14,                              # top half of circle
                2
            )

        # --------------------------------------------------------------
        # WAVES - ROW 2 (offset row, medium speed)
        # --------------------------------------------------------------
        # This row is shifted right by +20 and down by +20 to create
        # a staggered pattern. It adds depth and makes the ocean look
        # more natural.
        for i in range(8, 800, 40):
            pygame.draw.arc(
                screen,
                WHITE,
                (i + 20 + wave_offset2, 540, 40, 20),
                0,
                3.14,
                2
            )

        # ----------------------------------------------------------------
        # WAVES - ROW 3 (small waves, slowest)
        # ----------------------------------------------------------------
        # These smaller arcs add fine detail to the water. They sit
        # lowest and move with the same offset for consistency.
        for i in range(0, 800, 40):
            pygame.draw.arc(
                screen,
                WHITE,
                (i + 10 + wave_offset3, 560, 30, 15),
                0,
                3.14,
                1
            )






        # ---------------------
        # ISLAND
        # ---------------------
        # A simple oval shape for the sandy island.
        pygame.draw.ellipse(screen, ISLAND_SAND, (600, 520, 150, 40))

        # ----------------------
        # PALM TREE 1
        # ----------------------
        # Trunk (center-left on the island)
        pygame.draw.rect(screen, PALM_TRUNK, (650, 470, 10, 60))

        # Leaves for palm tree 1
        pygame.draw.line(screen, PALM_LEAF, (655, 470), (620, 445), 4) # left
        pygame.draw.line(screen, PALM_LEAF, (655, 470), (690, 445), 4) # right
        pygame.draw.line(screen, PALM_LEAF, (655, 470), (655, 435), 4) # top


        # ----------------------
        # PALM TREE 2
        # ----------------------
        # Trunk (smaller, slightly right)
        pygame.draw.rect(screen, PALM_TRUNK, (700, 480, 8, 50))

        # Leaves for palm tree 2
        pygame.draw.line(screen, PALM_LEAF, (704, 480), (685, 460), 3) # Left
        pygame.draw.line(screen, PALM_LEAF, (704, 480), (723, 460), 3) # right
        pygame.draw.line(screen, PALM_LEAF, (704, 480), (704, 455), 3) # top

        # Draw the bird using updated animation variables
        # The middle point of the wings moves up/down using wing_offset.
        pygame.draw.line(
            screen,
            BLACK,
            (bird_x, bird_y),                          # bird body start
            (bird_x + 20, bird_y - 10 + wing_offset),  # wing tip (animated)
            2
        )

        pygame.draw.line(
            screen,
            BLACK,
            (bird_x + 20, bird_y - 10 + wing_offset),  # wing tip (animated)
            (bird_x + 40, bird_y),
            2
        )



        pygame.display.flip()
        clock.tick(60)

main()
pygame.quit()



