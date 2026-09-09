"""
Chapter 21 Worksheet
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
    # 1. Take the following program and use print formatting so the
    #    output aligns and includes commas. Must work for any
    #    integer from 0 to 9,000,000. No plus signs. Only two
    #    double quotes per print statement.
    # -------------------------------------------------------------

    score = 41237
    highscore = 1023407

    print(f"Score:      {score:>10,}")
    print(f"High score: {highscore:>10,}")


def q2():
    clear_screen()

    # ----------------------------------------------------------
    # 2. Loop from 1 to 20 and print the decimal equivalent of
    #    their inverse. Use print formatting to exactly match the
    #    required output.
    # ----------------------------------------------------------

    for n in range(1, 21):
        inverse = 1 / n
        print(f"1/{n:<2} = {inverse:.4f}".rstrip("0").rstrip("."))


def q3():
    clear_screen()

    # ---------------------------------------------------------------
    # 3. Write a recursive function that will calculate the
    #    Fibonacci series, and use output formatting to match the
    #    exact sample output.
    # ----------------------------------------------------------------

    def fib(n: int) -> int:
        """
        Recursive Fibonacci function.

        The Fibonacci sequence is defined as:
            fib(1) = 1
            fib(2) = 1
            fib(n) = fib(n-1) + fib(n-2)

        This function calls itself until it reaches the base cases
        (n <= 2). Each call returns a number, and those numbers get
        added together as the recursion unwinds.

        Example:
            fib(5)
            -> fib(4) + fib(3)
            -> (fib(3) + fib(2)) + (fib(2) + fib(1))
            -> ... continues until base cases return 1
        """
        # Base cases: the first two Fibonacci numbers are always 1
        if n <= 2:
            return 1

        # Recursive case:
        # Return the sum of the previous two Fibonacci numbers.
        # This is where recursion happens - the function calls itself.
        return fib(n - 1) + fib(n - 2)

    # Loop through Fibonacci numbers 1-35
    for n in range(1, 36):
        value = fib(n)

        # Print the index and the Fibonacci value.
        # Formatting:
        #   {n:>2}       -> right-align index in width 2
        #   {value:>10,} -> right-align value in width 10 with commas
        print(f"{n:>2} - {value:>10,}")


def q4():
    clear_screen()

    # -------------------------------------------------------------
    # 4. Why does the problem above run so slow? How could it
    #    be made to run faster?
    # -------------------------------------------------------------

    print("The recursive Fibonacci function runs slow because it")
    print("recomputes the same value many times. It can be made")
    print("faster by storing results (memoization) or using a")
    print("non-recursive version.")


def q5():
    clear_screen()

    # ------------------------------------------------------------
    # 5. Create a faster version of the Fibonacci function using
    #    memoization. Memoization stores previously-computed values
    #    so they do not need to be recalculated. This eliminates
    #    repeated work and makes Fibonacci run dramatically faster.
    # -------------------------------------------------------------

    # Dictionary used to store previously-computed Fibonacci values.
    # Keys: n (the Fibonacci index)
    # Values: fib(n)
    cache = {}

    def fib_fast(n: int) -> int:
        """
        Fast Fibonacci using memoization.

        Memoization works by storing results the first time they are
        computed. If the function is called again with the same n,
        the stored value is returned instantly instead of recomputing
        the entire recursive chain.

        This reduces the time complexity from exponential to linear.
        """

        # If we already computed fib(n), return it immediately.
        if n in cache:
            return cache[n]

        # Base cases: fib(1) and fib(2) are always 1.
        if n <= 2:
            cache[n] = 1
            return 1

        # Recursive case:
        # Compute fib(n-1) and fib(n-2) using the fast version.
        value = fib_fast(n - 1) + fib_fast(n - 2)

        # Store the computed value in the cache.
        cache[n] = value
        return value

    # Print Fibonacci numbers 1-35 using the fast version.
    for n in range(1, 36):
        value = fib_fast(n)

        # Formatting:
        #   {n:>2}       -> right-align index in width 2
        #   {value:>10,} -> right-align value in width 10 with commas
        print(f"{n:>2} - {value:>10,}")


if __name__ == "__main__":
    # q1()    # <- run Question 1
    # q2()    # <- run Question 2
    # q3()    # <- run Question 3
    # q4()    # <- run Question 4
    q5()    # <- run

