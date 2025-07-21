from expense import Expense
from database import DatabaseManager

db = DatabaseManager()

def show_menu():
    print("\n ===PERSONAL EXPENSE TRACKER ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Exit")

def add_expense():
    amount = input("Enter amount : ₹")
    category = input("Enter category : ")
    date = input("Enter date (YYY-MM-DD) : ")
    note = input("Enter a note (optional) : ")

    new_expense = Expense(amount, category, date, note)
    db.insert_expense(new_expense.amount,new_expense.category,new_expense.date,new_expense.note)
    print("Expense added...")  


def view_expenses():
    all_expenses = db.fetch_all_expenses()

    print("\n--- Expenses ---")
    for e in all_expenses:
        print(f"{e[3]} | {e[2]} | ₹{e[1]} | {e[4]}")

while True:
    show_menu()
    choice = input("Choose an option (1-3): ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        db.close()
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option.")
