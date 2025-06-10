'''
Assignment 5
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.
=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
'''
# Prompt user for time duration and validate it is non-negative
try:
    hours = float(input("Enter time duration in hours: "))

    if hours < 0:
        print("Time duration cannot be negative.")
    else:
        # Convert to minutes and seconds
        minutes = hours * 60
        seconds = hours * 3600

        # Output the converted time
        print(f"{hours} hour(s) is {int(minutes)} minutes and {int(seconds)} seconds.")
except ValueError:
    print("Invalid input. Please enter a numeric value for hours.")
