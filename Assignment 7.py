'''
Assignment 7
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.
===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.
'''
# Prompt user to input a year and validate it's numeric
try:
    year = int(input("Enter a year: "))

    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError:
    print("Invalid input. Please enter a valid numeric year.")
