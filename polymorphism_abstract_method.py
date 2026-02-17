# Real-world single-code example of polymorphism: Payment processing system.
# Different payment types (CreditCard, UPI, NetBanking) expose the same interface: pay()

from abc import ABC, abstractmethod
from dataclasses import dataclass

class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Process a payment and return a confirmation message."""
        pass

@dataclass
class CreditCard(Payment):
    card_number: str
    holder_name: str
    expiry: str  # MM/YY

    def pay(self, amount: float) -> str:
        # In real apps: validate Luhn, check expiry, tokenize, call gateway, etc.
        masked = "**** **** **** " + self.card_number[-4:]
        return f"Paid ₹{amount:.2f} using Credit Card ({masked}) for {self.holder_name}"

@dataclass
class UPI(Payment):
    upi_id: str  # e.g., user@okaxis

    def pay(self, amount: float) -> str:
        # In real apps: create collect request / intent, validate VPA, handle callback.
        return f"Paid ₹{amount:.2f} using UPI ({self.upi_id})"

@dataclass
class NetBanking(Payment):
    bank_name: str
    customer_id: str

    def pay(self, amount: float) -> str:
        # In real apps: redirect to bank, handle success/failure, reconcile.
        return f"Paid ₹{amount:.2f} via NetBanking ({self.bank_name}, CustID: {self.customer_id})"

def checkout(payment_method: Payment, amount: float) -> None:
    # Polymorphism: same call (pay) behaves differently depending on the object
    print(payment_method.pay(amount))

# --- Example usage ---
if __name__ == "__main__":
    methods = [
        CreditCard(card_number="4111111111111111", holder_name="Kiran Chaudhari", expiry="12/28"),
        UPI(upi_id="kiran@okhdfcbank"),
        NetBanking(bank_name="HDFC Bank", customer_id="CUST90210"),
    ]
    amounts = [1200.0, 450.5, 980.0]

    for method, amt in zip(methods, amounts):
        checkout(method, amt)




# # Real-world single-code example of polymorphism: Notification system.
# # Different notification types (Email, SMS, Push) expose the same interface: send()

# from abc import ABC, abstractmethod

# class Notification(ABC):
#     @abstractmethod
#     def send(self, message: str) -> str:
#         pass

# class Email(Notification):
#     def __init__(self, to: str):
#         self.to = to
#     def send(self, message: str) -> str:
#         return f"[Email -> {self.to}] {message}"

# class SMS(Notification):
#     def __init__(self, phone: str):
#         self.phone = phone
#     def send(self, message: str) -> str:
#         return f"[SMS -> {self.phone}] {message}"

# class Push(Notification):
#     def __init__(self, device_id: str):
#         self.device_id = device_id
#     def send(self, message: str) -> str:
#         return f"[Push -> {self.device_id}] {message}"

# def notify(channel: Notification, message: str) -> None:
#     # Polymorphism: the same call (send) behaves differently per concrete class
#     print(channel.send(message))

# # --- Example usage ---
# if __name__ == "__main__":
#     channels = [
#         Email("kiran@example.com"),
#         SMS("+91-9876543210"),
#         Push("device-abc-123"),
#     ]
#     for ch in channels:
#         notify(ch, "Your order #A102 has been shipped!")
