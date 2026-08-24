class Customer:
    """Represents a bank customer and the account connected to them."""

    def __init__(self, name):
        self.name = name
        self.account = None

    def add_account(self, account):
        """Connect an account to this customer."""
        self.account = account
