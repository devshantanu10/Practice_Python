def is_palindrome(s):
    return s == s[::-1]

# Get input from user
word1 = input("Enter a word: ")
word2 = input("Enter a word: ")

# Check user input
print(is_palindrome(word1))
print(is_palindrome(word2))

# Example additional check


def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric and lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    # Check if cleaned string equals its reverse
    return cleaned == cleaned[::-1]

# Ask user for input
user_input = input("Enter a string: ")

# Check and print result
if is_palindrome(user_input):
    print(f"\"{user_input}\" is a palindrome!")
else:
    print(f"\"{user_input}\" is not a palindrome.")

