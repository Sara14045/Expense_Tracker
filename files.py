import json  # Get JSON tools.
import csv  # Get CSV tools.
import math  # Get number checking.
from datetime import datetime  # Get date checking.

# Save the expense list to a JSON file.
def save(data):  # Receive the expense list.
    name = input("File to save (example: expenses.json): ").strip()  # Read the file name.
    try:  # Try saving the file.
        with open(name, "w", encoding="utf-8") as f:  # Open the file for writing.
            json.dump(data, f, indent=4)  # Write the list as JSON.
        print("Expenses saved.")  # Confirm the save.
    except OSError:  # Catch a file error.
        print("Could not save that file.")  # Explain the problem.

# Open a JSON file and check its expenses.
def load():  # Start the open function.
    name = input("File to open: ").strip()  # Read the file name.
    try:  # Try reading the file.
        with open(name, "r", encoding="utf-8") as f:  # Open the file for reading.
            data = json.load(f)  # Read the JSON data.
        if not isinstance(data, list):  # Check for a list.
            raise ValueError  # Reject the wrong format.
        for e in data:  # Check each expense.
            if not isinstance(e, dict):  # Check for an expense dictionary.
                raise ValueError  # Reject the wrong format.
            d = e.get("date")  # Get the date.
            c = e.get("category")  # Get the category.
            a = e.get("amount")  # Get the amount.
            n = e.get("note")  # Get the note.
            if not isinstance(d, str):  # Check the date type.
                raise ValueError  # Reject the wrong type.
            x = datetime.strptime(d, "%Y-%m-%d")  # Check the calendar date.
            if x.strftime("%Y-%m-%d") != d:  # Check the date format.
                raise ValueError  # Reject the wrong format.
            if not isinstance(c, str) or not c.strip():  # Check the category.
                raise ValueError  # Reject a bad category.
            if type(a) not in (int, float):  # Check the amount type.
                raise ValueError  # Reject a nonnumeric amount.
            if not math.isfinite(a) or a <= 0:  # Check the amount value.
                raise ValueError  # Reject a bad amount.
            if not isinstance(n, str):  # Check the note type.
                raise ValueError  # Reject a bad note.
        print("Expenses opened. Current list replaced.")  # Confirm opening.
        return data  # Return the loaded list.
    except (OSError, ValueError, UnicodeError, OverflowError):  # Catch file and data errors.
        print("Could not open a valid expense file.")  # Explain the problem.
        return None  # Keep the current list unchanged.

# Export all current expenses to a CSV file for Excel.
def export(data):  # Receive the expense list.
    name = input("CSV file name (example: expenses.csv): ").strip()  # Read the file name.
    try:  # Try writing the CSV file.
        with open(name, "w", newline="", encoding="utf-8-sig") as f:  # Open the file for Excel.
            w = csv.writer(f)  # Make a CSV writer.
            w.writerow(["Date", "Category", "Amount", "Note"])  # Write column headings.
            for e in data:  # Visit each expense.
                w.writerow([e["date"], e["category"], f"{e['amount']:.2f}", e["note"]])  # Write one expense.
        print("CSV exported.")  # Confirm the export.
    except OSError:  # Catch a file error.
        print("Could not export that file.")  # Explain the problem.
