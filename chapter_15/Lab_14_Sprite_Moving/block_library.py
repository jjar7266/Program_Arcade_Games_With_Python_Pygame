"""
block_library.py
----------------
This module defines the base Block class.

A Block is the simplest type of sprite in the game.
- It has a color
- It has a width and height
- It has a rectangular positon (rect)
- It does NOT move by itself

other classes (GoodBlock, BadBlock) will INHERIT from this class
and add their own special behavior.

This file contains ONLY the Block class.
All spawning, movement, and game logic stay in the main script.
"""

# Import modules
import pygame


class Block(pygame.sprite.Sprite):
    """
    Block Class
    -----------
    The base class for all block types in the game.

    Inheritance:
        Block(pygame.sprite.Sprite)
        - This means Block becomes a Pygame Sprite.
        - It automatically gets:
            * image (surface)
            * rect (position)
            * sprite group compatibility

    This class does NOT move on its own.
    It simply defines what a block LOOKS LIKE.
    """

    def __init__(self, color, width, height):
        """
        Constructor
        -----------
        Called when a new Block object is created.

        Parameters:
            color  -> RGB tuple (example: (0, 255, 0))
            width  -> width of the block in pixels
            height -> height of the block in pixels

        The constructor creates:
            * a Surface (the block's image)
            * a rect (the block's position)
        """

        # Initialize the parent Sprite class
        super().__init__()

        # Create the block's image (a simple colored rectangle)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Get the rectangle that matches the image size
        # This rect stores teh block's position on the screen.
        self.rect = self.image.get_rect()
