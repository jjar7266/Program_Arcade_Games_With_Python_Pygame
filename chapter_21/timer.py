"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

Coded (2026) along by: Jose 'Joe' Ruiz

Chapter 21: Formatting

timer.py
"""

# Import
import pygame

# CONSTANTS
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

SCREEN_WIDTH  = 700
SCREEN_HEIGHT = 500
FPS           = 60

COUNTDOWN_START = 90  # seconds

# Initialize Pygame
pygame.init()

# Create the display window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Modern Timer Example")

clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

# Helper Functions
def format_time(total_seconds: int) -> str:
    """
    Convert seconds -> MM:SS string with leading zeros.
    """
    minutes  = total_seconds // 60
    seconds  = total_seconds % 60
    return "{:02}:{:02}".format(minutes, seconds)


def draw_centered_text(surface, text, y_pos, color=BLACK):
    """
    Render text and center it horizontally at the given y-position.
    """
    rendered = font.render(text, True, color)
    rect = rendered.get_rect(center=(SCREEN_WIDTH // 2, y_pos))
    surface.blit(rendered, rect)


# Main Loop
def main():
    frame_count = 0
    running = True

    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Background ---
        screen.fill(WHITE)

        # ================================================
        # COUNT-UP TIMER
        # ================================================
        elapsed_seconds = frame_count // FPS
        up_string = f"Time: {format_time(elapsed_seconds)}"

        # Center at 40% of screen height
        draw_centered_text(screen, up_string, SCREEN_HEIGHT * 0.40)

        # =================================================
        # COUNTDOWN TIMER
        # =================================================
        remaining_seconds = max(COUNTDOWN_START - elapsed_seconds, 0)
        down_string = f"Time left: {format_time(remaining_seconds)}"

        # Center at 55% of screen height
        draw_centered_text(screen, down_string, SCREEN_HEIGHT * 0.55)

        # Frame update
        frame_count += 1
        clock.tick(FPS)
        pygame.display.flip()

    pygame.quit()


# Entry Point
if __name__ == "__main__":
    main()




