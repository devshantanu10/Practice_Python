def is_palindrome(s):
    return s == s[::-1]

# Get input from user
word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

# Check user input
print(is_palindrome(word1))
print(is_palindrome(word2))

# Example additional check

