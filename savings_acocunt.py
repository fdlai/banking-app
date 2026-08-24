"""savings_account.py -- Savings account.
Pillars: INHERITANCE (extends Account)"""

from account import Account


class SavingsAccount(Account):
    """Savings account. must keep a minimum balance at all times."""
    MIN_BALANCE = 100
    INTEREST_RATE = 0.04

    # CONSTRUCTOR CHAINING
    # super().__init__() runs the PARENT constructor first, which
    # sets account_number, owner_name and the private balance.
    # Then we add what makes this a Savings account.
    def __init__(self, owner_name, initial_balance=0.0,
                 rate=INTEREST_RATE):
        super().__init__(owner_name, initial_balance)
        self.rate = rate

    def account_type(self) -> str:
        return "Savings"

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater that zero. ")
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(
                f"Savings must keep a ${self.MIN_BALANCE:..2f}. "
                f"minimum balance."
            )
        super().withdraw(amount)