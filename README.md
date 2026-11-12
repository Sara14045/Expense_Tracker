# Expense Tracker

A simple Python console program for recording expenses. It can show expenses, filter them, save and open JSON files, and export CSV files for Excel.

## Requirements

- Python 3.6 or newer.
- No extra packages are needed.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Shows the menu and keeps the current expense list. |
| `expenses.py` | Adds, prints, and filters expenses. |
| `files.py` | Saves and opens JSON files and exports CSV files. |
| `README.md` | Explains how to run and use the program. |

Keep these files in the same folder.

## How to run

Open a terminal in the project folder and enter:

```bash
python main.py
```

If your computer uses `python3`, enter `python3 main.py` instead.

## Menu

| Choice | Action |
| --- | --- |
| 1 | Add an expense. |
| 2 | Show all current expenses and their total. |
| 3 | Filter expenses by date range, category, or both. |
| 4 | Save all current expenses to a JSON file. |
| 5 | Open a saved JSON expense file. |
| 6 | Export all current expenses to a CSV file. |
| 7 | Exit the program. |

## Add an expense

Choose `1` and enter details like these:

```text
Date (YYYY-MM-DD): 2026-11-08
Category: Food
Amount: 12.50
Note (optional): Lunch
```

Use a real date in `YYYY-MM-DD` format. The category cannot be empty. Enter a positive amount without a currency symbol. Amounts are rounded to two decimal places. The note can be blank.

Choose `2` to see the expense and the total:

```text
2026-11-08 | Food | 12.50 | Lunch
Total: 12.50
```

## Filter expenses

Choose `3`. Enter a start date, an end date, and a category as needed.

- Leave either date blank for no limit on that side.
- Leave the category blank to include every category.
- Leave all three fields blank to show all expenses.
- Both boundary dates are included.
- Categories match the full category name and ignore capital letters. For example, `food` matches `Food`.
- The start date must be before or equal to the end date.

The program prints matching expenses and their total. Filtering keeps the original list unchanged.

## Save and open JSON

Choose `4` and enter a file name such as `expenses.json` to save the current list.

To use it later, start the program, choose `5`, and enter the same file name. Then choose `2` to see the loaded expenses.

Opening a valid file replaces the current list. Save any expenses you want to keep before opening another file. If opening fails, the current list stays unchanged.

## Export CSV

Choose `6` and enter a file name such as `expenses.csv`. Open the exported file in Microsoft Excel or another spreadsheet program.

The columns are `Date`, `Category`, `Amount`, and `Note`. CSV export includes all current expenses, even after filtering. An empty list produces a file containing only the column headings.

## File handling

- Saving is manual. Use option `4` before exiting to keep expenses for reopening in this program.
- Saving JSON or exporting CSV overwrites an existing file with the same name.
- File names are relative to the terminal's current folder unless you enter a full path.
- The program starts with an empty list each time. Use option `5` to open saved expenses.
- Amounts use Python floating-point numbers. Use one currency consistently; the program does not convert currencies.

