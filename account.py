from abc import ABC, abstractmethod
from transaction import Transaction

class Account(ABC):
    """
    Base class for every account type.
    This class is ABSTRACT - you can never write Account("Luis", 500).
    It defines WHAT every account must do; subclasses define HOW.
    """

# Class-level counter, shared by ALL accounts (not per object).
_last_account_number = 1000
# THE CONSTRUCTOR
    # __init__ runs AUTOMATICALLY when you write
    # SavingsAccount("Luis", 500). You never call it yourself.
    #   self            -> the new object being built
    #   owner_name      -> data injected into it
    #   initial_balance -> has a DEFAULT, so it is optional
    # Its job: put the object in a VALID state before use.

def __init__(self, owner_name: str, initial_balance: float = 0.0):
    if not owner_name or not owner_name.strip():
        raise ValueError("An account must have an owner name.")
    if initial_balance < 0:
        raise ValueError("Opening balance cannot be negative.")
    Account._last_account_number += 1
    self.account_number = f"ACC{Account.last_account_number}"
    self.owner_name = owner_name.strip()

    # ENCAPSULATION: double underscore = name mangling.
    # From outside, acct.__balance raises AttributeError.