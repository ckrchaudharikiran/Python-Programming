def findHCF(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if (x%i==0) and (y%i==0):
            hcf = i
    return hcf
    
x= int(input("Enter value1: "))
y = int(input("Enter value2: "))
print("The HCF/GCD of given two numbers is", findHCF(x,y))


# def findHCF(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# x = int(input("Enter value1: "))
# y = int(input("Enter value2: "))
# print("The HCF/GCD of given two numbers is", findHCF(x, y))


# import math

# x = int(input("Enter value1: "))
# y = int(input("Enter value2: "))
# print("The HCF/GCD of given two numbers is", math.gcd(x, y))

