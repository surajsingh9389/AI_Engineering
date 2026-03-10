# LIST - Ordered, mutable, indexed, allow duplecates

# fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# # Indexing (starts at 0!)
# print(fruits[0])      # First item: "apple"
# print(fruits[2])      # Third item: "orange"
# print(fruits[-1])     # Last item: "kiwi"
# print(fruits[-2])     # Second last: "grape"

# # Slicing [start:end] (end is exclusive)
# print(fruits[1:3])    # Items at index 1 and 2: ["banana", "orange"]
# print(fruits[:3])     # First 3 items: ["apple", "banana", "orange"]
# print(fruits[2:])     # From index 2 to end: ["orange", "grape", "kiwi"]
# print(fruits[::2])    # Every 2nd item: ["apple", "orange", "kiwi"]

# # Modifying items
# fruits[1] = "blueberry"
# print(fruits)         # ["apple", "blueberry", "orange", "grape", "kiwi"]

# games = ["chess", "monopoly"]

# # Adding items
# games.append("checkers")        # Add to end: ["chess", "monopoly", "checkers"]
# games.insert(1, "scrabble")     # Insert at position: ["chess", "scrabble", "monopoly", "checkers"]
# games.extend(["dominoes", "cards"])  # Add multiple: ["chess", "scrabble", "monopoly", "checkers", "dominoes", "cards"]

# # Removing items
# games.remove("monopoly")         # Remove specific item
# popped = games.pop()             # Remove and return last item
# popped = games.pop(1)            # Remove and return item at index 1
# games.clear()                    # Remove everything

# # Finding items
# colors = ["red", "blue", "green", "blue", "yellow"]
# print(colors.index("green"))     # Find position: 2
# print(colors.count("blue"))      # Count occurrences: 2
# print("purple" in colors)        # Check if exists: False

# # Sorting and reversing
# numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers.sort()                   # Sorts in place: [1, 1, 2, 3, 4, 5, 9]
# numbers.reverse()                # Reverses: [9, 5, 4, 3, 2, 1, 1]

# # Copying lists
# original = [1, 2, 3]
# copy1 = original.copy()          # Method 1: copy()
# copy2 = list(original)           # Method 2: list()
# copy3 = original[:]              # Method 3: slicing


# # Method 1: Direct iteration
# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print("I like", fruit)

# # Method 2: Using index
# for i in range(len(fruits)):
#     print(f"Fruit {i+1}: {fruits[i]}")

# # Method 3: Both index and value
# for i, fruit in enumerate(fruits):
#     print(f"Position {i}: {fruit}")

# # List comprehension - advanced but useful!
# squares = [x**2 for x in range(1, 6)]      # [1, 4, 9, 16, 25]
# evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]


# -------------------------------------------------------------------------------------------------------------------

# TUPLE - Imutable, orderd, index, allow duplicates

# # Creating tuples
# coordinates = (10, 20)           # Usually with parentheses
# rgb = 255, 128, 0                 # Parentheses optional
# single_item = (42,)               # Comma needed for single item
# empty_tuple = ()

# # Accessing (same as lists)
# print(coordinates[0])             # 10
# print(coordinates[-1])            # 20

# # Tuples are immutable - this will cause an error!
# # coordinates[0] = 15  # TypeError!

# # Why use tuples?
# # 1. Data that shouldn't change (like coordinates, colors)
# # 2. Dictionary keys (lists can't be keys, tuples can)
# # 3. More efficient (slightly faster than lists)
# # 4. Safer for data integrity

# # Tuple unpacking
# point = (5, 10)
# x, y = point                      # x=5, y=10
# print(f"X: {x}, Y: {y}")

# # Swapping variables (super useful trick!)
# a = 5
# b = 10
# a, b = b, a                       # Now a=10, b=5
# print(f"a: {a}, b: {b}")

# tuple methods

# count(), index(), len(), max(), min(), sum(), sorted(), any(), all()


# lis = [1, 2, 5, 6, 7]
# x, y, *rest = lis

# print(f"x: {x}, y: {y}, rest: {rest}")


# # This creates a generator object, not a tuple
# gen = (x**2 for x in range(5)) 

# # This is the "emulated" tuple comprehension
# my_tuple = tuple(x**2 for x in range(5))
# print(my_tuple)  # Output: (0, 1, 4, 9, 16)



# ----------------------------------------------------------------------------

# SET - unordered, unique, mutable(add, remove), unindexed

# methods - add(), update(), remove(), discard(), pop(), clear()

# mathematical operations - 

# Union() or | , intersection() or & , difference() or - , symmentic_difference() or ^ 

# iteration
# fruits = {"apple", "banana", "cherry"}

# for fruit in fruits:
#     print(fruit)


# {expression for item in iterable if condition}

# raw_names = ["Alice", "BOB" "alice", "Charlie", "BOb", "Ed"]

# clean_names = {name.lower() for name in raw_names if len(name)>3 }


# Comparison:         Set       vs.     Frozenset
# Feature       	  Set               Frozenset
# Mutability	Mutable (can change)	Immutable (cannot change)
# Hashable          	No               	Yes
# Used as Dict Key	    No	                Yes
# Creation	        {} or set()	        frozenset()


# ------------------------------------------------------------------


# Dictionary -  mutable, ordered, keyValue-Pair, unique keys, immutable keys, indexed by keys, dynamic

# Creating dictionaries 
student = {
    "name": "Alice", 
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# # Alternative creation 
# person = dict(name="Bob", age=25, city="New York")
# empty_dict = {}

# # Accessing values 
# print(student["name"])
# print(student.get("age"))
# print(student.get("phone", "not found"))

# Modifying dictionaries

# student["age"] = 21
# student["age"] = 23

# print(student)

# Removing items
# del student["grade"]               # Remove specific key
# email = student.pop("email")       # Remove and return value
# student.clear()                     # Remove everything

# # Dictionary methods
# grades = {"Math": 90, "Physics": 85, "Chemistry": 78}

# print(grades.keys())               # All keys: dict_keys(['Math', 'Physics', 'Chemistry'])
# print(grades.values())             # All values: dict_values([90, 85, 78])
# print(grades.items())              # All pairs: dict_items([('Math', 90), ('Physics', 85), ('Chemistry', 78)])
 

#  # Looping through dictionaries
# for subject in grades:
#     print(f"{subject}: {grades[subject]}")

# for subject, score in grades.items():
#     print(f"{subject}: {score}")

# # Checking if key exists
# if "Math" in grades:
#     print("Math grade:", grades["Math"])


