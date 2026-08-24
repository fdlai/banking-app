"""
account.py - Abstract base class for all account types.
Pillars: ABSTRACTION (ABC), ENCAPSULATION (private balance)
"""

from abc import ABC, abstractmethod

from transaction import Transaction


class Account(ABC):
    """
    Base class for every account type.
    This class is ABSTRACT - you can never write Account("ACC1001", "Luis", 500).
    It defines WHAT every account must do; subclasses define HOW.
    """

    # ----------------------------------------------------------
    # THE CONSTRUCTOR
    # __init__ runs AUTOMATICALLY when you write
    # SavingsAccount("ACC1001", "Luis", 500).
    # You never call it yourself.
    #   self            -> the new object being built
    #   account_number  -> data injected into it
    #   owner_name      -> data injected into it
    #   initial_balance -> has a DEFAULT, so it is optional
    # Its job: put the object in a VALID state before use.
    # ----------------------------------------------------------
    def __init__(self, account_number: str, owner_name: str,
                 initial_balance: float = 0.0):
        if not account_number or not account_number.strip():
            raise ValueError("An account must have an account number.")
        if not owner_name or not owner_name.strip():
            raise ValueError("An account must have an owner name.")
        if initial_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_number = account_number.strip().upper()
        self.owner_name = owner_name.strip()

        # ENCAPSULATION: double underscore = name mangling.
        # From outside, acct.__balance raises AttributeError.
        self.__balance = float(initial_balance)
        self.__transactions = []

        if initial_balance > 0:
            self.__record("OPEN", initial_balance)

    # ENCAPSULATION: read-only access
    @property
    def balance(self) -> float:
        """Read as acct.balance. No setter, so it cannot be overwritten."""
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        self.__record("DEPOSIT", amount)

    def withdraw(self, amount: float) -> None:
        """
        Default rule: cannot take out more than you have.
        Savings and Checking OVERRIDE this - that is POLYMORPHISM.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.__record("WITHDRAW", amount)

    def get_history(self, n: int = 5) -> list:
        """Return the last n transactions, newest last."""
        return self.__transactions[-n:]

    def _adjust(self, amount: float, kind: str) -> None:
        """
        Protected helper for SUBCLASSES only.
        They cannot touch __balance directly. Pass a negative
        amount to reduce the balance, e.g. an overdraft fee.
        """
        self.__balance += amount
        self.__record(kind, abs(amount))

    def __record(self, kind: str, amount: float) -> None:
        """Private - not even subclasses call this."""
        self.__transactions.append(
            Transaction(self.account_number, kind, amount)
        )

    # ABSTRACTION: the contract every subclass must fulfill
    @abstractmethod
    def account_type(self) -> str:
        """Every subclass MUST identify itself, e.g. 'Savings'."""

    def __str__(self) -> str:
        return (f"[{self.account_number}] {self.owner_name:<12} "
                f"{self.account_type():<10} ${self.balance:>12,.2f}")