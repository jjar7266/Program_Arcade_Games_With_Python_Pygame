"""
badblock_library.py
-------------------
This module defines the BadBlock class.

A BadBlock is a RED block that moves downward each frame.
It inherits from the base Block class found in block_library.py

This file contains ONLY the BadBlock class.
All spawning, positioning, and game logic stay in the main script.
"""

import pygame
from block_library import Block


class BadBlock(Block):
    """
    BadBlock Class
    --------------
    A BAD block that moves downward each frame.

    Inheritance:
        BadBlock(Block)
        - This means BadBlock automatically gets everything from Block:
          * image
          * rect (position)
          * width/height
          * color
          * Sprite behavior

    We override the update() method to give BadBlock special movement.
    """

    def update(self):
        """
        update()
        --------
        Called once per frame by the main game loop.

        BAD blocks move downward:
            - Increase rect.y by a fixed amount each frame
            - This creates a falling motion
        """

        # Move downward by 1 pixel per frame
        self.rect.y += 1
