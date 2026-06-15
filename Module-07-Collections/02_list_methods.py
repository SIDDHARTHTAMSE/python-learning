# Access List Items

# Example:

fruits = ["Apple", "Mango", "Banana"]

print(fruits[0])

# Negative Indexing
print(fruits[-1])

# Modify List
# Example:

fruits = ["Apple", "Banana", "Mango"]

fruits[2] = "Orange"

print(fruits)


# Add Items
# append()

# Adds item at the end.

fruits = ["Apple", "Banana", "Mango"]

fruits.append("Chikku")
 

print(fruits)



# insert()

fruits = ["Apple", "Banana", "Mango"]
fruits.insert(1, "Dragon fruit")

print(fruits)


# Remove Items
# remove()

fruits = ["Apple", "Banana", "Mango"]
fruits.remove("Mango")
print(fruits)


# pop()
# Removes last item.

fruits = ["Apple", "Banana", "Mango"]
fruits.pop()
print(fruits)


# List Length

fruits = ["Apple", "Banana", "Mango"]
print(len(fruits))


# Loop Through List

fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)