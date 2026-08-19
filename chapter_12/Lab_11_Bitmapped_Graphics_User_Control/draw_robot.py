"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 12: Bitmapped Graphics and Sound

Lab 11: Bitmapped Graphics and User Control

Standalone robot demo:
  - Draws a custom iRobot using pygame.draw
  - Includes bitmapped graphics (background)
  - Includes sound (keypress)
  - Allows keyboard control of the robot

draw_robot.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Import modules
import pygame
from pathlib import Path

# --------------------------------------------------------------------
# CONSTANTS (safe globals)
# --------------------------------------------------------------------
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

# Base directory for assets
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_DIR = BASE_DIR / "images"
SOUND_DIR = BASE_DIR / "sounds"


# ----------------------------------------------------------------------
# DRAW FUNCTION - REQUIRED BY LAB 11
# ----------------------------------------------------------------------
def draw_iRobot(screen, x, y):
    """
    Draw a simple iRobot-style robot using pygame.draw commands.
    The (x, y) position represents the TOP-LEFT corner of the robot.
    """

    # --- BODY ---
    body_width = 80
    body_height = 100
    body_rect = pygame.Rect(x, y + 40, body_width, body_height)
    pygame.draw.rect(screen, (180, 180, 180), body_rect, border_radius=12)

    # --- HEAD ---
    head_width = 60
    head_height = 50
    head_rect = pygame.Rect(x + 10, y, head_width, head_height)
    pygame.draw.rect(screen, (200, 200, 200), head_rect, border_radius=12)

    # --- EYES ---
    pygame.draw.circle(screen, BLACK, (x + 25, y + 25), 6)
    pygame.draw.circle(screen, BLACK, (x + 45, y + 25), 6)

    # --- MOUTH ---
    pygame.draw.rect(screen, (50, 50, 50), (x + 25, y + 40, 30, 6), border_radius=3)

    # --- ARMS ---
    pygame.draw.rect(screen, (160, 160, 160), (x - 15, y + 55, 15, 60), border_radius=8)
    pygame.draw.rect(screen, (160, 160, 160), (x + body_width, y + 55, 15, 60), border_radius=8)

    # --- LEGS ---
    pygame.draw.rect(screen, (140, 140, 140), (x + 10, y + 140, 20, 40), border_radius=6)
    pygame.draw.rect(screen, (140, 140, 140), (x + 50, y + 140, 20, 40), border_radius=6)


# -------------------------------------------------------------------
# MAIN PROGRAM
# -------------------------------------------------------------------
def main():
    pygame.init()
    pygame.mixer.init()

    # Window Setup
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Lab 11: iRobot Demo")

    clock = pygame.time.Clock()
    done = False

    # Load background image
    background_path = IMAGE_DIR / "saturn_family1.jpg"
    background_image = pygame.image.load(background_path).convert_alpha()
    background_image = pygame.transform.smoothscale(background_image, size)

    # Load sound
    beep_path = SOUND_DIR / "laser5.ogg"
    beep_sound = pygame.mixer.Sound(str(beep_path))

    # Robot starting position
    robot_x = 350
    robot_y = 250
    robot_speed = 5

    # ---------- Main Loop ----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.KEYDOWN:
                beep_sound.play()

        # Keyboard control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            robot_x -= robot_speed

        if keys[pygame.K_RIGHT]:
            robot_x += robot_speed

        if keys[pygame.K_UP]:
            robot_y -= robot_speed

        if keys[pygame.K_DOWN]:
            robot_y += robot_speed

        # Drawing
        screen.blit(background_image, (0, 0))
        draw_iRobot(screen, robot_x, robot_y)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


# ---------------------------------------------------------------
# ENTRY POINT
# ---------------------------------------------------------------
if __name__ == "__main__":
    main()







