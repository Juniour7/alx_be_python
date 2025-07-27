def display_menu():
    """Prints the main menu options to the console."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager application.
    Initializes an empty list and enters a loop to process user commands.
    """
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the name of the item to add: ").strip()
            if item:  # Ensure the user entered something
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the name of the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' was not found in the list.")

        elif choice == '3':
            # Display the shopping list
            print("\n--- Your Shopping List ---")
            if not shopping_list:
                print("The list is currently empty.")
            else:
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            print("--------------------------")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()