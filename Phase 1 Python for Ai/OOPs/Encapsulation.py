# In Object-Oriented Programming (OOP), encapsulation is the practice of bundling an object's data (attributes) and the methods (functions) that operate on that data into a single unit, known as a class
# The primary purpose of encapsulation is to restrict direct access to the internal state of an object, a concept often referred to as data hiding.


class BankAccount: 
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance  # Protected (convention)
        self.__pin = "1234"  # Private (name mangling)
        self.__transaction_history = []  # Private


    # Feature	               get_balance()	@property balance
    # Calling syntax	account.get_balance()	account.balance

    # Getter method
    def get_balance(self):
        return self._balance        
    
    # Property decorator (Pythonic way)
    @property
    def balance(self):
        """Get current balance"""
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance canaot be negative")
        
        self._balance = amount

    # Setter and Getter both work as pair
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__add_transaction(f"Deposit: +${amount}")
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid amount"
    
    def withdraw(self, amount, pin):
        if pin != self.__pin:
            return "Invalid PIN"
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self.__add_transaction(f"Withdrawal: -${amount}")
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"
    
    # Private method (name mangling)
    def __add_transaction(self, transaction):
        self.__transaction_history.append(transaction)

    # Getter for private data
    def get_history(self, pin):
        if pin == self.__pin:
            return self.__transaction_history
        return "Invalid PIN"
    
account = BankAccount("Alice", 1000)

account.balance = 1500
print(account.deposit(500))
print(account.withdraw(100, "1234"))
print(account.withdraw(300, "1234"))

print(account.get_history("1234"))


    
# # Using the class
# account = BankAccount("Alice", 1000)

# # Using getter
# print(f"Balance: ${account.get_balance()}")

# # Using property
# print(f"Balance via property: ${account.balance}")

# # Using property setter
# account.balance = 1500
# print(f"New balance: ${account.balance}")

# # Protected methods - accessible but should be treated as internal
# print(f"Protected balance: {account._balance}")  # Works but not recommended

# # Private methods/attributes - name mangled
# # print(account.__pin)  # ERROR!
# print(f"Private pin: {account._BankAccount__pin}")  # Can still access (but don't!)

# # Using controlled methods
# print(account.deposit(500))
# print(account.withdraw(200, "1234"))
# print(account.withdraw(2000, "1234"))

# # Can't access private directly
# # print(account.__transaction_history)  # ERROR!
# print(f"History: {account.get_history('1234')}")