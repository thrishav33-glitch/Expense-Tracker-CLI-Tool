import csv

FILE_NAME = "expenses.csv"

def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if file.tell() == 0:
            writer.writerow(["Date", "Category", "Amount"])

        writer.writerow([date, category, amount])

    print("Expense added successfully!")

def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)

            print("\n----- Expense Records -----")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("No expense records found.")

def total_spending():
    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                total += float(row["Amount"])

        print(f"\nTotal Spending: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expense records found.")

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Spending")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Try again.")
