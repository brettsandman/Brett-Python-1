'''
Assignment 13
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.
===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
'''
# Step 1: Prompt the user to enter a string
user_input = input("Enter a string to check if it's a palindrome: ")

# Step 2: Normalize the string (remove spaces and make lowercase for accurate comparison)
normalized = ''.join(user_input.lower().split())

# Step 3: Use loop to compare characters from both ends
is_palindrome = True
length = len(normalized)
for i in range(length // 2):
    if normalized[i] != normalized[length - 1 - i]:
        is_palindrome = False
        break

# Step 4: Display the result
if is_palindrome:
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
