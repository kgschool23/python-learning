# Python Banking Program

def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")
    print("*****************************")

def deposit():
    deposit = float(input("How much would you like to deposit?"))
    print("*****************************")

    if deposit < 0:
        print("That's not a valid amount.")
        print("*****************************")
        return 0
    else:
        return deposit

def withdraw(balance):
    withdraw_amount = float(input("How much would you like to withdraw?"))
    print("*****************************")

    if withdraw_amount > balance:
        print("Insufficient funds")
        print("*****************************")
        return 0
    elif withdraw_amount < 0:
        print("That's not a valid amount.")
        print("*****************************")
        return 0
    else:
        return withdraw_amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("*****************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*****************************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Invalid choice")
            print("*****************************")

    print("Have a nice day!")

if __name__ == '__main__':
    main()