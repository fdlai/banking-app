def main(): 
    while True:
        print("=====Banking System=====")
        print("Please select an option below.")
        print ("\n1. View accounts")
        print ("\n2. Deposit")
        print ("\n3. Withdraw")
        print ("\n4. Transaction History")
        print ("\n5. Exit")

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

if __name__ == "__main__":
    main()
