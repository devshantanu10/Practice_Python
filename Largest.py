def max_of_three (a,b,c):
    if(a >= b) and (a >= c):
        return a
    elif (b >= a) and (b >= c):
        return b
    else:
        return c
    

num1 = 10
num2 = 20
num3 = 50

result = max_of_three (num1,num2,num3)
print("The largest number is:" , result)
