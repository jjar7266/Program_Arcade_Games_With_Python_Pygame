"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) by: Jose 'Joe' Ruiz

Chapter 14: Lab 13 - Sprite Collecting

sprite_moving.py
=========================================================================
"""
# Import modules
import pygame
import random
from block_library import Block
from goodblock_library import GoodBlock
from badblock_library import BadBlock
from pathlib import Path


# -------------------------------------------------------------------
# Initialize Pygame and the mixer
# -------------------------------------------------------------------
pygame.init()
pygame.mixer.init()

# Set the height and width of the screen
screen_width  = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Chapter 14: Lab 13 - Sprite Collecting")

# --------------------------------------------------------------------
# Path setup (modern pathlib)
# --------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------
# LOAD SOUNDS (Modern pathlib version)
# ---------------------------------------------------------------------
good_sound = pygame.mixer.Sound(BASE_DIR / "good_block.wav")
bad_sound  = pygame.mixer.Sound(BASE_DIR / "bad_block.wav")
bump_sound = pygame.mixer.Sound(BASE_DIR / "bump.wav")

# ---------------------------------------------------------------------
# LOAD BACKGROUND IMAGE
# ---------------------------------------------------------------------
background_image = pygame.image.load(BASE_DIR / "world_background.png").convert_alpha()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)).convert_alpha()
background_image.fill((0, 0, 0, 125), special_flags=pygame.BLEND_RGBA_SUB)

# COLORS (RGB)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)


class Player(pygame.sprite.Sprite):
    """
    Player Sprite (Modern 2026 Version)
    -----------------------------------
    This class represents the player-controlled character.

    We use a class because:
    - It keeps movement logic organized
    - It stores speed, position, and future features (sounds, boundaries)
    - It matches modern pygame-ce and game engine architecture
    """

    # --- Methods ---
    def __init__(self, x, y):
        """
        Constructor: Runs once when the Player object is created.

        Parameters:
        x, y -> Starting position of the player on the screen.
        """
        super().__init__()  # Initialize Sprite parent class

        # --- Create the player's visual appearance ---
        # A 40x40 blue square (Lab 13 requirement: player must be BLUE)

        self.image = pygame.Surface([15, 15])
        self.image.fill(BLUE)  # BLUE player

        # The rect tracks the player's position and collision box.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # --- Movement Attributes ---
        # These store how fast the player moves horizontally and vertically.
        # Modern approach: direct assignment (not stacking speeds.)
        self.change_x = 0
        self.change_y = 0

    # -------------------------------------------------------------------
    # Movement Methods (Modern 2026 Style)
    # -------------------------------------------------------------------

    def go_left(self):
        """ Move player left by setting horizontal speed negative. """
        self.change_x = -3

    def go_right(self):
        """ Move player right by setting horizontal speed positive. """
        self.change_x = 3

    def go_up(self):
        """ Move player up by setting vertical speed negative. """
        self.change_y = -3

    def go_down(self):
        """ Move player down by setting vertical speed positive. """
        self.change_y = 3

    def stop_x(self):
        """ Stop horizontal movement when LEFT or RIGHT key is released. """
        self.change_x = 0

    def stop_y(self):
        """ Stop vertical movement when UP or DOWN key is released. """
        self.change_y = 0


    # ----------------------------------------------------------------
    # Update Method
    # ----------------------------------------------------------------

    def update(self):
        """
        Called once per frame.
        Moves the player based on current speed values.
        """
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        # ------------------------------------------------------------
        # Boundary Clamping (keep player inside screen)
        # ------------------------------------------------------------

        # LEFT boundary
        if self.rect.x < 0:
            self.rect.x = 0
            bump_sound.play()  # Hit left wall

        # RIGHT boundary
        if self.rect.right > screen_width:
            self.rect.right = screen_width
            bump_sound.play()  # Hit right wall

        # TOP boundary
        if self.rect.y < 0:
            self.rect.y = 0
            bump_sound.play()  # Hit top wall

        # BOTTOM boundary
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            bump_sound.play()  # Hit bottom wall


# This is a list of 'sprites'. Each block in the program is
# added to this list. The list is managed by a class called 'Group'.
block_list = pygame.sprite.Group()

# This is a list of every sprite.
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# GOOD blocks (green)
good_block_list = pygame.sprite.Group()

# BAD blocks (red)
bad_block_list = pygame.sprite.Group()

# --------------------------------------------------------------------
# CREATE GOOD (GREEN) AND BAD (RED) BLOCKS
# --------------------------------------------------------------------

# GOOD BLOCKS (GREEN)
for i in range(30):
    """
    These are the GOOD blocks. When the player collects them,
    the score will increase by +1.

    We now use GoodBlock instead of Block.
    GoodBlock moves randomly each frame

    GREEN blocks = GOOD. Collect them!
    """

    # Create a GOOD block (GREEN)
    block = GoodBlock(GREEN, 20, 15)

    # Random starting position inside the window
    block.rect.x = random.randrange(screen_width - block.rect.width)
    block.rect.y = random.randrange(screen_height - block.rect.height)

    # Add the block to the sprite groups
    good_block_list.add(block)
    all_sprites_list.add(block)


# BAD BLOCKS (RED)
for i in range(20):
    """
    These are the BAD blocks. When the player collects them,
    the score will decrease by -1.

    We now use BadBlocks instead of Block.
    BadBlock moves downward each frame

    RED Blocks = BAD. Avoid them!
    """
    block = BadBlock(RED, 20, 15)

    # Random starting position inside the window
    block.rect.x = random.randrange(screen_width - block.rect.width)
    block.rect.y = random.randrange(screen_height - block.rect.height)

    # Add the block to the sprite groups
    bad_block_list.add(block)
    all_sprites_list.add(block)

# Create a BLUE player
player = Player(20, 15)
all_sprites_list.add(player)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

score = 0

# ------------------------------------------------------------------
# FONT SETUP (for drawing score on screen)
# ------------------------------------------------------------------
font = pygame.font.SysFont("comicsans", 24)

# ---------- Main Program Loop ----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Keyboard Movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.go_left()

            elif event.key == pygame.K_RIGHT:
                player.go_right()

            elif event.key == pygame.K_UP:
                player.go_up()

            elif event.key == pygame.K_DOWN:
                player.go_down()

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.stop_x()

            if event.key in (pygame.K_UP, pygame.K_DOWN):
                player.stop_y()

    # --------------------------------------------------------------
    # GAME LOGIC
    # --------------------------------------------------------------

    # --------------------------------------------------------------
    # UPDATE ALL SPRITES
    # --------------------------------------------------------------
    # This calls the update() method on every sprite in the group.
    # GoodBlock objects will move randomly because their update()
    # method overrides the base Block update()
    all_sprites_list.update()

    # ------------------------------------------------------------------
    # REMOVE BAD BLOCKS THAT FALL OFF THE SCREEN
    # ------------------------------------------------------------------
    for block in bad_block_list:
        # If the block has moved below the bottom of the screen
        if block.rect.y > screen_height:
            """
            Remove the block from both sprite groups.
            This prevents invisible blocks from continuing to update.
            """
            bad_block_list.remove(block)
            all_sprites_list.remove(block)

            # OPTIONAL: Spawn a new BadBlock to replace it
            new_block = BadBlock(RED, 20, 15)
            new_block.rect.x = random.randrange(screen_width - new_block.rect.width)
            new_block.rect.y = random.randrange(-50, -10)  # spawn slightly above screen

            bad_block_list.add(new_block)
            all_sprites_list.add(new_block)


    # --------------------------------------------------------------
    # COLLISION DETECTION (GOOD and BAD blocks)
    # --------------------------------------------------------------

    # GOOD BLOCK collisions
    good_hits = pygame.sprite.spritecollide(player, good_block_list, True)
    for block in good_hits:
        """
        When the player touches a GOOD (green) block, we remove it
        from the game and increase the score by +1.

        GREEN = GOOD. Collect these!
        """
        score += 1
        good_sound.play()
        print(f"Score: {score} (+1 good block)")

        # Bump the player backward slightly
        player.rect.x -= 15
        player.rect.y -= 15

    # BAD BLOCK collisions
    bad_hits = pygame.sprite.spritecollide(player, bad_block_list, True)
    for block in bad_hits:
        """
        When the player touches a BAD (red) block, we remove it
        from the game and decrease the score by -1.

        RED = BAD. Avoid these!
        """
        score -= 1
        bad_sound.play()
        print(f"Score: {score} (-1 bad block)")

        # Bump the player backward slightly
        player.rect.x -= 15
        player.rect.y -= 15

    # -------------------------------------------------------------
    # GAME OVER CONDITION
    # -------------------------------------------------------------
    if len(good_block_list) == 0:
        # Clear screen
        screen.fill(BLACK)

        # Game Over message
        game_over_text = font.render("GAME OVER! You collected all the good blocks!", True, WHITE)
        screen.blit(game_over_text, (screen_width // 2 - 250, screen_height //2))

        pygame.display.flip()

        # Pause so player can see the message
        pygame.time.delay(3000)

        done = True
        continue

    # --------------------------------------------------------------
    # DRAWING
    # --------------------------------------------------------------

    # Fill the screen with black first (removes white edges)
    screen.fill(BLACK)

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # screen.fill(BLACK) # NO BACKGROUND IMAGE USE THIS
    all_sprites_list.draw(screen)

    # Draw score on screen
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
