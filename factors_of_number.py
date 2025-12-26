num = int(input("Enter the number: "))
for i in range(1, num+1):
    if num%i==0:
        print(i)




#using math module but hard

# import math

# num = int(input("Enter the number: "))

# for i in range(1, int(math.sqrt(num)) + 1):
#     if num % i == 0:
#         print(i)          # first factor
#         if i != num // i: # avoid duplicate when num is a perfect square
#             print(num // i)
