# Basic try-except
# try:
#     number = int(input("Enter a number: "))
#     result = 10/number
#     print(f"10 divided by {number} is {result}")

# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except Exception as e: # Catch any other error
#     print(f"An error occured: {e}")


# --------------------------------------------------------------
# Multiple exceptions in one line
# try:
#     number = int(input("Enter a number: "))
#     result = 10/number
#     print(f"10 divided by {number} is {result}")
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error: {e}")
# else:
#     print(f"Success! Result: {result}")

# ---------------------------------------------------------------------------

# Using else and finally

# try: 
#     file = open("Phase 1 Python for Ai/test.txt", "r")
#     content = file.read()
# except FileNotFoundError:
#     print("File not found")
# else: 
#     print("File read successfully")
#     print(content)
# finally: 
#     print("This always runs!")
#     try:
#         file.close()
#     except:
#         pass

# -------------------------------------------------------------------------

# Raising Exceptions


# def withdraw_money(balance, amount):
#     """Withdraw money from account"""
#     if amount<0 :
#         raise ValueError("Amount cannot be negative")
#     if amount > balance:
#         raise ValueError("Insufficient funds")
#     balance -=amount
#     return balance

# # Using the function with error handling
# balance = 1000

# try:
#     amount = float(input("Enter amout to withdraw: $"))
#     new_balance = withdraw_money(balance, amount)
#     print(f"Withdrawal successful! New balance: ${new_balance}")
# except ValueError as e:
#     print(f"Error: {e}")
# except Exception as e:
#     print(f"Unxepected error: {e}")


# ---------------------------------------------------------------

# Creating Custom Exceptions

# class InsufficentFundsError(Exception):
#     """Raised when account balance is insufficient"""
#     pass
# class NegativeAmountError(Exception):
#     """Raised when amount is negative"""
#     pass

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def withdraw_money(self, amount):
#         """Withdraw money from account"""
#         if amount<0 :
#             raise NegativeAmountError("Cannot withdraw negative amount")
#         if amount > self.balance:
#             raise InsufficentFundsError(f"Insufficinet funds. Balance: ${self.balance}")
#         self.balance -=amount
#         return  f"Withdrew ${amount}. New balance: ${self.balance}"
    
#     def deposit(self, amount):
#         if amount < 0:
#             raise NegativeAmountError("Cannot deposit negative amount")
#         self.balance += amount
#         return f"Deposited ${amount}. New balance: ${self.balance}"


# # Test the custom execptions
# account = BankAccount("Alice", 500)

# try:
#     print(account.withdraw_money(600))
# except InsufficentFundsError as e:
#     print(f"Transaction failed: {e}")
# except NegativeAmountError as e:
#     print(f"Invalid amount: {e}")

# try:
#     print(account.deposit(-50))
# except NegativeAmountError as e:
#     print(f"Invalid amount: {e}")


# ---------------------------------------------------------------------------

# Practical File Operations

import os 
import shutil

# Check if file exists

# try:
#     if os.path.exists("Phase 1 Python for Ai/student.csv"):
#         print("File exists!")

#     else:
#         # print("File doesn't exist")
#         raise FileNotFoundError("File dosen't exist")

# except Exception as e:
#     print(e)


# ----------------------------------------------------------------------

# Get file information

# file_path = "Phase 1 Python for Ai/student.csv"

# if(os.path.exists(file_path)):
#     print(f"File size: {os.path.getsize(file_path)} bytes")
#     print(f"Last modified: {os.path.getmtime(file_path)}")
#     print(f"Absolute path: {os.path.abspath(file_path)}")

# -----------------------------------------------------------------------------

# Directory operations
# os.mkdir("Phase 1 Python for Ai/test_folder") # Create directory
# print(f"Current directory: {os.getcwd()}")
# print(f"Files is current dir: {os.listdir('.')}")


# Copy, move, rename files
# shutil.copy("source.txt", "destination.txt")
# os.rename("oldname.txt", "newname.txt")
# os.remove("file_to_delete.txt")


# ----------------------------------------------------------------

# Walk through directories
for root, dirs, files in os.walk("."):
    print(f"Root: {root}")
    print(f"Dirs: {dirs}")
    print(f"Files: {files}")
    print("-"*30)