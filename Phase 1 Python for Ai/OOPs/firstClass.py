# class Student:
#     """A simple student class"""

#     # Class attribute (shared by all students)
#     school = "Python University"

#     # Constructor - initializes new objects
#     def __init__(self, name, age, grade):
#         # Instance attributes (unique to each student)
#         self.name = name
#         self.age = age
#         self.grade = grade
#         self.courses = [] # Empty list for enrolled courses
    
#     def inroduce(self):
#         return f"Hi, I'm {self.name}, {self.age} years old in grade {self.grade}"
    
#     # Another method
#     def enroll(self, course):
#         self.courses.append(course)
#         print(f"{self.name} enrolled in {course}")

# # Create student objects
# student1 = Student("Alice", 15, 9)
# student2 = Student("Bob", 16, 10)

# # Use the objects
# print(student1.inroduce())
# print(student2.inroduce())


# student1.enroll("Math")
# student2.enroll("Science")
# student2.enroll("History")

# print(f"{student1.name}'s courses: {student1.courses}")
# print(f"{student2.name}'s courses: {student2.courses}")

# print(f"Both attend {Student.school}")  # Access class attribute


# -----------------------------------------------------------------

# Without Constructor

# class Blank:
#     sound = "moooooooo"
#     def print_sound(self):
#         print(self.sound)

# obj = Blank()
# obj.print_sound()


# class Employee:
#     # Class attributes (shared by all instances)
#     company = "Tech ASP"
#     raise_amount = 1.04
#     employee_count = 0 # Track total employees

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.employee_count += 1 # Increment class attribute
    
#     def apply_raise(self):
#         self.salary = int(self.salary*Employee.raise_amount)
    
#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: ${self.salary}")
#         print(f"Company: {Employee.company}")  # Access class attribute


# emp1 = Employee("GT", 5000)
# emp2 = Employee("SS", 6000)

# # Each has own instance attributes
# print(f"{emp1.name}: ${emp1.salary}")
# print(f"{emp2.name}: ${emp2.salary}")

# # But share class attributes
# print(f"Both work at {Employee.company}")
# print(f"Total employees: {Employee.employee_count}")

# # Modify class attribute for all instances
# Employee.raise_amount = 1.05
# print(f"New raise amount: {emp1.raise_amount}")  # Both see the change

# emp1.company = "Honda"

# print(f"Both work at {Employee.company}")
# print(emp1.company)

# print(f"{emp1.name} salary is {emp1.salary}")
# print(f"{emp2.name} salary is {emp2.salary}")
# print(f"comapany: {emp1.company}")
# print(f"comapany: {emp2.company}")

# emp2.company = "Honda"

# print(f"comapany: {emp1.company}")
# print(f"comapany: {emp2.company}")


# Instance Methods, Class Methods, and Static Methods

# class MathOperations:
#     pi = 3.14159 # class attribute 

#     def __init__(self, value):
#         self.value = value # Instance attribute

#     # Instance method (works wiht instancw data )
#     def square(self):
#         return self.value ** 2
    
#     # Class method (works with class data)
#     @classmethod - alternative constructor
#     def circle_area(cls, radius):
#         return cls.pi * radius ** 2
    
#     #Static method (utility - doesn't need class or instance)
#     @staticmethod
#     def add(a, b):
#         return a + b
    

# Using instance method
# m = MathOperations(5)
# print(f"Square of {m.value}: {m.square()}")

# Using class method (doesn't need instance)
# print(f"Circle area: {MathOperations.circle_area(10)}")

# Using static method
# print(f"Add: {MathOperations.add(10, 20)}")


# -------------------------------------------------------------------

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Instance method
    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    # Class method - alternative constuctor
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day) # Creates new instance
    
    # Static method - validation
    @staticmethod
    def is_valid_date(year, month, day):
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        # Simplified - real validation would check months properly
        return True
    
# Regular creation
# d1 = Date(2024, 3, 15)
# print(d1.display())

# Create using class method
# d2 = Date.from_string("2024-12-25")
# print(d2.display())

# Use static method for validation
print(Date.is_valid_date(2024, 2, 30))  # False   