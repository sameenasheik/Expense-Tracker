import json
from datetime import datetime

with open("expenses.json", "r") as file:
    expenses = json.load(file)

choice = 0

while choice != 7:

    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Category-wise Total")
    print("6. Monthly Total")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid menu number!")
        continue

    # ADD EXPENSE
    if choice == 1:

        while True:
            try:
                amount = float(input("Enter amount: "))

                if amount > 0:
                    break
                else:
                    print("Amount must be greater than zero!")

            except ValueError:
                print("Please enter a valid number!")

        while True:
            category = input("Enter Category: ").strip()

            if category:
                break
            else:
                print("Category cannot be empty!")

        while True:
            date = input("Enter date (YYYY-MM-DD): ")

            try:
                datetime.strptime(date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date! Please use YYYY-MM-DD.")

        while True:
            note = input("Enter note: ").strip()

            if note:
                break
            else:
                print("Note cannot be empty!")

        expense = {
            "amount": amount,
            "category": category,
            "date": date,
            "note": note
        }

        expenses.append(expense)

        with open("expenses.json", "w") as file:
            json.dump(expenses, file)

        print("Expense added successfully")

    # VIEW ALL EXPENSES
    elif choice == 2:

        if expenses == []:
            print("No expenses found")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"Expense {i}")
                print(f"Amount : {expense['amount']}")
                print(f"Category : {expense['category']}")
                print(f"Date : {expense['date']}")
                print(f"Note : {expense['note']}")

    # EDIT EXPENSE
    elif choice == 3:

        if expenses == []:
            print("No expenses found")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"Expense {i}")
                print(f"Amount : {expense['amount']}")
                print(f"Category : {expense['category']}")
                print(f"Date : {expense['date']}")
                print(f"Note : {expense['note']}")

            while True:
                try:
                    select_expense = int(input("Select an expense: "))

                    if 1 <= select_expense <= len(expenses):
                        break
                    else:
                        print("Invalid expense number!")

                except ValueError:
                    print("Please enter a valid number!")

            while True:
                expense_key = input(
                    "What do you want to edit? [amount, category, date, note]: "
                ).strip().lower()

                if expense_key in ["amount", "category", "date", "note"]:
                    break
                else:
                    print("Invalid field name!")

            if expense_key == "amount":

                while True:
                    try:
                        new_amount = float(input("Enter new amount: "))

                        if new_amount > 0:
                            break
                        else:
                            print("Amount must be greater than zero!")

                    except ValueError:
                        print("Please enter a valid number!")

                expenses[select_expense - 1]["amount"] = new_amount

            elif expense_key == "category":

                while True:
                    new_category = input("Enter new category: ").strip()

                    if new_category:
                        break
                    else:
                        print("Category cannot be empty!")

                expenses[select_expense - 1]["category"] = new_category

            elif expense_key == "date":

                while True:
                    new_date = input("Enter new date (YYYY-MM-DD): ")

                    try:
                        datetime.strptime(new_date, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date! Please use YYYY-MM-DD.")

                expenses[select_expense - 1]["date"] = new_date

            elif expense_key == "note":

                while True:
                    new_note = input("Enter new note: ").strip()

                    if new_note:
                        break
                    else:
                        print("Note cannot be empty!")

                expenses[select_expense - 1]["note"] = new_note

            with open("expenses.json", "w") as file:
                json.dump(expenses, file)

            print("The expense has been updated successfully")

    # DELETE EXPENSE
    elif choice == 4:

        if expenses == []:
            print("No expenses found")

        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"Expense {i}")
                print(f"Amount : {expense['amount']}")
                print(f"Category : {expense['category']}")
                print(f"Date : {expense['date']}")
                print(f"Note : {expense['note']}")

            while True:
                try:
                    delete_expense = int(input("Enter expense number to delete: "))

                    if 1 <= delete_expense <= len(expenses):
                        break
                    else:
                        print("Invalid expense number!")

                except ValueError:
                    print("Please enter a valid number!")

            expenses.pop(delete_expense - 1)

            with open("expenses.json", "w") as file:
                json.dump(expenses, file)

            print("Expense deleted successfully")

    # CATEGORY-WISE TOTAL
    elif choice == 5:

        if expenses == []:
            print("No expenses found")

        else:
            category_totals = {}

            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]

                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

            for category, total in category_totals.items():
                print(f"{category} : ₹{total}")

    # MONTHLY TOTAL
    elif choice == 6:

        if expenses == []:
            print("No expenses found")

        else:
            monthly_total = 0

            while True:
                month = input("Enter month [YYYY-MM]: ")

                try:
                    datetime.strptime(month, "%Y-%m")
                    break
                except ValueError:
                    print("Invalid month! Please use YYYY-MM.")

            for expense in expenses:
                if expense['date'].startswith(month):
                    monthly_total += expense["amount"]

            print("Total monthly amount:", monthly_total)

    # EXIT
    elif choice == 7:
        print("Exiting Expense Tracker!")

    else:
        print("Invalid choice")