"""
savings_account.py - Savings account.
Pillars: INHERITANCE (extends Account), POLYMORPHISM (withdraw override)
"""

from account import Account


class SavingsAccount(Account):
    """Savings must keep a minimum balance at all times."""

    MIN_BALANCE = 100.0
    INTEREST_RATE = 0.04

    # CONSTRUCTOR CHAINING
    # super().__init__() runs the PARENT constructor first, which
    # sets account_number, owner_name and the private balance.
    # Then we add what makes this a Savings account.
    def __init__(self, account_number, owner_name, initial_balance=0.0,
                 rate=INTEREST_RATE):
        super().__init__(account_number, owner_name, initial_balance)
        self.rate = rate

    # ABSTRACTION: required by the parent's @abstractmethod
    def account_type(self) -> str:
        return "Savings"

    # POLYMORPHISM: same method name as the parent, different rule.
    # Our rule is STRICTER than the parent's, so we check ours
    # first and then let the parent do the actual work.
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(
                f"Savings must keep a ${self.MIN_BALANCE:,.2f} "
                f"minimum balance."
            )
        super().withdraw(amount)