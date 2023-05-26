def show_balance(balance):
    print(f"Account Balance :${balance}")


def deposit(balance):
    amount = eval(input("Enter the amount to deposit:"))
    return balance + amount


def withdraw(balance):
    amount = eval(input(f"Enter the amount to withdraw:"))
    return balance - amount


def logout(name):
    print(f"GoodBye {name}!")
