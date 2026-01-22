def swap_numbers(a , b):
    return b , a

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

num1 , num2 = swap_numbers(num1, num2)

print("After swapping:")
print("first number:" , num1)
print("second number:" , num2)



# num1 , num2 = swap_numbers(num1 , num2)

# tuple unpacking method 

x = int(input("Enter x: "))
y = int(input("Enter y: "))

x , y = y, x 

print("x =" , x)
print("y = " , y)


