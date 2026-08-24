# Banking App

A console-based banking system written in Python. It models customers and
their accounts (checking and savings) and lets you view balances, make
deposits and withdrawals, and review transaction history from a simple
text menu.

This project doubles as a demonstration of core OOP principles:

- **Abstraction** — `Account` is an abstract base class (`ABC`) that
  defines the contract every account type must fulfill.
- **Encapsulation** — account balance and transaction history are
  private attributes, exposed only through a read-only `balance`
  property and controlled methods like `deposit()`/`withdraw()`.
- **Inheritance** — `CheckingAccount` and `SavingsAccount` both extend
  `Account`, reusing its constructor and shared behavior.
- **Polymorphism** — each subclass overrides `withdraw()` with its own
  rule: `SavingsAccount` enforces a minimum balance, while
  `CheckingAccount` allows overdrawing up to a limit for a fee.

## Features

- View all accounts belonging to a customer
- Deposit funds into an account
- Withdraw funds, with account-specific rules:
  - **Savings**: withdrawals are rejected if they would drop the balance
    below a $100 minimum
  - **Checking**: withdrawals beyond the balance are allowed up to a
    $500 overdraft limit, with a $35 overdraft fee applied
- View an account's transaction history

## Project Structure

| File                  | Purpose                                                       |
|-----------------------|----------------------------------------------------------------|
| `main.py`              | Console menu and program entry point                          |
| `account.py`           | Abstract `Account` base class                                 |
| `checking_account.py`  | `CheckingAccount`, extends `Account`, overdraft support        |
| `savings_account.py`   | `SavingsAccount`, extends `Account`, minimum balance rule      |
| `customer.py`          | `Customer` model, holds a list of accounts                    |
| `customerdata.py`      | Hard-coded sample customers linked to accounts                |
| `accountdata.py`       | Hard-coded sample account data                                |
| `transaction.py`       | `Transaction` and `TransactionHistory` models                 |

## Getting Started

### Requirements

- Python 3.9+

### Run

```bash
python main.py
```

You'll be presented with a menu:

```
=====Banking System=====
Please select an option below.

1. View accounts
2. Deposit
3. Withdraw
4. Transaction History
5. Exit
```

### Sample Data

The app comes preloaded with five customers, each linked to one account:

| Customer ID | Name          | Account Number | Type     | Starting Balance |
|-------------|---------------|-----------------|----------|-------------------|
| C001        | Alex Johnson  | 1001            | Checking | $500.00           |
| C002        | Maria Garcia  | 1002            | Savings  | $1,000.00         |
| C003        | Jordan Lee    | 1003            | Checking | $750.00           |
| C004        | Taylor Brown  | 1004            | Savings  | $1,500.00         |
| C005        | Morgan Davis  | 1005            | Checking | $250.00           |

Use a customer ID (e.g. `C001`) to view accounts, or an account number
(e.g. `1001`) to deposit, withdraw, or view transaction history.
