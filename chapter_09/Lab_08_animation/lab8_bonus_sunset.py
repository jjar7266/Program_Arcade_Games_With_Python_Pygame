"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose "Joe" Ruiz

Chapter 9: Introduction to Animation

lab_8_bonus_sunset.py

Description:
    This file is the bonus-phase extension of my Lab 8 project.
    It builds on the animated sunset scene from Chapter 6: Lab 5
    and adds advanced animation effects such as a sinking sun,
    sky color transition, night fade-in, and twinkling stars.
    This version is not the official Lab 8 submission, but an
    enhanced cinematic version created for additional practice
    and creative exploration.
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

# --------------------------------------------------------------
# BONUS PHASE ANIMATION VARIABLES
# --------------------------------------------------------------

# Sun animation
sun_y = 300
sun_speed = 0.15

# Sky fade values (start bright)
sky_blue_alpha = 255
peach_alpha    = 255
orange_alpha   = 255

# Night fade-in
night_alpha    = 0

# Stars (generated once)
stars = []
for _ in range(40):
    x = random.randint(0, 800)
    y = random.randint(0, 200)
    size = random.randint(0, 200)
    twinkle = random.randint(0, 20)
    stars.append([x, y, size, twinkle])

# Main loop function
# This function holds our animation logic and all drawing code.
def main():
    done = False
    clock = pygame.time.Clock()
    # --------------------------------------------------------------
    # BONUS PHASE ANIMATION VARIABLES
    # --------------------------------------------------------------

    # Sun animation
    sun_y = 300
    sun_speed = 0.15

    # Sky fade values (start bright)
    sky_blue_alpha = 255
    peach_alpha    = 255
    orange_alpha   = 255

    # Night fade-in
    night_alpha    = 0

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


