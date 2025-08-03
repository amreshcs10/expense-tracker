# expense_tracker.py

"""
Personal Expense Tracker

A command-line tool for individuals to log daily expenses, categorize them,
track spending against a monthly budget, and persist data using CSV files.
"""

import csv
import os
from datetime import datetime

# File to store expenses
EXPENSES_FILE = 'expenses.csv'

# In-memory list of expenses
expenses = []

# Global variable to hold monthly budget
monthly_budget = None


def load_expenses():
    """
    Load expenses from a CSV file and store them in the `expenses` list.
    Skips invalid or corrupted rows.
    """
    if not os.path.exists(EXPENSES_FILE):
        return
    with open(EXPENSES_FILE, newline='', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                row['amount'] = float(row['amount'])
                expenses.append(row)
            except (KeyError, ValueError):
                continue


def save_expenses():
    """
    Save the current list of expenses to a CSV file.
    """
    with open(EXPENSES_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)


def add_expense():
    """
    Prompt the user for details of a new expense and add it to the list.
    Validates date format and numeric amount.
    """
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Travel): ")

    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    description = input("Enter a brief description: ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    print("✅ Expense added successfully.")


def view_expenses():
    """
    Display all stored expenses in a readable format.
    Skips incomplete entries.
    """
    if not expenses:
        print("No expenses to display.")
        return

    print("\nAll Expenses:")
    for exp in expenses:
        if all(k in exp for k in ['date', 'category', 'amount', 'description']):
            print(f"{exp['date']} | {exp['category']} | ${exp['amount']:.2f} | {exp['description']}")
        else:
            print("⚠️ Incomplete expense entry found. Skipping.")


def set_budget():
    """
    Prompt the user to set a monthly budget.
    """
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"✅ Monthly budget set to ${monthly_budget:.2f}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")


def track_budget():
    """
    Calculate and display the total spending against the budget.
    Shows remaining balance or a warning if the budget is exceeded.
    """
    if monthly_budget is None:
        print("Monthly budget not set. Please set it first.")
        return

    total_spent = sum(exp['amount'] for exp in expenses)
    print(f"\n💰 Total expenses so far: ${total_spent:.2f}")

    if total_spent > monthly_budget:
        print("⚠️ Warning: You have exceeded your budget!")
    else:
        print(f"✅ You have ${monthly_budget - total_spent:.2f} left for the month.")


def main_menu():
    """
    Display an interactive menu for the user to navigate the tracker.
    """
    load_expenses()

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if monthly_budget is None:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
            print("✅ Expenses saved successfully.")
        elif choice == '5':
            save_expenses()
            print("👋 Exiting... Expenses saved.")
            break
        else:
            print("❌ Invalid choice. Please try again.")


# Entry point
if __name__ == '__main__':
    main_menu()
