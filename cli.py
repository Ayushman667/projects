import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add_expense():
    category = input("Enter the category of your expense: ")
    amount = float(input("Enter the amount of your expense: "))
    date = input("Enter the date of your expense (DD-MM): ")

    with open("projects/expenses.txt", "a") as file:
        file.write(f"{category},{amount},{date}\n")

    flag = True
    while flag:
        command = input("Enter 'exit' to exit this window.\n")
        if command == 'exit':
            flag = False
            return


def view_expense():
    with open("projects/expenses.txt", "r") as file:
        expenses = file.readlines()

    if not expenses:
        print("No expenses found.")
        flag = True
        while flag:
            command = input("Enter 'Exit' to exit this window.\n")
            if command == 'exit':
                flag = False
                clear_screen()
                return

    for expense in expenses:
        expense_details = expense.strip().split(",")
        print(f"Category: {expense_details[0]}, Amount: {expense_details[1]}, Date: {expense_details[2]}")

    flag = True
    while flag:
        command = input("Enter 'Exit' to exit this window.")
        if command == "exit":
            flag = False
    clear_screen()

def search_expense():
    search_term = input("Enter the expense name to search: ")

    with open("projects/expenses.txt", "r") as file:
        expenses = file.readlines()

    found_expenses = [expense for expense in expenses if search_term.lower() in expense.lower()]

    if not found_expenses:
        print("No expenses found.")
        return

    for expense in found_expenses:
        expense_details = expense.strip().split(",")
        print(f"Category: {expense_details[0]}, Amount: {expense_details[1]}, Date: {expense_details[2]}")

def show_total_spending():
    with open("projects/expenses.txt", "r") as file:
        expenses = file.readlines()

    total_spending = sum(float(expense.strip().split(",")[1]) for expense in expenses)
    print(f"Total spending: {total_spending}")

def show_spending_by_category():
    with open("projects/expenses.txt", "r") as file:
        expenses = file.readlines()

    category_spending = {}
    for expense in expenses:
        expense_details = expense.strip().split(",")
        category = expense_details[0]
        amount = float(expense_details[1])
        if category in category_spending:
            category_spending[category] += amount
        else:
            category_spending[category] = amount

    for category, total in category_spending.items():
        print(f"Category: {category}, Total spending: {total}")

def delete_expense():
    expense_to_delete = input("Enter the expense name to delete: ")

    with open("projects/expenses.txt", "r") as file:
        expenses = file.readlines()

    with open("projects/expenses.txt", "w") as file:
        for expense in expenses:
            if expense_to_delete.lower() not in expense.lower():
                file.write(expense)

    print("Expense deleted successfully!")




flag = True
while flag:
    clear_screen()

    num = int(input("Press\n1. Add expense\n2. View expense\n3. Search expense\n4. Show total spending\n5. Show spending by category\n6. Delete expense\n7. Exit\n"))

    if num == 1:
        add_expense()

    if num == 2:
        view_expense()

    if num == 3:
        search_expense()

    if num == 4:
        show_total_spending()

    if num == 5:
        show_spending_by_category()

    if num == 6:
        delete_expense()

    if num == 7:
        clear_screen()
        flag = False