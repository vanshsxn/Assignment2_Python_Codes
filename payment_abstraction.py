from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):
    def __init__(self, vpa):
        self.vpa = vpa

    def pay(self, amount):
        return f"UPI payment of {amount} from {self.vpa} processed"

class CreditCard(PaymentMethod):
    def __init__(self, card_no):
        self.card_no = card_no

    def pay(self, amount):
        return f"Credit card {self.card_no[-4:]} charged {amount}"

class Wallet(PaymentMethod):
    def __init__(self, wallet_id):
        self.wallet_id = wallet_id

    def pay(self, amount):
        return f"Wallet {self.wallet_id} debited {amount}"

def process_payment(method: PaymentMethod, amount):
    return method.pay(amount)

print(process_payment(UPI("alice@upi"), 250))
print(process_payment(CreditCard("1234567812345678"), 1200))
print(process_payment(Wallet("WALLET42"), 75))
