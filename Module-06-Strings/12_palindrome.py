# Check Palindrome

word = input("Enter the word: ")

if word == word[::-1]:
    print("Palindrom")
else:
    print("Not Palindrom")