from datetime import date
import json
import os
FILE_NAME="tracker_expenses.json"
if os.path.exists(FILE_NAME):
    with open(FILE_NAME,"r")as file:
        expenses=json.load(file)
else:
    expenses = []
def add_expense():
    category = input("enter category(food/travel/bills):").strip()
    try:
        amount = float(input("enter amount in rs:"))
        if amount <=0:
            print("amount must be greater than zero.")
            return
        expense ={"date":date.today().isoformat(),"category":category,"amount":amount}
        expenses.append(expense)
        with open(FILE_NAME,"w")as file:
            json.dump(expenses,file,indent=4)
        print("expense added successfully!")
    except ValueError:
        print("error:enter a valid number.")
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return 
    for item in expenses:
        print(item["date"], item["category"], f"Rs.{item['amount']:.2f}")


def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total expenses: Rs.{total:.2f}")


def main():
    while True:
        print("\n--- EXPENSES TRACKER ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()                          

                            
