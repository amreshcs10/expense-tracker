import os
import csv
from datetime import datetime
from pathlib import Path

# List to store all expenses in memory
expenses = []

# Global variable for user's budget
monthly_budget = 0.0

def get_expense_file_path():
    """
    Returns the full path to the expense CSV file inside src/resources.
    Ensures the directory exists even when run from outside src.
    """
    try:
        base_dir = Path(__file__).resolve().parent.parent
    except NameError:
        base_dir = Path.cwd()

    resource_dir = base_dir / "src" / "resources"
    resource_dir.mkdir(parents=True, exist_ok=True)

    return resource_dir / "personal_expenses.csv"


# Location to store expenses, keeping this in a data seprate folder
PERSONAL_EXPENSES_FILE = get_expense_file_path()

def add_expense():
    """
    Prompts the user to input expense details.
    Validates input and appends the new expense to the 'expenses' list.
    Raises exceptions for invalid inputs; handled by main_menu() if thwron here.
    """
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    datetime.strptime(date, "%Y-%m-%d")  # Validates date format

    category = input("Enter the category (e.g., Food, Travel): ").strip()
    if not category:
        raise ValueError("Category cannot be empty.")

    amount = float(input("Enter the amount spent: ").strip())
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    description = input("Enter a brief description: ").strip()
    if not description:
        raise ValueError("Description cannot be empty.")

    expenses.append({
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    })
    print("================================================================================")
    print("Success: Expense added successfully at location ", PERSONAL_EXPENSES_FILE)
    print("================================================================================")

def view_expenses():
    """
    Displays all recorded expenses in a readable format.
    """
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n All Expenses:")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. Date: {exp['date']}, Category: {exp['category']}, "
              f"Amount: ₹{exp['amount']:.2f}, Description: {exp['description']}")


def track_budget():
    """
    Prompts the user to set a budget if not already set.
    Displays total spent and remaining budget.
    Warns if the user has exceeded the budget.
    """
    global monthly_budget

    if monthly_budget == 0.0:
        budget_input = input("Enter your monthly budget: ").strip()
        try:
            monthly_budget = float(budget_input)
            if monthly_budget <= 0:
                print("Budget must be greater than zero.")
                monthly_budget = 0.0
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

    total_spent = sum(exp['amount'] for exp in expenses)
    remaining = monthly_budget - total_spent

    print(f"\n💰 Total Spent: ₹{total_spent:.2f}")
    print(f"📉 Budget Remaining: ₹{remaining:.2f}")

    if remaining < 0:
        print("Warning: Budget Exceeded!")


def save_expenses():
    """
    Saves all expenses to a CSV file named 'expenses.csv'.
    """
    with open(PERSONAL_EXPENSES_FILE, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
        writer.writeheader()
        writer.writerows(expenses)


def load_expenses():
    """
    Loads expenses from 'expenses.csv' (if available) into the program.
    Skips if file not found (first-time use).
    """
    try:
        with open(PERSONAL_EXPENSES_FILE, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['amount'] = float(row['amount'])  # Convert amount from string to float
                expenses.append(row)
    except FileNotFoundError:
        pass  # Safe to skip if file doesn't exist


def main_menu():
    """
    Main interaction loop for the user.
    Handles navigation and centralized exception handling.
    """
    load_expenses()

    while True:
        print("\nPersonal Expense Tracker(Enter your input): ")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        try:
            if choice == '1':
                add_expense()
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                track_budget()
            elif choice == '4':
                save_expenses()
                print("================================================================================")
                print("Success: Expenses saved to file.")
                print("================================================================================\n")
            elif choice == '5':
                save_expenses()
                print("================================================================================")
                print("Exiting. Expenses saved at location ", PERSONAL_EXPENSES_FILE)
                print("================================================================================\n")
                break
            else:
                print("================================================================================")
                print("Invalid choice. Please enter a number from 1 to 5.")
                print("================================================================================\n")

        except ValueError as ve:
            print("================================================================================")
            print(f"Input Error: {ve}")
            print("================================================================================\n")
        except Exception as e:
            print("================================================================================")
            print(f"Unexpected error occurred: {e}")
            print("================================================================================\n")


# Entry point for the program
if __name__ == "__main__":
    main_menu()
