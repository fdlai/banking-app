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
            transaction_history()
        elif choice == "5":
            print("Thank you for using our banking system.")
            break
        else:
            print("Invalid choice. Please try again.")


def deposit():
    print("Deposit")


def withdraw():
    print("Withdraw")


def make_transfer():
    print("Transfer")


def transaction_history():
    print("Transaction history")


def find_customer(customer_id):
    pass


def find_account(account_number):
    pass


def get_amount(prompt):
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
