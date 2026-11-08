from datetime import datetime  # Get date checking.
import math  # Get number checking.

# Ask for expense details and add them to the list.
def add(data):  # Receive the expense list.
    d = input("Date (YYYY-MM-DD): ").strip()  # Read the date.
    try:  # Try checking the date.
        x = datetime.strptime(d, "%Y-%m-%d")  # Check the calendar date.
        if x.strftime("%Y-%m-%d") != d:  # Check the date format.
            raise ValueError  # Reject the wrong format.
    except ValueError:  # Catch an invalid date.
        print("Enter a valid date as YYYY-MM-DD.")  # Explain the problem.
        return  # Stop adding.
    c = input("Category: ").strip()  # Read the category.
    if c == "":  # Check for an empty category.
        print("Category cannot be empty.")  # Explain the problem.
        return  # Stop adding.
    try:  # Try reading the amount.
        a = float(input("Amount: "))  # Convert the amount to a number.
    except ValueError:  # Catch nonnumeric text.
        print("Enter a number.")  # Explain the problem.
        return  # Stop adding.
    if not math.isfinite(a) or a <= 0:  # Check for a positive finite amount.
        print("Enter a positive number.")  # Explain the problem.
        return  # Stop adding.
    a = round(a, 2)  # Keep two decimal places.
    if a == 0:  # Check for an amount rounded to zero.
        print("Amount must be at least 0.01.")  # Explain the problem.
        return  # Stop adding.
    n = input("Note (optional): ").strip()  # Read a note.
    e = {"date": d, "category": c, "amount": a, "note": n}  # Make one expense.
    data.append(e)  # Add the expense to the list.
    print("Expense added.")  # Confirm the new expense.

# Print each expense and the total amount.
def show(data):  # Receive the expense list.
    if not data:  # Check for an empty list.
        print("No expenses yet.")  # Show an empty message.
        return  # Stop printing.
    total = 0  # Start the total at zero.
    for e in data:  # Visit each expense.
        print(f"{e['date']} | {e['category']} | {e['amount']:.2f} | {e['note']}")  # Print one expense.
        total = total + e["amount"]  # Add its amount to the total.
    print(f"Total: {total:.2f}")  # Print the total.
