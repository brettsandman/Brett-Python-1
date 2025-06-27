# Inventory list to hold all items
inventory = []

# Function to add a new item
def add_item(name, price, quantity, category):
    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }
    inventory.append(item)
    print(f"Item '{name}' added successfully.")

# Function to update an existing item
def update_item(name, price=None, quantity=None, category=None):
    for item in inventory:
        if item['name'].lower() == name.lower():
            if price is not None:
                item['price'] = price
            if quantity is not None:
                item['quantity'] = quantity
            if category is not None:
                item['category'] = category
            print(f"Item '{name}' updated successfully.")
            return
    print(f"Item '{name}' not found.")

# Function to view all items
def view_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    for item in inventory:
        print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}, Category: {item['category']}")

# Function to remove an item
def remove_item(name):
    global inventory
    new_inventory = [item for item in inventory if item['name'].lower() != name.lower()]
    if len(new_inventory) < len(inventory):
        inventory = new_inventory
        print(f"Item '{name}' removed successfully.")
    else:
        print(f"Item '{name}' not found.")

# Function to search by category
def search_by_category(category):
    found = False
    for item in inventory:
        if item['category'].lower() == category.lower():
            print(f"Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            found = True
    if not found:
        print(f"No items found in category '{category}'.")

# Main loop to interact with the user
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            category = input("Enter item category: ")
            add_item(name, price, quantity, category)

        elif choice == '2':
            name = input("Enter item name to update: ")
            try:
                price = float(input("Enter new price (or leave blank): ") or None)
            except ValueError:
                price = None
            try:
                quantity = int(input("Enter new quantity (or leave blank): ") or None)
            except ValueError:
                quantity = None
            category = input("Enter new category (or leave blank): ") or None
            update_item(name, price, quantity, category)

        elif choice == '3':
            view_inventory()

        elif choice == '4':
            name = input("Enter item name to remove: ")
            remove_item(name)

        elif choice == '5':
            category = input("Enter category to search: ")
            search_by_category(category)

        elif choice == '6':
            print("Exiting Inventory Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
