"""
Program Arcade Games With Python and Pygame
Fourth Edition
Author: Dr. Paul Vincent Craven

coded along by: Jose 'Joe' Ruiz

Lab 1: Custom Calculators

lab_1_part_C.py

Create your own original problem and have the user plug in the variables.
If you are not in the mood for anything original, choose an equation from
this list:

  - Area of a circle                 #  math.pi * (r ** 2)
  - Area of an ellipse               #  math.pi * a * b
  - Area of an equilateral triangle  #  (math.sqrt(3) / 4) * (s ** 2)
  - Volume of a cone                 #  (1/3) * math.pi * (r ** 2) * h
  - Volume of a sphere               #  (4/3) * math.pi * (r ** 3)
  - Area of an arbitrary triangle    #  0.5 * b * h
"""

# Import modules
import subprocess
import os

def clear_screen() -> None:
    """Clear the terminal screen on Windows, macOS, or Linux."""
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

PLANET_DISTANCES_KM: dict[str, int] = {
    "Mercury": 91_000_000,
    "Venus":   41_000_000,
    "Mars":    78_000_000,
    "Jupiter": 628_000_000,
    "Saturn":  1_275_000_000,
    "Uranus":  2_723_000_000,
    "Neptune": 4_351_000_000,
    "Sun":     149_600_000,
    "Moon":    384_400,
}

def main() -> None:
    while True:
        clear_screen()

        print("Available destinations: ")
        for planet in PLANET_DISTANCES_KM:
            print(f" - {planet}")

        destination = input("\nWhich planet are we traveling to? ").title()

        if destination not in PLANET_DISTANCES_KM:
            print("That destination isn't in the list.")
            continue


        ship_speed = float(input("How fast is your spacecraft traveling (km/h)? "))

        distance = PLANET_DISTANCES_KM[destination]

        time_hours = distance / ship_speed
        time_days = time_hours / 24
        time_years = time_days / 365

        print(f"\nDistance to {destination}: {distance:,} km")
        print(f"Travel time in hours: {time_hours:,.2f}")
        print(f"Travel time in days: {time_days:,.2f}")
        print(f"Travel time in years: {time_years:,.4f}")

        again = input("\nCalculate another trip? (y/n): ").lower()
        if again != "y":
            return


if __name__ == "__main__":
    main()
