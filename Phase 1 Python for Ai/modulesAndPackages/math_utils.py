"""
Math Utilities Module
A collection of useful math functions
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b with error handling"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

def power(base, exponent):
    """Raise base to exponent"""
    return base ** exponent

def factorial(n):
    """Calculate factorial recursively"""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Generate fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib


# Module-level variables
VERSION = "1.0.0"
Author = "Suraj"

# Only run if executed directly (not imported)
if __name__ == "__main__":
    # Test code
    print("Testing math_utils module...")
    print(f"add(5, 3): {add(5, 3)}")
    print(f"factorial(5): {factorial(5)}")
    print(f"is_prime(17): {is_prime(17)}")
    print(f"fibonacci(10): {fibonacci(10)}")
    print(f"Module version: {VERSION}")
