"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 8: Introduction to Lists

simple_encryption.py
"""

# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: http://youtu.be/sxFIxD8Gd3A

plain_text = "This is a test. ABC abc"

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)


