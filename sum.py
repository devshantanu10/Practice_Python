def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num 
    return total
    

my_numbers = [8,2,3,0,7]
result = sum_of_list(my_numbers)
print("The sum of the list is:" , result)
    