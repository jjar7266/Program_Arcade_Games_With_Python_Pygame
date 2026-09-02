"""
goodblock_library.py
--------------------
This module defines the GoodBlock class.

A GoodBlock is a GREEN block that moves randomly around the screen.
It inherits from the base Block class found in block_library.py.

This file contains ONLY the GoodBlock class.
All spawning, positioning, and game logic stay in the main script.
"""

# import modules
import pygame
import random
from block_library import Block


class GoodBlock(Block):
    """
    GoodBlock Class
    ---------------
    A GOOD block that moves randomly each frame.

    Inheritance:
        GoodBlock(Block)
        - This means GoodBlock automatically gets everything from Block:
          * image
          * rect (position)
          * width/height
          * color
          * Sprite behavior

    We only override the update() method to give GoodBlock special movement.
    """

    def update(self):
        """
        update()
        --------
        Called once per frame by the main game loop

        GOOD blocks move randomly:
            - random left/right movement
            - random up/down movement

        random.randrange(-3, 4) gives a number between -3 and +3.
        This creates a jittery wandering motion.
        """

        # Move horizontally by a random amount
        self.rect.x += random.randrange(-3, 4)

        # Move vertically by a random amount
        self.rect.y += random.randrange(-3, 4)

        # Keep GoodBlocks inside the screen
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 800:
            self.rect.right = 800

        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.bottom > 600:
            self.rect.bottom = 600

