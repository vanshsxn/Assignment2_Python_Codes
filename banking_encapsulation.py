class BankAccount:
    def __init__(self, owner, balance, pin, card_limit):
        self.owner = owner
        self._balance = balance
        self.__pin = pin
        self.__card_limit = card_limit

    def check_balance(self, pin):
        if pin != self.__pin:
            raise PermissionError("Invalid PIN")
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self._balance += amount
        return self._balance

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            raise PermissionError("Invalid PIN")
        if amount > self._balance or amount > self.__card_limit:
            raise ValueError("Insufficient funds or over limit")
        self._balance -= amount
        return self._balance

acct = BankAccount("Maya", 50000, "4321", 20000)
print(acct.deposit(5000))
try:
    print(acct.check_balance("0000"))
except Exception as e:
    print(e)
print(acct.check_balance("4321"))
print(acct.withdraw(10000, "4321"))
