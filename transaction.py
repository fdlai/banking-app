class Transaction:
    def __init__(self, account_number, transaction_type, amount):
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount


class TransactionHistory:
    def __init__(self):
        self.history = []

    def add_transaction(self, account_number, transaction_type, amount):
        transaction = Transaction(account_number, transaction_type, amount)
        self.history.append(transaction)

    def display_history(self, account_number):
        print("\n===== TRANSACTION HISTORY =====")

        found = False

        for transaction in self.history:
            if transaction.account_number == account_number:
                print(
                    f"{transaction.transaction_type}: "
                    f"${transaction.amount:.2f}"
                )
                found = True

        if not found:
            print("No transactions found.")