# Main loop function
# This function holds our animation logic and all drawing code.
def main():
    done = False
    clock = pygame.time.Clock()

    # --------------------------------------------------------------
    # BONUS PHASE ANIMATION VARIABLES
    # --------------------------------------------------------------
    # These variables control the sunset → night transition.
    # They are initialized once at the start of the program.

    # Sun animation
    sun_y = 300              # starting height of the sun
    sun_speed = 0.15         # how fast the sun sinks each frame

    # Sky fade values (start bright)
    # These represent the alpha (transparency) of each sky layer.
    # As the sun sinks, these values decrease, causing the sky to fade.
    sky_blue_alpha = 255     # top sky layer (brightest)
    peach_alpha    = 255     # middle sky layer
    orange_alpha   = 255     # lower sky layer

    # Night fade-in
    # This controls the dark blue overlay that gradually appears.
    night_alpha    = 0       # starts invisible, becomes opaque at night

    # Sun fade-out alpha (starts fully visible)
    # As night_alpha increases, sun_alpha decreases.
    sun_alpha = 255

    # --------------------------------------------------------------
    # BIRD ANIMATION VARIABLES
    # --------------------------------------------------------------
    # These control the movement and wing flapping of the bird.
    bird_x = 200             # horizontal position
    bird_y = 150             # vertical position (constant)
    bird_speed = 2           # how fast the bird moves horizontally

    wing_offset = 0          # how far the wing tip moves up/down
    wing_direction = 1       # +1 = wing going up, -1 = wing going down

    # --------------------------------------------------------------
    # WAVE OFFSETS (PARALLAX EFFECT)
    # --------------------------------------------------------------
    # Each wave row moves at a different speed to create depth.
    wave_offset1 = 0         # fastest waves (closest)
    wave_offset2 = 0         # medium waves
    wave_offset3 = 0         # slowest waves (farthest)

    # --------------------------------------------------------------
    # STAR FIELD (generated once)
    # --------------------------------------------------------------
    # Stars are stored as [x, y, size, twinkle_timer].
    # Twinkle timer controls when a star changes size.
    stars = []
    for _ in range(40):
        x = random.randint(0, 800)
        y = random.randint(0, 200)
        size = random.randint(1, 2)
        twinkle = random.randint(0, 20)
        stars.append([x, y, size, twinkle])

    # --------------------------------------------------------------
    # MAIN LOOP
    # --------------------------------------------------------------
    # This loop runs 60 times per second.
    # Each cycle:
    #   1. Handles events (like closing the window)
    #   2. Updates animation variables (movement, fading, timing)
    #   3. Draws the entire scene using the updated values
    # --------------------------------------------------------------
    while not done:

        # ----------------------------------------------------------
        # EVENT HANDLING
        # ----------------------------------------------------------
        # This checks for user actions such as closing the window.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----------------------------------------------------------
        # ANIMATION UPDATES (ALL UPDATES MUST HAPPEN BEFORE DRAWING)
        # ----------------------------------------------------------
        # This section updates positions, alpha values, and timers.
        # Drawing happens AFTER this so the screen always shows
        # the newest animation state.

        # -----------------------------
        # Bird movement across the sky
        # -----------------------------
        bird_x += bird_speed

        # Reset bird when it flies off the right side
        # This creates a looping flight animation.
        if bird_x > 850:
            bird_x = -50

        # -----------------------------
        # Wing flapping animation
        # -----------------------------
        # wing_offset moves up/down to simulate flapping.
        wing_offset += wing_direction

        # Reverse direction when reaching flap limits.
        # Wings flap between -10 (down) and +10 (up).
        if wing_offset > 10:
            wing_direction = -1
        if wing_offset < -10:
            wing_direction = 1

        # ----------------------------------------------------------
        # SUNSET ANIMATION (UPDATE LOGIC)
        # ----------------------------------------------------------
        # The sun slowly sinks toward the horizon.
        sun_y += sun_speed

        # Fade sky colors once the sun reaches a certain height.
        # Each layer fades at a slightly different rate.
        if sun_y > 320:
            sky_blue_alpha = max(0, sky_blue_alpha - 0.3)
            peach_alpha    = max(0, peach_alpha    - 0.25)
            orange_alpha   = max(0, orange_alpha   - 0.2)

        # Fade in the night sky overlay.
        # night_alpha increases from 0 → 255.
        if sun_y > 300:
            night_alpha = min(255, night_alpha + 0.4)

        # Fade the sun itself (sun disappears at full night)
        # As night_alpha increases, sun_alpha decreases.
        sun_alpha = max(0, 255 - night_alpha)

        # Sink sun below horizon
        # Once the sun reaches the ocean line, stop it.
        if sun_y > 480:
            sun_y = 480

        # ----------------------------------------------------------
        # WAVE MOVEMENT (PARALLAX EFFECT)
        # ----------------------------------------------------------
        # Each wave row moves at a different speed to create depth.
        wave_offset1 = (wave_offset1 + 1.5) % 40
        wave_offset2 = (wave_offset2 + 1) % 40
        wave_offset3 = (wave_offset3 + 0.5) % 40

        # ----------------------------------------------------------
        # DRAWING SECTION
        # ----------------------------------------------------------
        # Everything drawn below uses the UPDATED animation values.
        # This ensures smooth movement and proper timing.

        # ----------------------------------------------------------
        # SKY GRADIENT WITH FADING COLORS
        # ----------------------------------------------------------
        # We use temporary surfaces with alpha values so the sky
        # can fade smoothly as the sun sets.
        sky_top = pygame.Surface((800, 200), pygame.SRCALPHA)
        sky_mid = pygame.Surface((800, 200), pygame.SRCALPHA)
        sky_low = pygame.Surface((800, 150), pygame.SRCALPHA)
        night_sky = pygame.Surface((800, 600), pygame.SRCALPHA)

        # Fill each sky layer with its color and current alpha.
        sky_top.fill((*SKY_BLUE, int(sky_blue_alpha)))
        sky_mid.fill((*PEACH, int(peach_alpha)))
        sky_low.fill((*ORANGE, int(orange_alpha)))

        # Night sky overlay (dark blue)
        night_sky.fill((10, 10, 40, int(night_alpha)))

        # Draw the sky layers
        screen.blit(sky_top, (0, 0))
        screen.blit(sky_mid, (0, 200))
        screen.blit(sky_low, (0, 350))
        screen.blit(night_sky, (0, 0))  # overlay on top

        # ----------------------------------------------------------
        # OCEAN (drawn after night overlay so it stays visible)
        # ----------------------------------------------------------
        pygame.draw.rect(screen, OCEAN_BLUE, (0, 500, 800, 100))

        # ----------------------------------------------------------
        # SUN (SINKING + FADING)
        # ----------------------------------------------------------
        # We draw the sun on a temporary surface so we can apply alpha.
        if sun_alpha > 0:
            sun_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
            pygame.draw.circle(
                sun_surface,
                (255, 255, 0, int(sun_alpha)),   # yellow with fading alpha
                (400, int(sun_y)),
                50
            )
            screen.blit(sun_surface, (0, 0))

            # Glow fades with sun
            glow_surface = pygame.Surface((800, 600), pygame.SRCALPHA)
            pygame.draw.circle(
                glow_surface,
                (255, 255, 150, int(sun_alpha * 0.6)),  # softer glow
                (400, int(sun_y)),
                80
            )
            screen.blit(glow_surface, (0, 0))

        # ----------------------------------------------------------
        # STARS (APPEAR + TWINKLE)
        # ----------------------------------------------------------
        # Stars only appear once the night sky is dark enough.
        for star in stars:
            x, y, size, timer = star

            # Twinkle effect: stars randomly change size.
            if timer == 0:
                size = random.randint(1, 3)
                star[2] = size
                star[3] = random.randint(10, 40)
            else:
                star[3] -= 1

            if night_alpha > 50:
                pygame.draw.circle(screen, WHITE, (x, y), size)

        # ----------------------------------------------------------
        # WAVES (3 ROWS)
        # ----------------------------------------------------------
        # Each row uses a different offset to create depth.
        for i in range(0, 800, 40):
            pygame.draw.arc(screen, WHITE, (i + wave_offset1, 520, 40, 20), 0, 3.14, 2)

        for i in range(8, 800, 40):
            pygame.draw.arc(screen, WHITE, (i + 20 + wave_offset2, 540, 40, 20), 0, 3.14, 2)

        for i in range(0, 800, 40):
            pygame.draw.arc(screen, WHITE, (i + 10 + wave_offset3, 560, 30, 15), 0, 3.14, 1)

        # ----------------------------------------------------------
        # ISLAND + PALM TREES
        # ----------------------------------------------------------
        pygame.draw.ellipse(screen, ISLAND_SAND, (600, 520, 150, 40))

        pygame.draw.rect(screen, PALM_TRUNK, (650, 470, 10, 60))
        pygame.draw.line(screen, PALM_LEAF, (655, 470), (620, 445), 4)
        pygame.draw.line(screen, PALM_LEAF, (655, 470), (690, 445), 4)
        pygame.draw.line(screen, PALM_LEAF, (655, 470), (655, 435), 4)

        pygame.draw.rect(screen, PALM_TRUNK, (700, 480, 8, 50))
        pygame.draw.line(screen, PALM_LEAF, (704, 480), (685, 460), 3)
        pygame.draw.line(screen, PALM_LEAF, (704, 480), (723, 460), 3)
        pygame.draw.line(screen, PALM_LEAF, (704, 480), (704, 455), 3)

        # ----------------------------------------------------------
        # BIRD (ANIMATED WINGS)
        # ----------------------------------------------------------
        # The middle point of the wings moves up/down using wing_offset.
        pygame.draw.line(screen, BLACK,
                         (bird_x, bird_y),
                         (bird_x + 20, bird_y - 10 + wing_offset), 2)

        pygame.draw.line(screen, BLACK,
                         (bird_x + 20, bird_y - 10 + wing_offset),
                         (bird_x + 40, bird_y), 2)

        # ----------------------------------------------------------
        # FINAL DISPLAY UPDATE
        # ----------------------------------------------------------
        pygame.display.flip()
        clock.tick(60)



if __name__ == "__main__":
    main()

