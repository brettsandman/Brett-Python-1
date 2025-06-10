'''
Assignment 11
Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.
=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1.
'''
# Step 1: Prompt the user to enter a positive integer and handle non-numeric input
while True:
    try:
        num = int(input("Enter a positive integer to generate the Collatz sequence: "))
        if num > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Step 2: Generate the Collatz sequence using a loop
print("Collatz sequence:")
while num != 1:
    print(num, end=" → ")
    # Apply the Collatz rule
    if num % 2 == 0:
        num = num // 2
    else:
        num = num * 3 + 1
# Step 3: Print the final number in the sequence
print("1")
