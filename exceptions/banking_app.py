"""
banking_app.py:     Testing different account classes
"""
from account import *

def account1_test():
    acct = Account1(100.0)
    acct.deposit(25.0)
    success = acct.withdraw(500.0)
    if not success:
        print("Insufficient Funds")
    print("Balance: ",acct.get_balance())

def account2_test():
    acct = Account2(100.0)
    acct.deposit(25.0)
    try:
        acct.withdraw(500.0)
    except AssertionError as ae:
        print(str(ae))
    except Exception:
        print("Something else went wrong")

    print("Balance: ", acct.get_balance())

def account_test():
    acct = Account(100.0)
    acct.deposit(25.0)
    try:
        acct.withdraw(500.0)
    except InsufficientFunds as e:
        print(e)
        print(f"Overdrawn ammount: {e.overage()}")

def main():
    account_test()


main()
