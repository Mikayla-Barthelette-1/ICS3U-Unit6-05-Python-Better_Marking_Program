#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program finds the average of a list of marks


def average_of_marks(marks, loop_counter):
    # this function finds the average of the marks

    amount_of_numbers = loop_counter - 1
    the_sum = 0
    for a_single_mark in marks:
        the_sum = the_sum + a_single_mark

    the_average = the_sum / amount_of_numbers

    return the_average


def main():
    # this function calls other functions

    marks = []

    # input
    print("Please enter 1 mark at a time. Enter -1 to end.")
    print("")

    loop_counter = 0

    while True:
        user_input = input("What is your mark? (as %): ")
        loop_counter = loop_counter + 1
        try:
            temp_mark = int(user_input)
            if temp_mark == -1:
                break
            elif temp_mark < 0 or temp_mark > 100:
                print("\nPlease enter a mark between 0 - 100.")
                print("\nDone.")
                exit()
            marks.append(temp_mark)
        except (Exception):
            print("\nInvalid input.")
            print("\nDone.")
            exit()
        finally:
            None

    average = average_of_marks(marks, loop_counter)
    print("\nThe average is {0}% ".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
