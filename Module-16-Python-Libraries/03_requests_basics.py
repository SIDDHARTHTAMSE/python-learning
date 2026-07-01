# 3. Requests
# What is Requests?

# Used for:

# Calling APIs
# Downloading Data
# Making HTTP Requests

# Install:
# pip install requests

# Import:
# import requests


# Example 1: GET Request
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.status_code)


# Example 2: Get JSON Data
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

print(response.json())


# Example 3: Print First User
import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

users = response.json()

print(users[0]["name"])



# Example 4: POST Request
import requests

data = {
    "name": "Sid"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.status_code)