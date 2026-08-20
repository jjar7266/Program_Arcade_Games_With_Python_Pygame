"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 13: Introduction to Classes

ball_class.py

This example code could be used in Python/Pygame to draw a ball.
Having all the parameters contained in a class makes data management
easier.
"""
# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: https://www.youtube.com/watch?v=VFd2m-IeKCc&t=2s

# Example: Ball Class

# Import modules
import pygame

# ============================================================
# 🟢 Ball Class
#    - Holds position
#    - Holds movement vector
#    - Holds size + color
#    - Can move itself
#    - Can draw itself
# ============================================================


class Ball():
    def __init__(self):

        # --- Class Attributes ---

        # Ball position
        self.x = 0
        self.y = 0

        # Ball's vector
        self.change_x = 0
        self.change_y = 0

        # Ball size
        self.size = 10

        # Ball color
        self.color = [255, 255, 255]

    # --- Class Methods ---
    def move(self):
        self.x += self.change_x
        self.y += self.change_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

# ========================================================================
"""
Below is the code that would go ahead of the main program loop
to create a ball and set its attributes:

theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255,0,0]

===========================================================================
This code would go inside the main loop to move and draw the ball:

theBall.move()
theBall.draw(screen)
"""
