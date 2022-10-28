"""
Written by Nahom Atnafu
Last Modified: October 28/ 2022
This program takes a number as an input from the user and determines if that number is even or odd.
"""
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
