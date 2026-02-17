class Notification:
    def send(self, message):
        raise NotImplementedError("Subclasses must implement send()")

class Email(Notification):
    def send(self, message):
        return f"Sending Email: {message}"

class SMS(Notification):
    def send(self, message):
        return f"Sending SMS: {message}"

class Push(Notification):
    def send(self, message):
        return f"Sending Push Notification: {message}"
      
def notify(user_notification: Notification, message):
    print(user_notification.send(message))

notify(Email(), "Your order has been shipped!")
notify(SMS(), "Your OTP is 4567")
notify(Push(), "You have a new message")
