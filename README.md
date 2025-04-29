![Screenshot from 2025-04-29 16-22-32](https://github.com/user-attachments/assets/ae6aee03-0492-4b83-8fd3-4a623aeb8ef9)
# Budget Planner

A simple Python 3 budget calculator that helps you track your income, expenses, and allocate remaining funds to different categories.

## Features

- Calculate your budget based on your total income
- Track regular expenses
- Load expenses from a file (expenses.txt)
- Allocate remaining funds to optional categories
- View a comprehensive budget summary including percentages of income

## Usage

Run the program with Python 3:

```bash
python3 budget.py
```


### Expense File Format

You can create an `expenses.txt` file with your regular expenses in the following format:

```Expense Name -$Amount```

For example:

```
Rent -$1200
Utilities -$150
Phone -$50
```

## Example

```Welcome to the Budget Planner!
Enter your total paycheck amount: $3000
Starting amount: $3000.00
Load expenses from 'expenses.txt'? (y/n): y
Loaded Gym: $30.00. Remaining: $2970.00
Loaded Car Wash: $42.00. Remaining: $2928.00
...
You have $2171.00 remaining. Let's allocate it to optional categories.
Enter a category name (or 'done' to finish): Savings
What percentage of your remaining $2171.00 would you like to allocate to Savings? (0-100): 50
Allocated $1085.50 to Savings
Remaining: $1085.50
...
===== BUDGET SUMMARY =====
Total Income: $3000.00
EXPENSES:
Gym: $30.00
Car Wash: $42.00
...
Total Expenses: $829.00 (27.6% of income)
OPTIONAL ALLOCATIONS:
Savings: $1085.50
...
Total Optional Allocations: $2171.00 (72.4% of income)
```
