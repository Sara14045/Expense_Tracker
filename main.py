# Show the menu and read the user's choice.
def main():  # Start the main function.
    while True:  # Repeat the menu.
        print("\nExpense Tracker")  # Show the title.
        print("1. Add expense")  # Show the add option.
        print("2. Show expenses")  # Show the print option.
        print("3. Filter expenses")  # Show the filter option.
        print("4. Save JSON")  # Show the save option.
        print("5. Open JSON")  # Show the open option.
        print("6. Export CSV")  # Show the export option.
        print("7. Exit")  # Show the exit option.
        ch = input("Choose 1 to 7: ").strip()  # Read the choice.
        if ch == "7":  # Check for exit.
            print("Goodbye!")  # Show a goodbye message.
            break  # Stop the loop.
        elif ch in ["1", "2", "3", "4", "5", "6"]:  # Check other menu choices.
            print("Coming soon.")  # Mark features to add later.
        else:  # Handle an invalid choice.
            print("Please choose 1 to 7.")  # Ask for a valid choice.

if __name__ == "__main__":  # Check this file is run directly.
    main()  # Run the program.
