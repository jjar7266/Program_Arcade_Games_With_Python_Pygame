"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 8: Introduction to Lists

simple_decryption.py
"""

# Sample Python/Pygame Programs
# http://programarcadegames.com/

# Explanation video: http://youtu.be/sxFIxD8Gd3A

encrypted_text = "Uijt!jt!b!uftu/!BCD!bcd"

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x = x - 1
    c2 = chr(x)
    plain_text = plain_text + c2
print(plain_text)

