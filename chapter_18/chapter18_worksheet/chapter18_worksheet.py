"""
Chapter 18 Worksheet
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

    # -----------------------------------------------------------
    # 1. Write code to swap the values 25 and 40.
    #
    # Given list:
    # my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]
    #
    # The values we need to swap:
    #   40 is at index 6
    #   25 is at index 7
    #
    # We use a temporary variable so neither value is overwritten
    # during the swap. This is the classic swap pattern used in
    # selection sort and many other algorithms.
    # ------------------------------------------------------------

    my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]

    temp = my_list[6]        # Save the value 40
    my_list[6] = my_list[7]  # Move 25 into index 6
    my_list[7] = temp        # Move 40 into index 7

    print("After swap:", my_list)


def q2():
    clear_screen()

    # --------------------------------------------------------------
    # 2. Write code to swap the values 2 and 27.
    #
    # Given list:
    # my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
    #
    # The values we need to swap:
    #   27 is at index 0
    #    2 is at index 3
    #
    # We use a temporary variable so neither value is overwritten
    # during the swap. This is the same classic swap pattern used
    # in selection sort and many other algorithms.
    # ----------------------------------------------------------------

    my_list = [27, 32, 18, 2, 11, 57, 14, 38, 19, 91]

    temp = my_list[0]           # Save the value 27
    my_list[0] = my_list[3]     # Move 2 into index 0
    my_list[3] = temp           # Move 27 into index 3

    print("After swap:", my_list)


def q3():
    clear_screen()

    # ---------------------------------------------------------------
    # 3. Why does the following code not work? Explain it, don't
    #    just list working code.
    #
    # my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
    # temp = my_list[0]
    # my_list[1] = my_list[0]
    # my_list[0] = temp
    #
    # ----------------------------------------------------------------
    # Explanation:
    #
    # The intention here is to swap values at index 0 and 1.
    # But the code does NOT perform a swap. Instead, it DUPLICATES
    # the value at index 0.
    #
    # Step-by-step:
    #
    #   temp = my_list[0]
    #       temp now holds the value 70.
    #
    #   my_list[1] = my_list[0]
    #       This overwrites index 1 with the SAME value (70).
    #       Now BOTH index 0 and index 1 contain 70.
    #
    #   my_list[0] = temp
    #       This puts 70 back into index 0.
    #
    # After these three lines:
    #       my_list[0] == 70
    #       my_list[1] == 70
    #
    # The original value at index 1 (32) is LOST.
    #
    # Why it fails:
    #   Because the programmer copied index 0 into index 1 BEFORE
    #   saving index 1's value. Once index 1 is overwritten, the
    #   original value (32) is gone forever.
    #
    # This is the classic mistake: copying one value destroys the
    # other unless BOTH values are saved before overwriting.
    #
    # ---------------------------------------------------------------
    # Demonstration:
    # ---------------------------------------------------------------

    my_list = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]

    temp = my_list[0]
    my_list[1] = my_list[0]
    my_list[0] = temp

    print("Result of the incorrect swap attempt:")
    print(my_list)


def q4():
    clear_screen()

    # ---------------------------------------------------------------
    # 4. Show how the following numbers can be sorted using the
    #    selection sort. Show the numbers after each iteration of
    #    the outer loop, similar to Figure 17.5.
    #
    #    I am NOT looking for code that performs the sort.
    #    I am showing the manual steps of the algorithm.
    #
    # Numbers:
    #    97   74    8   98   47   62   12   11    0   60
    #
    # ----------------------------------------------------------------
    # Selection sort logic (manual):
    #
    # Outer loop position (cur_pos) moves from index 0 -> end.
    # For each cur_pos:
    #   - Find the smallest value in the remaining unsorted portion.
    #   - Swap it into cur_pos.
    #
    # We sill show the list AFTER each outer loop iteration.
    #
    # -----------------------------------------------------------------
    # Initial list:
    # [97, 74, 8, 98, 47, 62, 12, 11, 0, 60]
    #
    # -----------------------------------------------------------------
    # OUTER LOOP ITERATION 0 (cur_pos = 0)
    # Smallest value in entire list is 0 at index 8.
    # Swap index 0 and index 8.
    #
    # Result:
    # [0, 74, 8, 98, 47, 62, 12, 11, 97, 60]
    #
    # ------------------------------------------------------------------
    # OUTER LOOP ITERATION 1 (cur_pos = 1)
    # Smallest value from index 1->end is 8 at index 2.
    # Swap index 1 and index 2.
    #
    # Result:
    # [0, 8, 74, 98, 47, 62, 12, 11, 97, 60]
    #
    # ------------------------------------------------------------------
    # OUTER LOOP ITERATION 2 (cur_pos = 2)
    # Smallest value from index 2->end is 11 at index 7.
    # Swap index 2 and index 7.
    #
    # Result:
    # [0, 8, 11, 98, 47, 62, 12, 74, 97, 60]
    #
    # ------------------------------------------------------------------
    # OUTER LOOP ITERATION 3 (cur_pos = 3)
    # Smallest value from index 3->end is 12 at index 6.
    # Swap index 3 and index 6.
    #
    # Result:
    # [0, 8, 11, 12, 47, 62, 98, 74, 97, 60]
    #
    # ------------------------------------------------------------------
    # OUTER LOOP ITERATION 5 (cur_pos = 5)
    # Smallest value from index 5->end is 60 at index 9.
    # Swap index 5 and index 9.
    #
    # Result:
    # [0, 8, 11, 12, 47, 60, 98, 74, 97, 62]
    #
    # ------------------------------------------------------------------
    # OUTER LOOP ITERATION 6 (cur_pos = 6)
    # Smallest value from index 6->end is 62 at index 9.
    # Swap index 6 and index 9.
    #
    # Result:
    # [0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
    #
    # ------------------------------------------------------------------
    # OUTER LOOP ITERATION 7 (cur_pos = 7)
    # Smallest value from index 7->end is 74 at index 7.
    # Already in correct position -> no swap.
    #
    # Result:
    # [0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
    #
    # ---------------------------------------------------------------
    # OUTER LOOP ITERATION 8 (cur_pos = 8)
    # Smallest value from index 8->end is 97 at index 8.
    # Already in correct position -> no swap.
    #
    # Result:
    # [0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
    #
    # ----------------------------------------------------------------
    # OUTER LOOP ITERATION 9 (cur_pos = 9)
    # Only one element left -> already sorted.
    #
    # Final sorted list:
    # [0, 8, 11, 12, 47, 60, 62, 74, 97, 98]
    #
    # ----------------------------------------------------------------
    # Print final result for visual confirmation.
    # ----------------------------------------------------------------

    print("Final sorted list (after manual selection sort):")
    print("[0, 8, 11, 12, 47, 60, 62, 74, 97, 98]")


def q5():
    clear_screen()

    # ------------------------------------------------------
    # 5. Show how the following numbers can be sorted using
    #    the selection sort:
    #
    #    74   92   18   47   40   58    0   36   29   25
    #
    # ------------------------------------------------------

    my_list = [74, 92, 18, 47, 40, 58, 0, 36, 29, 25]

    for cur_pos in range(len(my_list)):
        min_pos = cur_pos

        for scan_pos in range(cur_pos + 1, len(my_list)):
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    print(my_list)


def q6():
    clear_screen()

    # -------------------------------------------------------------------
    # 6. Show how the following numbers can be sorted using the
    #    INSERTION sort. (Note: If you think the 0 gets immediately
    #    sorted into position, you are doing it wrong. Go back and
    #    re-read how this sort works.)
    #
    #    74   92   18   47   40   58    0   36   29   25
    # -------------------------------------------------------------------

    my_list = [74, 92, 18, 47, 40, 58, 0, 36, 29, 25]

    for cur_pos in range(1, len(my_list)):
        key = my_list[cur_pos]
        scan_pos = cur_pos - 1

        while scan_pos >= 0 and my_list[scan_pos] > key:
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key

    print(my_list)


def q7():
    clear_screen()

    # -------------------------------------------------------
    # 7. Show how the following numbers can be sorted using
    #    the insertion sort:
    #
    #    37   11   14   50   24    7   17   88   99    9
    # --------------------------------------------------------

    my_list = [37, 11, 14, 50, 24, 7, 17, 88, 99, 9]

    for cur_pos in range(1, len(my_list)):
        key = my_list[cur_pos]
        scan_pos = cur_pos - 1

        while scan_pos >= 0 and my_list[scan_pos] > key:
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key

    print(my_list)

def q8():
    clear_screen()

    # ----------------------------------------------------------------
    # 8. Explain what min_pos does in the selection.
    # ----------------------------------------------------------------

    print("Explain what min_pos does in the selection")
    print()
    print("min_pos keeps track of the index of the smallest value found")
    print("during the inner loop scan. When the scan finishes, min_pos")
    print("tells the algorithm which position should be swapped into")
    print("the current outer-loop position (cur_pos).")


def q9():
    clear_screen()

    # ----------------------------------------------------------------
    # 9. Explain what cur_pos does in the selection sort.
    # ----------------------------------------------------------------

    print("Explain what cur_pos does in the selection sort")
    print()
    print("cur_pos marks the current position in the list where the")
    print("next smallest value should be placed. Each outer-loop")
    print("iteration moves cur_pos one step to the right, shrinking")
    print("the unsorted portion of the list.")


def q10():
    clear_screen()

    # ----------------------------------------------------------------
    # 10. Explain what scan_pos does in the selection sort.
    # ----------------------------------------------------------------

    print("Explain what scan_pos does in the selection sort")
    print()
    print("scan_pos moves through the unsorted portion of the list")
    print("from left to right, comparing values to find the smallest.")
    print("It is the index used by the inner loop to locate the")
    print("minimum value that will be swapped into cur_pos.")


def q11():
    clear_screen()

    # ----------------------------------------------------------------
    # 11. Explain what key_pos and key_value are in the insertion sort.
    # ----------------------------------------------------------------

    print("Explain what key_pos and key_value are in the insertion sort")
    print()
    print("key_pos is the index of the value currently being inserted")
    print("into the sorted portion of the list. key_value is the actual")
    print("number stored at that index. During insertion sort, key_value")
    print("is temporarily held while larger values are shifted right.")


def q12():
    clear_screen()

    # ---------------------------------------------------------------
    # 12. Explain scan_pos in the insertion sort.
    # ---------------------------------------------------------------

    print("Explain scan_pos in the insertion sort")
    print()
    print("scan_pos moves left through the sorted portion of the list")
    print("checking whether each value is greater than key_value. As long")
    print("as values are larger, scan_pos shifts them right. When scan_pos")
    print("finds a value not larger than key_value, the insertion point")
    print("has been found.")


def q13():
    clear_screen()

    # ------------------------------------------------------------------
    # 13. Look at the example sort program in the examples section here:
    #
    #     http://programarcadegames.com/python_examples/f.php?file=sorting_examples.py
    #
    #     Modify the sorts to print the number of times the inside
    #     loop is run, and the number of times the outside loop is
    #     run. Modify the program to work with a list of 100.
    #
    #     Paste the code you used here. Run the program and list the
    #     numbers you got here. (Don't forget this part!)
    # --------------------------------------------------------------------

    import random

    # Create two lists of the same random numbers
    list1 = []
    list2 = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list1.append(new_number)
        list2.append(new_number)

    # ----------------------------------------------------------------
    # OPTIONAL: Uncomment these lines to see the original random list
    # ----------------------------------------------------------------
    # print("Original List:")
    # print(list1)
    # print()

    # ----------------------------------------------------------------
    # Selection Sort (with loop counters)
    # ----------------------------------------------------------------
    sel_outer = 0
    sel_inner = 0

    for cur_pos in range(len(list1)):
        sel_outer += 1
        min_pos = cur_pos

        for scan_pos in range(cur_pos + 1, len(list1)):
            sel_inner += 1
            if list1[scan_pos] < list1[min_pos]:
                min_pos = scan_pos

        temp = list1[min_pos]
        list1[min_pos] = list1[cur_pos]
        list1[cur_pos] = temp

    print("Selection Sort:")
    print("Outer loop count:", sel_outer)
    print("Inner loop count:", sel_inner)
    print("Sorted list:", list1)
    print()

    # ---------------------------------------------------------------
    # Insertion Sort (with loop counters)
    # ---------------------------------------------------------------
    ins_outer = 0
    ins_inner = 0

    for key_pos in range(1, len(list2)):
        ins_outer += 1
        key_value = list2[key_pos]
        scan_pos = key_pos - 1

        while scan_pos >= 0 and list2[scan_pos] > key_value:
            ins_inner += 1
            list2[scan_pos + 1] = list2[scan_pos]
            scan_pos -= 1

        list2[scan_pos + 1] = key_value

    print("Insertion Sort:")
    print("Outer loop count:", ins_outer)
    print("Inner loop count:", ins_inner)
    print("Sorted list:", list2)


if __name__ == "__main__":
    q1()    # <- run Question 1
    # q2()    # <- run Question 2
    # q3()    # <- run Question 3
    # q4()    # <- run Question 4
    # q5()    # <- run Question 5
    # q6()    # <- run Question 6
    # q7()    # <- run Question 7
    # q8()    # <- run Question 8
    # q9()    # <- run Question 9
    # q10()   # <- run Question 10
    # q11()   # <- run Question 11
    # q12()   # <- run Question 12
    # q13()   # <- run Question 13
