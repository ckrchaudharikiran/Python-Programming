num = int(input("Enter the number: "))

fact = 1

if  num < 0:
    print("Factorial of negative number doesnt exist")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
    print(f"Factorial of {num} is {fact}")


# using math module         ---math module is c optimized so it is always fastest solution
# import math

# num = int(input("Enter the number: "))

# if num < 0:
#     print("Factorial of negative number doesn't exist")
# else:
#     print(f"Factorial of {num} is {math.factorial(num)}")



# using recurssion
# def fact(a):
#     if a == 0:
#         return 1
#     else:
#         return ((a)*fact(a-1))
# num = int(input("Enter the number here: "))
# result = fact(num)
# print("The factorial of the given number is ", result)



# def fact(a):
#     if a < 0:
#         raise ValueError("Factorial of negative number doesn't exist")
#     if a == 0 or a == 1:
#         return 1
#     else:
#         return a * fact(a - 1)

# try:
#     num = int(input("Enter the number here: "))
#     result = fact(num)
#     print("The factorial of the given number is", result)
# except RecursionError:
#     print("Error: Number too large for recursion. Try using math.factorial instead.")
