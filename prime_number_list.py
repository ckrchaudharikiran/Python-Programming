num1 = int(input("Enter lower limit: "))
num2 = int(input("Enter upper limit: "))

print(f"Prime numbers between {num1} and {num2} are: ")

for num in range(num1, num2+1):
    if num>1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num)



# Optimized code
# import math

# num1 = int(input("Enter number1: "))
# num2 = int(input("Enter number2: "))

# for num in range(num1, num2 + 1):
#     if num > 1:
#         for i in range(2, int(math.sqrt(num)) + 1):
#             if num % i == 0:
#                 break
#         else:
#             print(num)



# for 2 to upper limit
# import math

# n = int(input("Enter the upper limit: "))

# print(f"Prime numbers between 1 and {n} are:")

# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num, end=" ")
