# Abstraction is the concept of hiding the complex internal details of how something works and only showing the essential features to the user.


from abc import ABC, abstractmethod

# Create the Abstract Base Class (The Blueprint)
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """This method must be implemented by any subclass"""
        pass

# Implement the actual logic in Subclasses
class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Connecting to Bank... Charging ${amount} to Credit Card.")


class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Redirecting to PayPal... Authorizing ${amount} payment.")


# 3. Using the abstraction
def checkout(processor, amount):
    # We don't care IF it's a card or PayPal, 
    # we just know it HAS a process_payment method.
    processor.process_payment(amount)


card = CreditCard()
wallet = PayPal()

checkout(card, 50)
checkout(wallet, 100)

