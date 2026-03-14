# Module = A single Python file (like one chapter)

# Package = A folder containing multiple modules (like a book section)

# Library = Collection of packages (like a whole bookshelf)

# --------------------------------------------------------------------------------

# Module = single file
# my_module.py
# my_tools.py

# Package = folder with modules
# my_package/
#   ├── __init__.py
#   ├── module1.py
#   └── module2.py

# Library = collection of packages
# pip install requests
# pip install pandas


# ------------------------------------------------------------------------------

# Importing Modules - The Basics

# # Method 1: Import entire module
# import math 
# print(math.pi)
# print(math.sqrt(25))
# print(math.floor(3.7))

# # Method 2: Import specific functions
# from math import pi, sqrt, floor
# print(pi)
# print(sqrt(25))
# print(floor(3.7))


# # Method 4: Import everything (use carefully!)
# from math import* # Not recommended - namespace pollution!
# print(pi)
# print(sin(0))


# -----------------------------------------------------------------------------

# Python's Standard Library - Built-in Modules

import math

# Constants
# print(f"Pi: {math.pi}")
# print(f"e: {math.e}")
# print(f"Infinity: {math.inf}")
# print(f"NaN: {math.nan}")

# Basic math
# print(f"Square root of 16: {math.sqrt(16)}")
# print(f"2 to the 8th power: {math.pow(2, 8)}")
# print(f"Absolute value of -5: {math.fabs(-5)}")


# Trigonometry
# print(f"Sin(90°): {math.sin(math.pi/2)}")
# print(f"Cos(0°): {math.cos(0)}")


# Logarithms
# print(f"Log base 10 of 100: {math.log10(100)}")
# print(f"Natural log of e: {math.log(math.e)}")

# Rounding
# print(f"Ceil of 4.2: {math.ceil(4.2)}")
# print(f"Floor of 4.8: {math.floor(4.8)}")
# print(f"Factorial of 5: {math.factorial(5)}")

# number = 1234.5678

# print(round(number, -1))  # 1230.0 (Nearest 10)
# print(round(number, -2))  # 1200.0 (Nearest 100)
# print(round(number, -3))  # 1000.0 (Nearest 1000)

# Bankers Rounding
# round(15, -1) → 20 (2 is even)
# round(25, -1) → 20 (2 is even)

# round(1234, -1) → 1230 (int)
# round(1234.0, -1) → 1230.0 (float)


# GCD and more
# print(f"GCD of 48 and 18: {math.gcd(48, 18)}")



# -----------------------------------------------------------------------

# Random Module


import random

# Basic random numbers
# print(f"Random float (0-1): {random.random()}")
# print(f"Random integer (1-10): {random.randint(1, 10)}")
# print(f"Random choice from range: {random.randrange(0, 100, 5)}")


# Choosing from sequences
# fruits = ["apple", "banana", "orange", "grape", "kiwi"]
# print(f"Random fruit: {random.choice(fruits)}")
# print(random.sample(fruits, 3))


# Shuffling
# deck = list(range(1, 53))
# print(deck[:5])
# random.shuffle(deck)
# print(deck[:5])


# Random with weights
# colors = ["red", "green", "blue"]
# weights = [10, 30, 60]  # 10% red, 30% green, 60% blue
# print(random.choices(colors, weights=weights)[0])


# Seeding for reproducibility
# random.seed(42)
# print(f"First random with seed 42: {random.random()}")
# random.seed(42)  # Reset seed
# print(f"Second random with seed 42: {random.random()}")  # Same as first!



# -------------------------------------------------------------------

# Datetime Module

from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
# print(now)
# print(date.today())
# print(datetime.now().time())

# Creating specific dates
# specific_date = datetime(2024, 3, 15, 14, 30, 0)
# print(f"Specific date: {specific_date}")

# Date components
# print(f"Year: {now.year}")
# print(f"Month: {now.month}")
# print(f"Day: {now.day}")
# print(f"Hour: {now.hour}")
# print(f"Minute: {now.minute}")
# print(f"Second: {now.second}")


# Formatting dates
# print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
# print(f"Day of week: {now.strftime('%A')}")
# print(f"Month name: {now.strftime('%B')}")

# Parsing dates
# date_string = "2024-03-15 14:30:00"
# parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(f"Parsed: {parsed_date}")


# Difference between dates
# date1 = datetime(2024, 1, 1)
# date2 = datetime(2024, 12, 31)
# diff = date2 - date1
# print(f"Days between: {diff.days}")
# print(f"Seconds between: {diff.total_seconds()}")

# -------------------------------------------------------------------


# Collections - advanced data structures
from collections import Counter, defaultdict, deque

# # Counter - count occurrences
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# counter = Counter(words)
# print(counter)
# print(counter.most_common(1))


# deque - double-ended queue
# dq = deque([1, 2, 3])
# dq.appendleft(0)
# dq.append(4)
# print(dq)
# dq.rotate(1)
# print(dq)


# import re

# text = "My email is alice@email.com and phone is 555-123-4567"
# emails = re.findall(r'\b[\w.]+@[\w.]+\.\w+\b', text)
# phones = re.findall(r'\b\d{3}-\d{3}-\d{4}\b', text)

# print(f"Emails found: {emails}")
# print(f"Phones found: {phones}")


# Hashlib - cryptographic hashes
# import hashlib

# password = "mysecretpassword"
# hashed = hashlib.sha256(password.encode()).hexdigest()
# print(hashed)


# Statistics
import statistics

data = [2, 5, 3, 8, 9, 5, 2, 7, 5]
print(f"Mean: {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Mode: {statistics.mode(data)}")
print(f"Stdev: {statistics.stdev(data)}")


