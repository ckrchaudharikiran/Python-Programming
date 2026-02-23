# Polymorphism
# Happens when child class redefines parent method.
class Payment:
    def pay(self, amount):
        print("Processing payment")

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UpiPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

def process_payment(payment_obj):
    payment_obj.pay(1000)

process_payment(CreditCardPayment())
process_payment(UpiPayment())

