class Payment:
    def pay(self, amount):
        raise NotImplementedError("Payment method must implement pay()")
      
class CreditCard(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Credit Card"

class UPI(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using UPI (Google Pay / PhonePe)"

class NetBanking(Payment):
    def pay(self, amount):
        return f"Paid ₹{amount} using Net Banking"
def checkout(payment_method: Payment, amount):
    print(payment_method.pay(amount))
  
checkout(CreditCard(), 1200)
checkout(UPI(), 450)
checkout(NetBanking(), 980)
