# 2. Pandas
# What is Pandas?

# Pandas is used for:

# Data Analysis
# Data Cleaning
# Data Processing

# Import:

# import pandas as pd


# Important Functions
# df.head()
# df.tail()
# df.info()
# df.describe()
# df.columns


# Example 1: Create DataFrame
import pandas as pd

data = {
    "Name": ["Sid", "Rahul"],
    "Age": [24, 25]
}

df = pd.DataFrame(data)

print(df)



# Example 2: Read CSV

# Suppose:
# students.csv

import pandas as pd

df = pd.read_csv("students.csv")

print(df)


# Example 3: Show First Rows
print(df.head())


# Example 4: Column Access
import pandas as pd

df = pd.read_csv("students.csv")

print(df.columns)