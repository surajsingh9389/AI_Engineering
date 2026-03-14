import json

# Python to JSON (serialization)
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "gaming"],
    "married": False,
    "salary": None
}

# Convert to JSON string
# json_string = json.dumps(data, indent=4)
# print(json_string)


# # Write JSON to file
# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)


# JSON to Python (deserialization)
# From string
# parsed_data = json.loads(json_string) # convert json string to dictonary
# print(parsed_data['name'])
# print(parsed_data['hobbies'])


# From file
# with open("data.json", "r") as f:
#     file_data = json.load(f)
# print(f"\nFrom file - city: {file_data['city']}")

# Pretty printing
# print(json.dumps(data, indent=2, sort_keys=True))
