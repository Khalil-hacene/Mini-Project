# Python Banking Program

def show_balance(balance):
    print()
    print(f"Your balance is ${balance: .2f}")
    print()

def deposit(balance):
    try:
        amount = float(input("Enter the amount that you want to deposit in your account: "))
        if amount <= 0:
            print("The amount needs to be above zero!")
        else:
            balance += amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance


def withdraw(balance):
    try:
        amount = float(input("Enter the amount that you want to withdraw from your account: "))
        if amount > balance:
            print('Your withdrawal must be less than or equal to your current balance.')
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero!")
        else:
            balance -= amount
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    return balance



def main():
    balance = 0
    while True:
        print()
        print("********************************")
        print("*       Banking Program        *")
        print("********************************")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("********************************")
        print()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            continue

        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance = deposit(balance)
        elif choice == 3:
            balance = withdraw(balance)
        elif choice == 4:
            break
        
    print("Thank you for using our services")

main()