num = int(input("Enter the number: "))

if num<=1:
    print(num, " is not a prime number")
if num>1:
    for i in range(2, num):
        if (num%i==0):
            print(num, " is not a prime number")
            break
    else:
        print(num, " is a prime number")


# prime numbers are those which are only divisible by 1 and the number itself
# eg. 5 is divisible by only 1 and 5


#optimized solution

# import math

# num = int(input("Enter the number: "))

# if num <= 1:
#     print(num, "is not a prime number")
# else:
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
