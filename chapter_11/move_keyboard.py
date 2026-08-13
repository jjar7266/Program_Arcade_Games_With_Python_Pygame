"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 11: Controllers and Graphics - Keyboard

move_keyboard.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=LKOyJSc6Z1c

# Import modules
import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
WHITE = [255, 255, 255]
BLACK = [  0,   0,   0]
GREEN = [  0, 255,   0]
RED   = [255,   0,   0]

# Set the height and width of the screen
size = [400, 500]
screen = pygame.display.set_mode(size)

# Function that always draws a stickfigure in the same place

def draw_stick_figure(screen, x, y):
    """
    (x, y) is the center of the head.
    """

    # --- Head ---
    # Slightly larger head for better visibility
    pygame.draw.ellipse(screen, BLACK, [x - 7, y - 7, 14, 14])

    # --- Body ---
    # Longer torso for better proportions
    pygame.draw.line(screen, RED,
                     [x, y + 7],      # bottom of head
                     [x, y + 27],     # waist
                     3)

    # --- Arms ---
    # Arms angled outward from upper torso
    pygame.draw.line(screen, RED,
                     [x, y + 12],     # shoulder
                     [x + 10, y + 22],# right hand
                     2)
    pygame.draw.line(screen, RED,
                     [x, y + 12],     # shoulder
                     [x - 10, y + 22],# left hand
                     2)

    # --- Legs ---
    # Legs start at waist and angle outward
    pygame.draw.line(screen, BLACK,
                     [x, y + 27],     # waist
                     [x + 8, y + 42], # right foot
                     3)
    pygame.draw.line(screen, BLACK,
                     [x, y + 27],     # waist
                     [x - 8, y + 42], # left foot
                     3)


# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
x_coord = 10
y_coord = 10

# ---------- Main Program Loop ----------
while not done:

    # --- Event Processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            # Figure out if is was an arrow key.
            # if so adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0


    # --- Game Logic ---

    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed

    # --- Drawing Code ---

    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_stick_figure(screen, x_coord, y_coord)

    # Go ahead and update the screen with what we've drawn
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()


