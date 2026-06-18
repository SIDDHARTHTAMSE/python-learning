# JSON Files

# JSON means:

# JavaScript Object Notation

# Looks like a Python dictionary.

# Example:

# {
#   "name": "Sid",
#   "age": 25
# }


# Example 1 - Write JSON

import json

student = {
    "name": "Sid",
    "age": 25
}

with open("student.json", "w") as file:
    json.dump(student, file)



# Example 2 - Read JSON

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data)


# Example 3

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(data["name"])


# Example 4

import json

with open("student.json", "r") as file:
    data = json.load(file)

print(type(data))