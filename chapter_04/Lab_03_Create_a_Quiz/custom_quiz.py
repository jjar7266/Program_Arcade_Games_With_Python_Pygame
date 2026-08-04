"""
Program Arcade Games With Python and Pygame
Fourth Edition
Author: Dr. Paul Vincent Craven
Copyright 2016

coded (2026) along by: Jose 'Joe' Ruiz

Lab 3: Create-a-Quiz

custom_quiz.py

Quiz Example Below:
================================================================
    Quiz time!

    How many books are there in the Harry Potter series? 7
    Correct!

    What is 3*(2-1)? 3
    Correct!

    What is 3*2-1? 5
    Correct!

    Who sings Black Horse and the Cherry Tree?
    1. Kelly Clarkson
    2. K.T. Tunstall
    3. Hillary Duff
    4. Bon Jovi
    ? 2
    Correct!

    Who is on the front of a one dollar bill
    1. George Washington
    2. Abraham Lincoln
    3. John Adams
    4. Thomas Jefferson
    ? 2
    No.

    Congratulations, you got 4 answers right.
    That is a score of 80.0 percent.

================================================================
"""
# Import modules
import subprocess

# Clears the terminal screen
subprocess.run("cls", shell=True)

print("5th Grade General Knowledge Quiz")
print()

number_correct  = 0
total_questions = 10

# ------------------------
# Question 1
# ------------------------
print("1. What is the largest planet is our solor system?")
print("A) Earth")
print("B) Saturn")
print("C) Jupiter")
print("D) Mars")
answer = input("? ")

if answer.lower() == "c":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# ------------------------
# Question 2
# ------------------------
print("2. How many degrees are in a full circle?")
print("A) 90")
print("B) 180")
print("C) 270")
print("D) 360")
answer = input("? ")

if answer.lower() == "d":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# -----------------------------
# Question 3
# -----------------------------
print('3. Which continent is known as the "island continent" or "land down under"?')
print("A) Africa")
print("B) Australia")
print("C) Antarctica")
print("D) Europe")
answer = input("? ")

if answer.lower() == "b":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# -------------------------------
# Question 4
# -------------------------------
print("What do the stars on the United States flag represent?")
print("A) The original colonies")
print("B) Presidents")
print("C) States")
print("D) Wars fought")
answer = input("? ")

if answer.lower() == "c":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# -----------------------------------
# Question 5
# -----------------------------------
print("5. What is a baby frog called before it grows legs?")
print("A) Fry")
print("B) Tadpole")
print("C) Joey")
print("D) Larva")
answer = input("? ")

if answer.lower() == "b":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# ---------------------------------------
# Question 6
# ---------------------------------------
print("6. Which of these is the longest river in the world?")
print("A) Amazon River")
print("B) Mississippi River")
print("C) Nile River")
print("D) Yangtze River")
answer = input("? ")

if answer.lower() == "c":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# -------------------------------------------
# Question 7
# -------------------------------------------
print("7. What is the freezing point of water in Celsius?")
print("A) 0 degrees")
print("B) 32 degrees")
print("C) 100 degrees")
print("D) 212 degrees")
answer = input("? ")

if answer.lower() == "a":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# ---------------------------------------------
# Question 8
# ---------------------------------------------
print("8. What do you call A, E, I, O, and U?")
print("A) Consonants")
print("B) Vowels")
print("C) Syllables")
print("D) Nouns")
answer = input("? ")

if answer.lower() == "b":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# ------------------------------------------------
# Question 9
# ------------------------------------------------
print("9. What is the area of a rectangle with length 5 and width 4?")
print("A) 9 square inches")
print("B) 18 square inches")
print("C) 20 square inches")
print("D) 40 square inches")
answer = input("? ")

if answer.lower() == "c":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# ---------------------------------------------
# Question 10
# ---------------------------------------------
print("10. Who was the first President of the United States?")
print("A) Thomas Jefferson")
print("B) Abraham Lincoln")
print("C) George Washington")
print("D) Benjamin Franklin")
anser = input("? ")

if answer.lower() == "c":
    print("Correct!")
    number_correct += 1
else:
    print("No.")
print()

# -------------------------------
# Final Score
# -------------------------------
percent = (number_correct / total_questions) * 100

print("Congratulations, you got", number_correct, "answers right.")
print("That is a score of", percent, "percent.")

