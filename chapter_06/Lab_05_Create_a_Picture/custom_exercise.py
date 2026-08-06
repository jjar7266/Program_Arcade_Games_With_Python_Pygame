"""
Custom Exercise: Loop Practice (Not part of the book)

Created by: Jose "Joe" Ruiz
Date: 2026

Description:
   This file contains small practice examples to help understand how
   for-loops work before using them in Pygame graphics. These exercises
   were created to build intuition for iteration and offsets, and are
   not included in the Program Arcade Games book.
"""
# --------------------------
# Step 1: Simple for loop
# --------------------------

for i in range(5):
    print("i is:", i)

print("Done.")


# ----------------------------
# Step 2: Using i as an offset
# ----------------------------

for i in range(5):
    x = 10 + i * 20
    print(f"Box {i} starts at x =", x)


# ----------------------------
# Step 3: Minimal Pygame Window
# ----------------------------

# Import modules
import pygame

# Initialize Pygame
pygame.init()

# Create a display Window
size = (800, 600)
screen = pygame.display.set_mode(size)

# COLORS
BLACK  = (  0,   0,   0)
PURPLE = (200, 100, 255)
GRAY   = (150, 150, 150)
YELLOW = (255, 255, 100)

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    # Draw 10 circles in a row
    for i in range(10):
        x = 50 + i * 60  # moves right each time
        y = 300          # stays centered vertically
        pygame.draw.circle(screen, PURPLE, (x, y), 20)

    # Draw repeating lamp posts
    for i in range(6):
        x = 100 + i * 120

        # Pole
        pygame.draw.rect(screen, GRAY, (x, 350, 20, 150))

        # Lamp head
        pygame.draw.circle(screen, YELLOW, (x + 10, 340), 20)

    pygame.display.flip()

pygame.quit()

