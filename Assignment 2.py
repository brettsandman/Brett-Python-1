'''
Assignment 2
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.
=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''
# Prompt the user to enter the length and width of the rectangle.
# Use try-except to catch non-numeric input errors.
try:
    length = float(input("Enter the length of the rectangle: "))  # Get length as a float
    width = float(input("Enter the width of the rectangle: "))    # Get width as a float

    # Check if the values are positive
    if length <= 0 or width <= 0:
        print("Error: Length and width must be positive numbers.")  # Validation failed
    else:
        # Calculate area using the formula: Area = Length * Width
        area = length * width

        # Display the calculated area rounded to 2 decimal places
        print(f"Area of the rectangle = {area:.2f}")

# Handle the case where user inputs non-numeric values
except ValueError:
    print("Error: Please enter numeric values for both length and width.")
