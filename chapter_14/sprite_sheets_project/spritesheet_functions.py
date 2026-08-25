"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 14: Introduction to Sprites

This module is used to pull individual sprites from sprite sheets.

spritesheet_functions.py
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Part of a series:
#    - move_with_walls_example.py
#    - maze_runner.py
#    - platform_jumper.py
#    - platform_scroller.py
#    - platform_moving.py
#    - sprite_sheets/

"""
This class pulls smaller images out of the large sprite sheet.
Create an instance of the class and pass in the file name as a
parameter to the constructor. Then call getImage with the x, y location
of the upper left corner of your sprite along with its height and width.
You can use a drawing program to get the location of the sprite images
you are intersted in.
"""

# Import modules
import pygame
import constants

from pathlib import Path

class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet. """

    def __init__(self, file_name):
        """ Constructor. Pass in the file name of the sprite sheet. """

        # Build a reliable path to the assets folder
        sprite_path = Path(__file__).resolve().parent / "assets" / file_name

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()

    def get_image(self, x, y, width, height):
        """
        Grab a single image out of a larger spritesheet
        Pass in the x, y location of the sprite
        and the width and height of the sprite.
        """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert_alpha()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(constants.BLACK)

        # Return the image
        return image


