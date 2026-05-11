import os



expenses = {"rent": 0,
            "groceries": 0,
            "utilities": 0,
            "others": 0}
income = 0
budget = 0


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_total_expenses(expenses):
    return sum(expenses.values())

def get_choices():
    return input("\n1. Add income\n2. Add expense\n3. View budget\n4. Analytics\n5. Investment potential\n6. Exit\nEnter your choice (1-6): ")

def show_expenses_menu():
    print("What would you like to change next? \n1. Rent\n2. Groceries\n3. Utilities\n4. Others\n5. Summary of expenses\n6. Home")

def get_budget(income, expenses):
    return income - get_total_expenses(expenses)

while True:
    choice = get_choices()
    if choice == '1':
        while True:

            print("Would you like to change your monthly income? (1) or add to it? (2)")
            sub_choice = input()
            if sub_choice == '1':
                print("Enter new monthly income amount: ")
                income = float(input())
            elif sub_choice == '2':
                print("Enter amount to add to monthly income: ")
                add_amount = float(input())
                income += add_amount
            else:
                print("Invalid choice. Please try again.")
                continue
            budget = get_budget(income, expenses)
            clear()

            print(f"Income added. Monthly income: ${income:.2f}")
            break


    elif choice == '2':
            print("What would you like to change? \n1. Rent\n2. Groceries\n3. Utilities\n4. Others\n5. Summary of expenses")

            while True:

                subchoice = input()
                if subchoice not in ['1', '2', '3', '4', '5', '6']:
                    print("Invalid choice. Please try again.")
                    continue

                elif subchoice == '1':
                    print("Enter rent expense: ")
                    expenses["rent"] = float(input())
                    clear()
                    print(f"Your rent expenses are ${expenses['rent']:.2f}\n")
                    show_expenses_menu()

                elif subchoice == '2':
                    print("Enter groceries expense: ")
                    expenses["groceries"] = float(input())
                    clear()
                    print(f"Your groceries expenses are ${expenses['groceries']:.2f}\n")
                    show_expenses_menu()

                elif subchoice == '3':
                    print("Enter Utilities expense:")
                    expenses["utilities"] = float(input())
                    clear()
                    print(f"Your utilities expenses are ${expenses['utilities']:.2f}\n")
                    show_expenses_menu()

                elif subchoice == '4':
                    
                    print("Enter other expenses: ")
                    expenses["others"] = float(input())
                    clear()
                    print(f"Your other expenses are ${expenses['others']:.2f}\n")
                    show_expenses_menu()

                elif subchoice == '5':
                    clear()
                    print(f"Summary of expenses:\nRent: ${expenses['rent']:.2f}\nGroceries: ${expenses['groceries']:.2f}\nUtilities: ${expenses['utilities']:.2f}\nOthers: ${expenses['others']:.2f}\nTotal Expenses: ${get_total_expenses(expenses):.2f}\n")
                    show_expenses_menu()

                elif subchoice == '6':
                    clear()
                    print("Returning to main menu...\n")
                    break

    elif choice == '3':
        totalExpenses = get_total_expenses(expenses)
        budget = get_budget(income, expenses)
        clear()
        print(f"Your current budget is: ${budget:.2f}\n")
        

    elif choice == '4':
    
        totalExpenses = get_total_expenses(expenses)
        budget = get_budget(income, expenses)

        clear()
        print(f"Your income is ${income:.2f}, your expenses are ${totalExpenses:.2f}, and your budget is ${budget:.2f}")
        if budget > 0:
            print("You are within your budget. Great job!")
        elif budget < 0:
            print("You are over your budget. Consider reducing your expenses or increasing your income.")
        else:
            print("Your budget is perfectly balanced. Try to decrease your expenses to save more money.")

    elif choice == '5':
        budget = get_budget(income, expenses)
        clear()
        age = int(input("Enter your age: \n"))
        age_of_retirement = int(input("At what age do you plan to retire? \n"))
        years_until_retirement = age_of_retirement - age
        compound_interest_rate = 1.10
        compounding = compound_interest_rate ** years_until_retirement
        print(compounding)
        if years_until_retirement <= 0:
            clear()
            print("You are already at or past your retirement age. Consider consulting a financial advisor for retirement planning.")
        else:
            investing_amount = budget * 12 * years_until_retirement * compounding
            clear()
            print(f"If you invest your monthly budget of ${budget:.2f} for {years_until_retirement} years, you could potentially have ${investing_amount:.2f} by the time you retire, assuming a 10% return on investment. Consider investing in a diversified portfolio to potentially increase your returns over time.")

    elif choice == '6':
        clear()
        print("Bye!")
        break


    else: 
        print("Invalid choice. Please try again.")
                







