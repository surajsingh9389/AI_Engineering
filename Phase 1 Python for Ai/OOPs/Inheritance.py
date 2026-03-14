# Inheritance in Object-Oriented Programming (OOP) is a mechanism where a new class (child/derived class) acquires the properties and methods of an existing class (parent/base class).

# # parent class
# class Animal: 
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def speak(self):
#         return "Some sound"
    
#     def info(self):
#         return f"{self.name} is {self.age} years old"
    
# # child class
# class Dog(Animal):
#     def __init__(self, name, age, breed):
#         # Call parent's __init__
#         super().__init__(name, age)
#         # self.name = name
#         # self.age = age
#         self.breed = breed 

#     # Override parent method
#     def speak(self):
#         return f"{self.name} says Woof!"
    
#     # New method specific to Dog
#     def fetch(self):
#         return f"{self.name} is fetching the ball"
    
#     def info(self):
#         return super().info()
    

# # Another child class
# class Cat(Animal):
#     def __init__(self, name, age, color):
#         super().__init__(name, age)
#         # self.name = name
#         # self.age = age
#         self.color = color
    
#     def speak(self):
#         return f"{self.name} says Meow!"
    
#     def scratch(self):
#         return f"{self.name} is scratching the furniture"


# # Create instances
# dog = Dog("Buddy", 3, "Golden Retriever")
# cat = Cat("Whiskers", 2, "Orange")


# # Use methods
# print(dog.info())  # From parent
# print(dog.speak()) # Overriden
# print(dog.fetch()) # Child-specific

# print(cat.info())          # From parent
# print(cat.speak())         # Overridden
# print(cat.scratch())       # Child-specific


# -----------------------------------------------------------------

# Multiple Inheritance

class Flyer:
    def fly(self):
        return "Flying through the air"
    
    def take_off(self):
        return "Taking off"

class Swimmer:
    def swim(self):
        return "Swimming in water"
    
    def dive(self):
        return "Diving underwater"
    
class Duck(Flyer, Swimmer):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says Quack!"
    

# Duck inherits from both Flyer and Swimmer
donald = Duck("Donald")

print(donald.quack())
print(donald.fly())
print(donald.swim())
print(donald.take_off())
print(donald.dive())

# Method Resolution Order (MRO)
print(Duck.__mro__)  # Shows order Python looks for methods