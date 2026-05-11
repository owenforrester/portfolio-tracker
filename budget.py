




print()
print("Personal Budget Tracker (Hit enter to continue): ")
print((input("\n-----------------------")))
print("1. Add income")
print("2. Add expense")
print("3. View budget")
print("4. Analytics")

income = 0
expenses = 0
budget = income - expenses

print("Enter your choice (1-4): ")
choice = input()
while choice != '4': 
    if choice == '1':
        print("Would you like to change your weekly income? (1) or add to it? (2)")
        sub_choice = input()
        if sub_choice == '1':
            print("Enter new weekly income amount: ")
            income = float(input())
        elif sub_choice == '2':
            print("Enter amount to add to weekly income: ")
            add_amount = float(input())
            income += add_amount
        budget = income - expenses
        print(f"Income added. Weekly income: ${income:.2f}")
        choice = input("Enter your choice (1-4): ")
    elif choice == '2':
        print("Would you like to change your weekly expenses? (1) or add to them? (2)")
        sub_choice = input()
        if sub_choice == '1':
            print("Enter new weekly expenses amount: ")
            expenses = float(input())
            budget = income - expenses
            print(f"Expense added. Weekly expenses: ${expenses:.2f}")
        elif sub_choice == '2':
            print("Enter amount to add to weekly expenses: ")
            add_amount = float(input())
            expenses += add_amount
            budget = income - expenses
            print(f"Expense added. Weekly expenses: ${expenses:.2f}")
        choice = input("Enter your choice (1-4): ")

    elif choice == '3':
        print(f"Weekly budget: ${budget:.2f}")
        choice = input("Enter your choice (1-4): ")



if choice == '4':
    print("\nAnalytics:")
    print(f"Yearly Income: ${52 * income:.2f}")
    print(f"Yearly Expenses: ${52 * expenses:.2f}")
    print(f"Yearly Budget: ${52 * budget:.2f}")


    choice = input()














print()