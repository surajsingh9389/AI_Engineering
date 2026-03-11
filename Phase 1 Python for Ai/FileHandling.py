# the basic way
# file = open("example.txt", "r")
# content = file.read()
# file.close()

# print(content)

# The pythonic way F(ile is automatically closed here)
# with open("example.text", "r") as file:
#     content = file.read()



# Mode	Description
# "r"	Read (default) - file must exist
# "w"	Write - creates new file or overwrites existing
# "a"	Append - adds to end of file
# "r+"	Read and write - file must exist
# "w+"	Write and read - creates new or overwrites
# "a+"	Append and read - creates if doesn't exist
# "x"	Exclusive creation - fails if file exists


# create a sample file first
# with open("sample.txt", "w") as f:
#     f.write("Line 1: Hello World\n")
#     f.write("Line 2: Python is awesome\n")

# +++++++++++++++++++++++

# Read entire file
# with open("sample.text", "r") as file:
#     content = file.read()
#     print("Entire File:")
#     print(content)

# ++++++++++++++++++++++

# Read line by line
# with open("sample.text", "r") as file:
#     print("\n Line by line")
#     for line in file:
#         print(f"-> {line}", end="")
 

# +++++++++++++++++++++++++++++++++

# Read all lines into a list
# with open("sample.text", "r") as file:
#     lines = file.readlines()
#     print("\n\nLines as list:")
#     print(lines)

# ++++++++++++++++++++++++++++++++++++++

# Method 4: Read specific number of characters
# with open("sample.txt", "r") as file:
#     first_10 = file.read(10)
#     print(f"\nFirst 10 characters: '{first_10}'")

# ++++++++++++++++++++++++++++++++++++++++++++

# Method 5: Using seek() and tell()
# with open("sample.txt", "r") as file:
#     print(f"\nCurrent position: {file.tell()}")
#     content = file.read(5)
#     print(f"Read: '{content}', position: {file.tell()}")
#     file.seek(0)  # Go back to beginning
#     print(f"After seek(0), position: {file.tell()}")


# ----------------------------------------------------------------------------------------------

# Writing to Files

# Writing (overwrites existing content)
# with open("output.txt", "w") as file:
#     file.write("This is line 1\n")
#     file.write("This is line 2\n")
#     file.write("This is line 3\n")

# +++++++++++++++++++++++++++++++++++++++++++

# Appending (adds to existing content)
# with open("output.txt", "a") as file:
#     file.write("This line is append\n")


# Writing multiple lines at once
# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("Phase 1 Python for Ai/output2.text", "w") as file:
#     file.writelines(lines)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Working with Different File Formats

import csv

# Writing CSV
# students = [
#     ["Name", "Age", "Grade"],
#     ["Alice", 20, "A"],
#     ["Bob", 21, "B"],
#     ["Charlie", 19, "A"]
# ]

# with open("Phase 1 Python for Ai/student.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(students)

# ----------------------------------------------------

# Reading CSV
# with open("Phase 1 Python for Ai/student.csv", "r") as file:
#     reader = csv.reader(file)
#     print("CSV Contents")
#     for row in reader:
#         print(f" {row}")


# CSV with dictionaries (easier!)
# with open("Phase 1 Python for Ai/student.csv", "r") as file:
#     reader = csv.DictReader(file)
#     print("\nAs dictionaries:")
#     for row in reader:
#         print(f"{row['Name']} is {row['Age']}, and got {row['Grade']}")



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


import json

# Python data to save
# data = {
#     "name": "John Doe",
#     "age": 30,
#     "city": "New York",
#     "hobbies": ["reading", "gaming", "hiking"],
#     "married": False,
#     "pets": None
# }

# Writing JSON 
# with open("Phase 1 Python for Ai/data.json", "w") as file:
#     json.dump(data, file, indent=4) # indent for pretty printing

# ------------------------------------------------------------

# Reading JSON
# with open("data.json", "r") as file:
#     loaded_data = json.load(file)
#     print("Loaded JSON data:")
#     print(loaded_data)
#     print(f"Name: {loaded_data['name']}")
#     print(f"Hobbies: {', '.join(loaded_data['hobbies'])}")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Text Files - Simple Configuration

# Saving configuration
config = {
    "username": "python_user",
    "theme": "dark",
    "font_size": 12,
    "notifications": True
}


# with open("Phase 1 Python for Ai/config.txt", "w") as file:
#     for key, value in config.items():
#         file.write(f"{key}={value}\n")

# ------------------------------------------------------

# Reading configuration
# loaded_config = {}
# with open("Phase 1 Python for Ai/config.txt", "r") as file:
#     for line in file:
#         key, value = line.strip().split("=")
#         # converts values to appropriate types
#         if value == "True":
#             value = True
#         elif value == "False":
#             value = False
#         elif value.isdigit():
#             value = int(value)
#         loaded_config[key] = value

# print("Loaded config:", loaded_config)