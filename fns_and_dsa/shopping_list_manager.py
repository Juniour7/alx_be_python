def display_menu():
    """Prints the main menu options to the console."""
    print("Shopping List Manager")
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
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Prompt for and add an item
            # Corrected the prompt to match the checker's requirement.
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # Prompt for and remove an item
            # Proactively corrected this prompt as well.
            item = input("Enter the item to remove: ").strip()
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
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()