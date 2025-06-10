'''
Assignment 1
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.
=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''
# Prompt the user to enter the principal amount, interest rate, and time period.
# Use try-except to catch non-numeric input errors.
try:
    principal = float(input("Enter the principal amount: "))  # Get the principal as a float
    rate = float(input("Enter the interest rate (in %): "))   # Get the interest rate as a float
    time = float(input("Enter the time period (in years): ")) # Get the time period as a float

    # Calculate simple interest using the formula (P * R * T) / 100
    simple_interest = (principal * rate * time) / 100

    # Display the result rounded to 2 decimal places
    print(f"Simple Interest = {simple_interest:.2f}")

# Handle the case where user inputs non-numeric values
except ValueError:
    print("Error: Please enter numeric values only for principal, rate, and time.")
