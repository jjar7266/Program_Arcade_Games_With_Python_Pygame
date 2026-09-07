"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 20: Recursion

example that draws a rectangle, and recursively keeps drawing rectangles
inside of it. Each rectangle is 20% smaller than the parent rectangle.

recursive_rectangles.py
"""
# Import modules
import pygame

# COLORS
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)


# -----------------------------------------------------------------
# Recursive Drawing Function
# -----------------------------------------------------------------
def recursive_draw(screen, x, y, width, height):
    """
    Draw a rectangle, then draw a smaller rectangle inside it.

    Think of this like stacking boxes inside each other:
    - First we draw the big box.
    - Then we shrink the box a little.
    - Then we draw the smaller box.
    - We keep shrinking and drawing until the box is too small.

    This is recursion: the function calls itself to keep going.
    """

    # Draw the current rectangle outline
    pygame.draw.rect(
        screen,
        BLACK,
        pygame.Rect(x, y, width, height),
        1  # outline only
    )

    # Is the rectangle is still big enough, draw another inside it
    if(width > 14):
        # Move inward by 10% of the size
        x += width * 0.1
        y += height * 0.1

        # Shrink the rectangle to 80% of its size
        width *= 0.8
        height *= 0.8

        # Call this function again with the new smaller rectangle
        recursive_draw(screen, x, y, width, height)


# -----------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------

def main():
    """ Main game loop that draws recursive rectangles. """

    pygame.init()

    # Set the height and width of the screen
    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Recursive Rectangles")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # ---------- Main Program Loop ----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Fill the background with white
        screen.fill(WHITE)

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

        # Draw the first (largest) rectangle
        recursive_draw(screen, 0, 0, 700, 500)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.

        # Update the screen with what we've drawn
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)

    # Be IDLE friendly. If you forget this line, the program will 'hang' on exit.
    pygame.quit()


# --------------------------------------------------------------
# Run Program
# --------------------------------------------------------------
if __name__ == "__main__":
    main()
