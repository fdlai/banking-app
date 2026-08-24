"""checking_account.py - Checking acocunt."""

from account import Account

class CheckingAccount(Account):
    """Checking allows going negative , up to a limit, for a fee"""

    OVERDRAFT_LIMIT = 500.0
    OVERDRAFT_FEE = 35.0

    def __init__(self,owner_name,initial_balance=0.0, overdraft_limit=OVERDRAFT_LIMIT,):
        super().__init__(owner_name,initial_balance)
        self.overdraft_limit = overdraft_limit

    def account_type(self) -> str:
        return "Checking"

    def withdraw(self,amount: float)-> None:
        if amount <= 0:
            raise ValueError("withdrawal amount must be greater than zero.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Withdrawal amount exceeds overdraft limit. ")

        if amount > self.balance:
            self._adjust(-amount, "WITHDRAW")
            self._adjust(-self.OVERDRAFT_LIMIT, "OD_FEE")
            print(f"   ! Overdraft fee of ${self.OVERDRAFT_FEE:.2f} applied. ")
        else:
            super().withdraw(amount)
