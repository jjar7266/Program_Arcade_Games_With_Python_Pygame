"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 11: Controllers and Graphics

lab_10_user_control.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import pygame
import random
from pathlib import Path


# Initialize Pygame
pygame.init()


# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)


# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Lab 10 - User Control")


# Hide the mouse cursor
pygame.mouse.set_visible(False)


# Base directory for assets
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"


# --- Load PNG assets ---
spaceship_img = pygame.image.load(ASSETS_DIR / "spaceship.png").convert_alpha()
alien_img = pygame.image.load(ASSETS_DIR / "alien_02.png").convert_alpha()
asteroid_img = pygame.image.load(ASSETS_DIR / "asteroid.png").convert_alpha()


# --- Joystick Setup

if pygame.joystick.get_count() > 0:
      joystick = pygame.joystick.Joystick(0)
      print("Controller detected:", joystick.get_name())
else:
      joystick = None
      print("No controller detected.")


# Ship starting positions
x_key   = 100
y_key   = 250

x_mouse = 350
y_mouse = 250

x_joy   = 600
y_joy   = 250


# Drawing function
def draw_keyboard_ship(screen, x, y):
      """ Draw the keyboard-controlled spaceship. """
      screen.blit(spaceship_img, (x, y))


def draw_mouse_ship(screen, x, y):
      """ Draw the mouse-controlled alien ship."""
      screen.blit(alien_img, (x, y))


def draw_controller_ship(screen, x, y):
      """ Draw the controller-controlled asteroid. """
      screen.blit(asteroid_img, (x, y))


# Create an empty array
star_list = []

for i in range(50):
            x = random.randrange(0, 800)
            y = random.randrange(0, 600)
            star_list.append([x, y])

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# ------ Main Program Loop ------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should be here (movement, input, updates)

    # --- Keyboard movement for spaceship ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_key -= 5
    if keys[pygame.K_RIGHT]:
        x_key += 5
    if keys[pygame.K_UP]:
        y_key -= 5
    if keys[pygame.K_DOWN]:
        y_key += 5

    # --- Boundary checks for keyboard ship ---
    if x_key < 0:
          x_key = 0
    if x_key > 800 - spaceship_img.get_width():
          x_key = 800 - spaceship_img.get_width()

    if y_key < 0:
          y_key = 0
    if y_key > 600 - spaceship_img.get_height():
          y_key = 600 - spaceship_img.get_height()


    # --- Mouse movement for alien ship ---
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clamp mouse position BEFORE assigning to ship
    mouse_x = max(0, min(mouse_x, 800 - alien_img.get_width()))
    mouse_y = max(0, min(mouse_y, 600 - alien_img.get_height()))

    x_mouse = mouse_x
    y_mouse = mouse_y

    # --- Controller movement for asteroid ship ---
    if joystick:
          axis_x = joystick.get_axis(0)   # left stick horizontal
          axis_y = joystick.get_axis(1)   # left stick vertical

          x_joy += axis_x * 5
          y_joy += axis_y * 5

    # --- Boundary checks for controller ship
    if x_joy < 0:
          x_joy = 0
    if x_joy > 800 - asteroid_img.get_width():
          x_joy = 800 - asteroid_img.get_width()

    if y_joy < 0:
          y_joy = 0
    if y_joy > 600 - asteroid_img.get_height():
          y_joy = 600 - asteroid_img.get_height()


    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing
    # the background image.
    screen.fill(BLACK)

    for item in star_list:

            # Create falling stars
            item[1] += 1
            pygame.draw.circle(screen, WHITE, item, 2)

            if item[1] > 600:
                  item[1] = random.randrange(-20, -5)
                  item[0] = random.randrange(800)

    # --- Drawing code should go here

    draw_keyboard_ship(screen, x_key, y_key)

    draw_mouse_ship(screen, x_mouse, y_mouse)

    draw_controller_ship(screen, x_joy, y_joy)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit:
pygame.quit()


