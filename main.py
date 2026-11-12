from expenses import add, show, find  # Get the expense functions.
from files import save, load, export  # Get the file functions.

# Show the menu and keep the expense list.
def main():  # Start the main function.
    data = []  # Make an empty expense list.
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
        if ch == "1":  # Check for adding.
            add(data)  # Add an expense.
        elif ch == "2":  # Check for printing.
            show(data)  # Print the expenses.
        elif ch == "3":  # Check for filtering.
            find(data)  # Print matching expenses.
        elif ch == "4":  # Check for saving.
            save(data)  # Save expenses as JSON.
        elif ch == "5":  # Check for opening.
            new = load()  # Read an expense file.
            if new is not None:  # Check that opening worked.
                data = new  # Replace the current list.
        elif ch == "6":  # Check for exporting.
            export(data)  # Write all expenses to CSV.
        elif ch == "7":  # Check for exit.
            print("Goodbye! Only saved expenses are kept.")  # Remind the user about saving.
            break  # Stop the loop.
        else:  # Handle an invalid choice.
            print("Please choose 1 to 7.")  # Ask for a valid choice.

if __name__ == "__main__":  # Check this file is run directly.
    main()  # Run the program.
