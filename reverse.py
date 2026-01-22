def reverse_string(s):
    return s[::-1]


text = " Hello"
print(reverse_string(text))


# from loop

def reverse_string(s):
    result = "" 
    for ch in s:
        result = ch + result
    return result

print(reverse_string("hello"))



# from built in methods

def reverse_string(s):
    return ''.join(reversed(s))

print(reverse_string("shantanu"))