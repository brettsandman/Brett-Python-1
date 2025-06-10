'''Assignment 4
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.
============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
'''
# Prompt user to input coordinates and handle errors
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    # Calculate the distance between two points
    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    # Output the result
    print(f"The distance between the two points is: {distance:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for all coordinates.")
