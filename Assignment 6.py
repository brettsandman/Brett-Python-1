'''
Assignment 6
Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.
==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.
'''
# Define fixed exchange rates (example: USD to EUR, GBP, JPY)
exchange_rates = {
    "EUR": 0.85,
    "GBP": 0.75,
    "JPY": 110.0
}

# Prompt user to enter amount and currency
try:
    amount = float(input("Enter amount in USD: "))
    target_currency = input("Enter target currency (EUR, GBP, JPY): ").upper()

    # Convert and display result if currency is supported
    if target_currency in exchange_rates:
        converted = amount * exchange_rates[target_currency]
        print(f"{amount} USD is {converted:.2f} {target_currency}")
    else:
        print("Unsupported currency. Please choose EUR, GBP, or JPY.")
except ValueError:
    print("Invalid input. Please enter a numeric value for the amount.")
