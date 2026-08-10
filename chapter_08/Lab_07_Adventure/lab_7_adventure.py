"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Lab 7: Adventure

lab_7_adventure.py
"""

# ------------------------------------------------------
# STEP 1: Create an empty list to hold all rooms
# ------------------------------------------------------
# In this adventure game, every room will be represented as
# a small list containing:
#   [description, north, east, south, west]
#
# We will store ALL of those room lists inside one big list
# called room_list. This allows us to access rooms by number.
# like room_list[0], room_list[1], etc.
#
# Right now, we start with an empty list and will append
# each room one at a time.
room_list = []


# -------------------------------------------------------
# STEP 2: Create Room 0
# -------------------------------------------------------
# Each room in our adventure game is represented as a list:
#   [description, north, east, south, west]
#
# The description is what the player sees when they enter
# the room. The four directions tell the game which room
# number lies in each direction. If there is no room in a
# direction, we use None.

# ROOM 0 - Forest Clearing
# Description:
#   The forest opens into a quiet clearing surrounded by
#   towering pines. A cool breeze carries the scent of moss
#   and earth. A narrow path winds north toward a shadowy
#   cave entrance.
#
# Exits:
#  North -> Room 1
#  East  -> None
#  South -> None
#  West  -> None
room = ["You stand in a quiet forest clearing surrounded by tall pines.\n"
        "A cool breeze carries the scent of moss and earth.\n"
        "A narrow path leads north toward a shadowy cave entrance.",
        1, None, None, None
]

# Add this room to the master list of rooms
room_list.append(room)

# ---------------------------------------------------------------------
# STEP 3: Create Room 1
# ---------------------------------------------------------------------
# ROOM 1 - Cave Entrance
# Description:
#   A rocky archway opens into a yawning cave mouth. The air
#   grows cooler as you approach, carrying the scent of damp
#   stone. Faint echoes drift from deep within the darkness.
#
# Exits:
#   North -> Room 2
#   East  -> Room 3
#   South -> Room 0
#   West  -> None

room = [
    "A rocky archway opens into a yawning cave mouth.\n"
    "The air grows cooler as you approach, carrying the scent of damp stone.\n"
    "Faint echoes drift from deep within the darkness.\n"
    "A tunnel leads north, a side passage heads east, and a path runs south.",
    2, 3, 0, None
]

# Add this room to the master list of rooms
room_list.append(room)

# ---------------------------------------------------------------------
# STEP 4: Create Room 2
# ---------------------------------------------------------------------
# ROOM 2 - Old Temple
# Description:
#   Crumbling stone pillars rise from the floor, carved with
#   faded symbols of forgotten rituals. Dust drifts through
#   beams of pale light slipping in from cracks overhead.
#   The silence feels ancient, as though the temple itself
#   is holding its breath.
#
# Exits:
#   North -> None
#   East  -> None
#   South -> Room 3
#   West  -> Room 1

room = [
    "Crumbling stone pillars rise from the floor, carved with faded symbols\n"
    "of forgotten rituals. Dust drifts through beams of pale light slipping\n"
    "in from cracks overhead. The silence feels ancient, as though the temple\n"
    "itself is holding its breath.\n"
    "A narrow route heads south, and a worn stone path leads west.",
    None, None, 3, 1
]

# Add this room to the master list of rooms
room_list.append(room)

# -------------------------------------------------------------------
# STEP 5: Create Room 3
# -------------------------------------------------------------------
# ROOM 3 - Dark Tunnel
# Description:
#   The tunnel walls glisten with moisture, reflecting faint
#   shards of light from somewhere far behind you. The air is
#   thick and cool, carrying the steady drip of water echoing
#   through the narrow passage. The darkness ahead feels heavy,
#   as though it is waiting.
#
# Exits:
#   North -> Room 2
#   East  -> None
#   South -> Room 6
#   West  -> Room 1

room = [
    "The tunnel walls glisten with moisture, reflecting faint shards of light\n"
    "from somewhere far behind you. Cool air carries the steady drip of water\n"
    "echoing through the narrow passage. The darkness ahead feels heavy, as\n"
    "though it is waiting.\n"
    "A passage climbs north, another drops south, and a narrow path bends west.",
    2, None, 6, 1
]

# Add this room to the master list of rooms
room_list.append(room)

# ------------------------------------------------------------------------
# STEP 6 - Create Room 4
# ------------------------------------------------------------------------
# ROOM 4 - Abandoned Hut
# Description:
#   A collapsed wooden roof lets moonlight spill across the
#   remains of broken furniture. Dusty shelves line the walls,
#   their contents long since taken or decayed. The air feels
#   still, as though no one has stepped inside for decades.
#
# Exits:
#   North -> None
#   East  -> Room 5
#   South -> None
#   West  -> None

room = [
    "A collapsed wooden roof lets moonlight spill across broken furniture.\n"
    "Dusty shelves line the walls, their contents long forgotten. The air\n"
    "feels still, untouched for decades.\n"
    "A narrow passage leads east toward a glowing well.",
    None, 5, None, None
]

# Add this room to the master list of rooms
room_list.append(room)

# ---------------------------------------------------------------------
# STEP 7: Create Room 5
# ---------------------------------------------------------------------
# ROOM 5 - Mysterious Well
# Description:
#   A circular stone well stands at the center of the room,
#   its water glowing with a faint blue light. A soft hum
#   vibrates through the air, as though the well itself is
#   alive. The glow reflects off the walls, casting shifting
#   patterns that dance like spirits.
#
# Exits:
#   North -> Room 6
#   East  -> None
#   South -> None
#   West  -> Room 4

room = [
    "A circular stone well glows with faint blue light, humming softly in\n"
    "the still air. Shifting reflections ripple across the walls like\n"
    "dancing spirits. The energy feels ancient, pulsing gently beneath your\n"
    "feet.\n"
    "A narrow stone ramp climbs north toward a vast cavern.",
    6, None, None, 4
]

# Add this room to the master list of rooms
room_list.append(room)

# ------------------------------------------------------------------
# STEP 8: Create Room 6
# ------------------------------------------------------------------
# ROOM 6 - Underground Lake
# Description:
#   A vast cavern opens before you, illuminated by the solf
#   glow of crystals embedded in the walls. A still, glassy
#   lake stretches into the darkness, its surace reflecting
#   shimmering patterns of blue and silver. Gentle ripples
#   echo through the chamber, as though something beneath the
#   water is stirring.
#
# Exits:
#   North -> Room 3
#   East  -> None
#   South -> Room 7
#   West  -> Room 5

room = [
    "A vast cavern illuminated by glowing crystals opens around a still\n"
    "underground lake. Blue and silver reflections shimmer across the\n"
    "water's surface, disturbed only by gentle ripples. The air feels cool\n"
    "and alive, as though something beneath the lake is quietly stirring.\n"
    "A narrow tunnel leads north, while a sloping path descends south.",
    3, None, 7, 5
]

# Add this room to the master list of rooms
room_list.append(room)

# -----------------------------------------------------------------------
# STEP 9: Create Room 7
# -----------------------------------------------------------------------
# ROOM 7 - Treasure Chamber
# Description:
#   Golden light spills from a massive crystal suspended
#   above a stone pedestal. Ancient treasures lie scattered
#   around the chamber-rusted blades, jeweled goblets, and
#   ornate chests sealed by time. The air hums with power,
#   as though the chamber itself recognizes your presence.
#
# Exits:
#   North -> Room 6
#   East  -> None
#   South -> None
#   West  -> None

room = [
    "Golden light pours from a massive crystal suspended above a stone\n"
    "pedestal. Ancient treasures lie scattered across the chamber—jeweled\n"
    "goblets, rusted blades, sealed chests. The air hums with quiet power,\n"
    "acknowledging your arrival.\n"
    "A narrow passage leads north toward the vast cavern.",
    6, None, None, None
]

# Add this room to the master list of rooms
room_list.append(room)

# ----------------------------------------------------------------------
# Utility Function: clear the screen
# ----------------------------------------------------------------------
# This function clears the terminal window so the player
# always sees a fresh screen when entering a new room.
# It works on Windows (cls) and macOS/Linux (clear).
import subprocess

def clear_screen():
    # Windows uses 'cls' macOS/Linux use 'clear'
    command = "cls" if subprocess.os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

# ----------------------------------------------------------------------
# STEP 10: Main Game Loop
# ----------------------------------------------------------------------
# This loop controls the entire adventure. It repeatedly:
#   1. Shows the player the description of the current room.
#   2. Asks the player which direction they want to go.
#   3. Checks if that direction is valid.
#   4. Moves the player to the next room if possible.
#   5. Continues until the player chooses to quit.
#
# This is the "engine" of the game. All movement, exploration,
# and interaction happens inside this loop.
# -----------------------------------------------------------------------


def main():
    current_room = 0          # The player always starts in Room 0
    done = False              # When this becomes True, the game ends

    while not done:
        # --------------------------------------
        # Show the player where they are
        # --------------------------------------
        print()
        print(room_list[current_room][0])   # Print the room description
        print()

        # --------------------------------------
        # Ask the player what they want to do
        # --------------------------------------
        user_input = input("Which direction do you want to go? (n/e/s/w or q to quit): ")

        # --------------------------------------
        # Handle quitting the game
        # --------------------------------------
        if user_input.lower() == "q":
            print("Thanks for playing!")
            done = True
            continue

        # --------------------------------------------------
        # Convert the player's direction into a room index
        # --------------------------------------------------
        if user_input.lower() == "n":
            next_room = room_list[current_room][1]

        elif user_input.lower() == "e":
            next_room = room_list[current_room][2]

        elif user_input.lower() == "s":
            next_room = room_list[current_room][3]

        elif user_input.lower() == "w":
            next_room = room_list[current_room][4]

        else:
            print("I don't understand that command.")
            input("Press Enter to continue...")
            clear_screen()
            continue

        # ----------------------------------------------------
        # Check if the player can move in that direction
        # ----------------------------------------------------
        if next_room is None:
            print("You can't go that way.")
            input("Press Enter to continue...")
            clear_screen()
            continue

        else:
            current_room = next_room  # Move to the next room

        # ------------------------------------------------------
        # Clear the screen *after* movement
        # ------------------------------------------------------
        clear_screen()


# ------------------------------------------------------
# Standard Python entry point
# ------------------------------------------------------
if __name__ == "__main__":
    main()
