"""
checking_account.py - Checking account.
Pillars: INHERITANCE (extends Account), POLYMORPHISM (withdraw override)
"""

from account import Account


class CheckingAccount(Account):
    """Checking allows going negative, up to a limit, for a fee."""

    OVERDRAFT_LIMIT = 500.0
    OVERDRAFT_FEE = 35.0

    def __init__(self, account_number, owner_name, initial_balance=0.0,
                 overdraft_limit=OVERDRAFT_LIMIT):
        super().__init__(account_number, owner_name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self) -> str:
        return "Checking"

    # POLYMORPHISM: this rule is the OPPOSITE of Savings.
    # Ours is LOOSER than the parent's, so on the overdraft path
    # we cannot call super().withdraw() - the parent would reject
    # it. We use the protected _adjust() helper instead.
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Amount exceeds your overdraft limit.")

        if amount > self.balance:
            self._adjust(-amount, "WITHDRAW")
            self._adjust(-self.OVERDRAFT_FEE, "OD_FEE")
            print(f"  ! Overdraft fee of ${self.OVERDRAFT_FEE:.2f} applied.")
        else:
            super().withdraw(amount)