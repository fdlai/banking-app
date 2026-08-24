from transaction import TransactionHistory

transaction_history = TransactionHistory()


def main():
    while True:
        print("=====Banking System=====")
        print("Please select an option below.")
        print("\n1. View accounts")
        print("\n2. Deposit")
        print("\n3. Withdraw")
        print("\n4. Transaction History")
        print("\n5. Exit")

        choice = input("\n Enter your choice: ")

        if choice == "1":
            view_accounts()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            view_transaction_history()
        elif choice == "5":
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")


def deposit():
    account_number = input("Enter account number: ")
    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    amount = get_amount("Enter deposit amount: $")

    try:
        account.deposit(amount)

        transaction_history.add_transaction(account_number, "Deposit", amount)

        print("Deposit successful.")
        print(f"New balance: ${account.balance:.2f}")

    except ValueError as error:
        print(error)


def withdraw():
    account_number = input("Enter account number: ")
    account = find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    amount = get_amount("Enter withdrawal amount: $")

    try:
        account.withdraw(amount)

        transaction_history.add_transaction(account_number, "Withdrawal", amount)

        print("Withdrawal successful.")
        print(f"New balance: ${account.balance:.2f}")

    except ValueError as error:
        print(error)


def make_transfer():
    print("Transfer")


def view_transaction_history():
    account_number = input("Enter account number: ")
    transaction_history.display_history(account_number)


def get_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def find_customer(customer_id):
    pass


def find_account(account_number):
    pass


def view_accounts():
    customer_id = input("Enter customer ID: ")
    customer = find_customer(customer_id)

    if customer is None:
        print("Customer not found.")
        return

    print(f"\nAccounts for {customer.name}:")

    for account in customer.accounts:
        print(
            f"{account.account_number} - "
            f"{account.__class__.__name__} - "
            f"${account.get_balance():.2f}"
        )


if __name__ == "__main__":
    main()
