#finance tracker
#user name
transaction = []
user_name = input("enter your name: ")
if user_name == "":
    print(input("please enter your name"))
starting_balance = int(input("enter your starting balance: "))

balance_expense = int(input("enter your expense: "))
print("your expense is: ", balance_expense)

transaction.append(user_name)
transaction.append(starting_balance)
transaction.append(balance_expense)
set(transaction)


print("========= PERSONAL FINANCE TRACKER =========")
print("Welcome " + user_name)

#Welcome, Azada!

#1. Add Income
#2. Add Expense
#3. View Transactions
#4. View Financial Summary
#5. Manage Savings Goal
#6. Exit

for i in range(6):
    add =int(input("Choose from 1-6"))
    if add == 1:
        print("your balance is: ", starting_balance)
    elif add == 2:
        print("your expense is: ", balance_expense)



#Choose an option: