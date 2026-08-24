"""Hard-coded customers, each linked to a checking or savings account."""

from customer import Customer
from checking_account import CheckingAccount
from savings_account import SavingsAccount


alex = Customer("C001", "Alex Johnson", "1990-01-15")
alex.add_account(CheckingAccount("1001", "Alex Johnson", 500.00))

maria = Customer("C002", "Maria Garcia", "1985-06-22")
maria.add_account(SavingsAccount("1002", "Maria Garcia", 1000.00))

jordan = Customer("C003", "Jordan Lee", "1992-11-03")
jordan.add_account(CheckingAccount("1003", "Jordan Lee", 750.00))

taylor = Customer("C004", "Taylor Brown", "1978-09-14")
taylor.add_account(SavingsAccount("1004", "Taylor Brown", 1500.00))

morgan = Customer("C005", "Morgan Davis", "2000-02-29")
morgan.add_account(CheckingAccount("1005", "Morgan Davis", 250.00))

customers = [alex, maria, jordan, taylor, morgan]
