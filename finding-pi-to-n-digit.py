# program to print the value of pi
# to the desired number of digits the user mentions

import math

print("Note: Please enter a number between 0 and 50.")
digits = input("How many values you desire after the decimal for PI? ")
value = 1

while value:

    if int(digits) > 0 and int(digits) < 50:
        print("\nThe desired value of PI: %.*f" % (int(digits), math.pi))
        repeat = input("Do you want to run the program again? Press y for yes or n for no. ")
        if repeat == 'y' or repeat == 'Y':
            digits = input("How many values you desire after the decimal for PI? ")
        elif repeat == 'n' or repeat == 'N':
            print("\nYou chose to exit the program. Good bye.")
            value = 0
        else:
            print("\nInvalid choice. Program terminated.")
            value = 0

    else:
        print("\nNumber out of range.")
        repeat = input("Do you want to run the program again? Press y for yes or n for no. ")
        if repeat == 'y' or repeat == 'Y':
            digits = input("How many values you desire after the decimal for PI? ")
        elif repeat == 'n' or repeat == 'N':
            print("\nYou chose to exit the program. Good bye.")
            value = 0
        else:
            print("\nInvalid choice. Program terminated.")
            value = 0
