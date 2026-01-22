def multiply_num(numbers):
    total = 1
    for num in numbers:
       total = total * num
    return total


my_numbers = (10,2,3,4,5)
result = multiply_num(my_numbers)
print("The multiplication is:" , result)