"""
account.py:     Definition of account classes
"""


class Account1:
    """
    option1: look before you leap - test if the withdrawal
             is valid before we attempt the withdrawal.
    """
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance >= amt:
            self.balance -= amt
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

class Account2:
    """
    option2: Use assertions to throw an AssertionError exception
             if a problem occurs
    """
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        assert(type(amt) == float), "withdraw: Invalid data"
        assert(self.balance >= amt), "withdraw: Insufficient balance"
        self.balance -= amt

    def get_balance(self):
        return self.balance

class InsufficientFunds(Exception):
    """ A user-defined exception for signaling a banking
        application specific issue. """
    def __init__(self, balance, amt):
        super().__init__(f"Insufficient funds: Balance: {balance}, Requested: {amt}")
        self.balance = balance
        self.amt = amt

    def overage(self):
        return self.amt - self.balance


class Account:
    """
    option3: Raise a custom domain-specific exception
    """
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def deposit(self, amt):
        self.balance += amt

    def withdraw(self, amt):
        if self.balance < amt:
            raise InsufficientFunds(self.balance, amt)
        self.balance -= amt

    def get_balance(self):
        return self.balance
