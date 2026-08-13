"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 11: Controllers and Graphics

move_game_controller.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

import pygame

# ------------------------------------------------------------------
# TEACHER MODE:
# These are CONSTANTS - values that NEVER change.
# Constants are the ONLY type of global that is safe.
# They make your code readable and avoid magic numbers.
#
# STUDENT MODE (OH WOW I GET IT):
# ohhhh... constants can live at the top of the file because
# they never change. They aren't "evil globals" - they're
# just shared settings the whole program can use safely.
# --------------------------------------------------------------------

# Define some colors as global constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

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

def main():
    """ Main function for the game. """

    # -------------------------------------------------------------
    # TEACHER MODE:
    # Putting pygame.init() INSIDE main() is proper architecture.
    # It prevents accidental execution when this file is imported.
    # It keeps initialization controlled and avoids global side effects.
    #
    # STUDENT MODE (OH WOW I GET IT):
    # Ohhh... so pygame.init() shouldn't run automatically when
    # the file loads. Putting it in main() means it only runs
    # when I CALL main(). This is how real Python programs work.
    # --------------------------------------------------------------
    pygame.init()

    # --- Joystick Setup (modern Pygame) ---
    joystick_count = pygame.joystick.get_count()
    if joystick_count > 0:
        my_joystick = pygame.joystick.Joystick(0)
        print("Controller ready:", my_joystick.get_name())
    else:
        my_joystick = None
        print("No controller detected.")

    # Starting position
    x_coord = 10
    y_coord = 10

    # Initialize last axis values for debug comparison
    last_horiz = 0.0
    last_vert  = 0.0

    # Set the width and height of the screen [width, height]
    size = [700, 500]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("My Game")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop ----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.ACTIVEEVENT:
                 if event.gain == 1 and event.state == 1:
                      pygame.display.set_mode(size)

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # As long as there is a joystick
        if my_joystick is not None:

            # This gets the position of the axis on the game controller
            # It returns a number between -1.0 and +1.0
            horiz_axis_pos = my_joystick.get_axis(0)
            vert_axis_pos  = my_joystick.get_axis(1)

            # DEBUG PRINT - Only print when the value changes enough to matter
            if abs(horiz_axis_pos - last_horiz) > 0.05 or abs(vert_axis_pos - last_vert) > 0.05:
                        print(f"Horiz: {horiz_axis_pos:.3f} Vert: {vert_axis_pos:.3f}")
                        last_horiz = horiz_axis_pos
                        last_vert  = vert_axis_pos

            # Move x according to the axis. We multiply by 10
            # to speed up the movement.
            x_coord = x_coord + int(horiz_axis_pos * 10)
            y_coord = y_coord + int(vert_axis_pos * 10)

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # Draw the item at the proper coordinates
        draw_stick_figure(screen, x_coord, y_coord)

        # ALL CODE TO DRAW SHOLD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Close the window and quit.
    # If you forget this line, the program with 'hang'
    # on exit if running from IDLE.
    pygame.quit()

# ------------------------------------------------------------------
# TEACHER MODE:
# This is the official Python entry point:
# It ensures main() only runs when THIS file is executed directly.
# If another file imports this one, main() with NOT run.
#
# STUDENT MODE (OH WOW I GET IT):
# Ohhh... so THIS is why Python programs use main().
# It prevents accidental execution and makes the file reusable.
# --------------------------------------------------------------------
if __name__ == "__main__":
    main()



