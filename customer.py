"""Customer model for the banking application."""


class Customer:
    """Represents a bank customer and the account connected to them."""

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.accounts = []

    def add_account(self, account):
        """Connect an account to this customer."""
        self.accounts.append(account)
