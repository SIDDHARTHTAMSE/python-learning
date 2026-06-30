# What is Regex?

# Regex is used to search patterns in text.

# Import:
# import re



# Example 1

# Check word exists.

import re

text = "Hello Python"

result = re.search("Python", text)

print(result)



# Example 2
# Find digits.

import re

text = "Age is 25"

result = re.findall(r"\d", text)

print(result)



# Example 3
# Find all words.

import re

text = "Python FastAPI Docker"

print(re.findall(r"\w+", text))



# Example 4
# Email validation pattern.

import re

email = "test@gmail.com"

pattern = r".+@.+\.com"

print(bool(re.match(pattern, email)))