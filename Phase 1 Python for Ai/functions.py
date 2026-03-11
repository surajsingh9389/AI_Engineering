# Returning multiple valuse

# def get_min_max(numbers):
#     # Returns the minimum and maximum of a list
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return minimum, maximum

# scores = [85, 92, 78, 90, 88]
# low, high = get_min_max(scores)
# print(f"Lowest: {low}, Highest: {high}")

# --------------------------------------------------------------------------

# Docstrings - Documenting Your Functions

# def calculate_bmi(weight, height):
#     """
#     Calculate BMI (Body Mass Index)

#     Parameters:
#     weight (float): Weight in kilograms
#     height (float): Height in meters

#     return: 
#     float: BMI value rounded to 1 decimal place

#     Example
#     >>> calculate_bmi(70, 1.75)
#     22.9
#     """

#     bmi = weight/(height ** 2)
#     return round(bmi, 1)

# # View the documentation
# help(calculate_bmi)
# print(calculate_bmi.__doc__)

# -----------------------------------------------------------------------------

# def get_positive_number(prompt):
#     """Keep asking until user enters a positive number"""

#     while True:
#         try:
#             num = float(input(prompt))
#             if num > 0:
#                 return num
#             else: 
#                 print("Please enter a positive number")
#         except ValueError:
#             print("Please enter a valid number")        


# # Use the validation function
# age = get_positive_number("Enter your age: ")
# print(f"Age: {age}")


# --------------------------------------------------------------------------------------

# Data processing function
def process_students(students):
    """
    Process student data and return statics

    students: List of dictionaries with name and grade
    Returns: Dictinary with statics

    """

    if not students:
        return {"error": "No students provided"}
    
    grades = [s["grade"] for s in students]

    stats = {
        "total_students": len(students),
        "average_grade": sum(grades) / len(grades),
        "highest_grade": max(grades),
        "lowest_grade": min(grades),
        "passing_students": sum(1 for g in grades if g >= 60)
    }

    return stats

classroom = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 58},
    {"name": "Diana", "grade": 78}
]

results = process_students(classroom)
for key, value in results.items():
    print(f"{key}: {value}")