# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     # String representation for users
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
    
#     # # String representation for developers
#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.pages})"
    
#     # Length
#     def __len__(self):
#         return self.pages
    
#     # Delete The Destructor This is called when an object is about to be destroyed
#     def __del__(self):
#         print(f"Book '{self.title}' is being deleted")
    
#     # Equality
#     def __eq__(self, other):
#         if isinstance(other, Book):
#             return self.title == other.title and self.author == other.author
#         return False

#     # Less than (for sorting)
#     def __lt__(self, other):
#         return self.pages < other.pages
    

# # Create books
# book1 = Book("1984", "George Orwell", 328)
# book2 = Book("Animal Farm", "George Orwell", 112)
# book3 = Book("1984", "George Orwell", 328)

# # Using magic methods 
# print(book1)  # or print(str(book1))
# print(repr(book1))
# print(len(book1))
# print(book1 == book3)
# print(book2 < book1)   

# # List of books - sorting uses __lt__
# books = [book1, book2]

# books.sort()
# for book in books:
#     print(f"{book.title}: {book.pages} pages")

# ----------------------------------------------------------------------


class Vector: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Add two vectors: v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __sub__(self, other):
        """Subtract two vectors: v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Multiply by scalar: v * scalar"""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __abs__(self):
        """Magnitude of vector"""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    
# Test the Vector class
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"|v1|: {abs(v1)}")
    
