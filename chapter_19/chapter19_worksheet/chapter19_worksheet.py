"""
Chapter 19 Worksheet
Program Arcade Games With Python and Pygame
Fourth Edition
Jose 'Joe' Ruiz

This file contains the worksheet questions and fully commented solutions.
"""

# Import modules
import subprocess

def clear_screen():
    """ Clears the terminal screen. """
    subprocess.run("cls", shell=True)


def q1():
    clear_screen()

    # -------------------------------------------------------------
    # 1. Define the following terms in your own words:
    #    Exception
    #    Exception Handling
    #    Try block
    #    Catch block
    #    Unhandled exception
    #    Throw
    # --------------------------------------------------------------

    print("Exception:")
    print("An exception is what happens when Python run into a problem it cannot solve on its own.")

    print("\nException Handling:")
    print("Exception handling is how we catch those problems so the program does not crash.")

    print("\nTry block:")
    print("A try block is the part of the code where we tell Python to 'try' something that might fail.")

    print("\nCatch block:")
    print("A catch block is the part that runs if something goes wrong inside the try block.")

    print("\nUnhandled exception:")
    print("An unhandled exception is a problem that was not caught, so the program stops and crashes.")

    print("\nThrow:")
    print("To throw means to purposely create an exception to signal that something is wrong.")


def q2():
    clear_screen()

    # ------------------------------------------------------------
    # 2. Show how to modify the following code so that an error is
    #    printed if the number conversion is not successful.
    #    Modify this code, don't just copy the example from the text.
    #    Do NOT ask again if the conversion is unsuccessful.
    #
    #    user_input_string = input("Enter a number:")
    #    user_value = int(user_input_string)
    # ------------------------------------------------------------

    user_input_string = input("Enter a number: ")

    try:
        # Try to convert the text into a number
        user_value = float(user_input_string)
        print("You entered the number:", user_value)

    except ValueError:
        # If conversion fails, print an error once
        print("Error: that is not a valid number.")


def q3():
    clear_screen()

    # ------------------------------------------------------------
    # 3. What will the following code output? Predict, and then run
    #    the code to see if you are correct. Write your prediction
    #    here and if you are right. If you aren't make sure you
    #    understand why. (Make sure to write both the prediction,
    #    and the actual results. No credit will be given if you just
    #    list the results or the prediction. If the program raises
    #    an error, list fact for this and the next problem as well.)
    #
    #    x = 5
    #    y = 0
    #    print("A")
    #    try:
    #        print("B")
    #        a = x / y
    #        print("C")
    #    except:
    #        print("D")
    #    print("E")
    #    print(a)
    # --------------------------------------------------------------

    print("Prediction:")
    print("A prints first.")
    print("B prints next.")
    print("x / y causes a ZeroDivisionError.")
    print("So 'C' will NOT print.")
    print("'D' will print because the except block runs.")
    print("'E' will print after the try/except.")
    print("Then print(a) will cause an error because 'a' was never created.")

    print("\nActual Result:")
    try:
        x = 5
        y = 0
        print("A")
        try:
            print("B")
            a = x / y
            print("C")
        except:
            print("D")
        print("E")
        print(a)
    except Exception as e:
        print("The program raised an error:", e)


def q4():
    clear_screen()

    # ---------------------------------------------------------------
    # 4. What will the following code output? Predict, and then run
    #    the code to see if you are correct. Write your prediction
    #    here and if you are right. If you aren't, make sure you
    #    understand why.
    #
    #    x = 5
    #    y = 10
    #    print("A")
    #    try:
    #        print("B")
    #        a = x / y
    #        print("C")
    #    except:
    #        print("D")
    #    print("E")
    #    print(a)
    # ----------------------------------------------------------------

    print("Prediction:")
    print("A prints first.")
    print("B prints next.")
    print("x / y works because dividing by 10 is allowed.")
    print("So 'C' will print.")
    print("'D' will NOT print because no error happens.")
    print("'E' will print after the try/except.")
    print("Then print(a) will show the result of 5 / 10, which is 0.5.")

    print("\nActual Result:")
    try:
        x = 5
        y = 10
        print("A")
        try:
            print("B")
            a = x / y
            print("C")
        except:
            print("D")
        print("E")
        print(a)
    except Exception as e:
        print("The program raised an error:", e)


if __name__ == "__main__":
    # q1()    # <- run Question 1
    # q2()    # <- run Question 2
    # q3()    # <- run Question 3
    q4()    # <- run Question 4
