# whole sentence reversed

def reverse_word_order(sentence):
     
     words = sentence.split()

     reversed_words = words[::-1]

     return " " .join(reversed_words)


text = input("Enter a sentence:")
result = reverse_word_order(text)
print(result)


# keeping the words order the same

def reverse_each_word(sentence):
     
     words = sentence.split()

     reversed_words = [word[::-1] for word in words]

     return " ".join(reversed_words)

text = "python is fun"
result = reverse_each_word(text)
print(result)