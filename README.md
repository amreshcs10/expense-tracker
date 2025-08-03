# 💸 Personal Expense Tracker

## 1. Project Overview
A lightweight Python-based CLI application to help individuals track daily expenses, monitor spending habits, and stay within a defined monthly budget.  
It stores data in a CSV format and is designed for simplicity, portability, and future extensibility toward data analysis.

---

## 2. Core Features

- ✅ **Add Expense** – Record expenses with date, category, amount, and description.  
- 📋 **View Expenses** – Display all recorded expenses in a readable list.  
- 💰 **Track Budget** – Set a monthly budget, view total spending, and get alerts when overspending.  
- 💾 **Save Expenses** – Persist all expenses to a CSV file for long-term storage.  
- 📂 **Load Existing Data** – Automatically load past data at startup from the CSV.  
- 🛡️ **Error Handling** – Centralized input validation and user-friendly error messages.  

---

## 3. Design Highlights

- 🧱 **Modular Functions** – Each task (add, view, track, save, load) is cleanly separated.  
- 🔐 **Exception-Safe** – Uses `try-except` blocks in `main_menu()` for graceful error handling.  
- 📁 **Separation of Concerns** – Data file path stored in a dedicated `data/` folder.  
- 🗃️ **Lightweight CSV Storage** – No external database dependency.  

---

## 4. Usage Instructions

### ▶️ Run the Application
python src/personal_expense_tracker.py

## 5. Menu Descriptions:

- **1️⃣ Add Expense** – Input details like date, category, amount, and description to log an expense.
- **2️⃣ View Expenses** – Display all recorded expenses in an easy-to-read list.
- **3️⃣ Track Budget** – Set or view your monthly budget and check if your spending exceeds it.
- **4️⃣ Save Expenses** – Save all current session expenses to the CSV file.
- **5️⃣ Exit** – Automatically saves and exits the application.

---

## 6. 🗂️ Output Location

All expense records entered through the CLI are saved automatically in a CSV file: data/personal_expenses.csv




## 7  Requirements
Python 3.7.x+