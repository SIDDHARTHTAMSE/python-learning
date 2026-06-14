word = input("Enter word: ")

count = 0

for ch in word.lower():

    if ch in "aeiou":
        count += 1

print(count)