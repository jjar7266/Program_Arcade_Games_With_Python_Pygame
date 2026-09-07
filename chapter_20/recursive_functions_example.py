"""
Program Arcade Games With Python and Pygame
Fourth Edition
Copyright 2016
Author: Dr. Paul Vincent Craven

coded (2026) along by: Jose 'Joe' Ruiz

Chapter 20: Recursion

recursive_functions_example.py

"""
# ===================================================
# FACTORIAL WITHOUT RECURSION
# ===================================================
# A factorial means multiplying all whole numbers
# from 1 up to the number we choose.
#
# Example:
# 5! = 1 * 2 * 3 * 4 * 5
#
# This version uses a loop to do the multiplying.
# Think of it like climbing stairs one step at a time.


def factorial_nonrecursive(n):
    """
    Calculate a factorial using a simple loop.
    This does NOT use recursion.

    n: the number we want the factorial of
    """
    answer = 1

    # Start at 2 because multiplying by 1 doesn't change anything
    for i in range(2, n + 1):
        # Show each multiplication step
        print(i, "*", answer, "=", i * answer)

        # Update the running total
        answer = answer * i

    return answer

print("FACTORIAL (NON-RECURSIVE METHOD)")
user_input = input("Enter a number:")
n = int(user_input)

# Call the non-recursive version
answer = factorial_nonrecursive(n)
print(answer)


# ===========================================================
# FACTORIAL WITH RECURSION
# ===========================================================
# Recursion means a function calls itself.
#
# Think of recursion like climbing stairs,
# but instead of a loop, the function keeps calling itself
# until it reaches the top step.
#
# Each call handles ONE step of the multiplication.


def factorial_recursive(n):
    """
    Calculate a factorial using recursion.

    n: the number we want the factorial of
    """

    # Base case:
    # If n is 1, we stop and return 1.
    # This is like saying:
    # "We reached the top step. No more climbing."
    if n == 1:
        return 1

    # Recursive case:
    # Ask the function to solve the factorial of n - 1.
    x = factorial_recursive(n - 1)

    # Show the multiplication step happening on the way back up
    print(n, "*", x, "=", n * x)

    # Return the result of this step
    return n * x


print("\nFACTORIAL (RECURSIVE METHOD)")
user_input = input("Enter a number:")
n = int(user_input)

# Call the recursive version
answer = factorial_recursive(n)
print(answer)


