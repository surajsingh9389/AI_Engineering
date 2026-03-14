# Polymorphism in OOP means "many forms," allowing one entity (method, object, or operator) to behave differently depending on its context or the data it receives. It enables a single interface to represent general actions, such as a draw() method behaving differently for a Circle vs. a Square.



# class Shape:
#     def area(self):
#         pass

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#     def area(self):
#         return self.side ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * (self.radius ** 2)

# shapes = [Square(4), Circle(3)]

# for s in shapes:
#     print(f"Area: {s.area()}")

# ---------------------------------------------------------------------

class Human:
    def speak(self):
        print("Hello!")

class Robot:
    def speak(self):
        print("Beep Boop!")

# This function doesn't care what 'obj' is, as long as it has .speak()
def make_it_talk(obj):
    obj.speak()

make_it_talk(Human())
make_it_talk(Robot())

