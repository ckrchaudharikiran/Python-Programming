def convertBinary(n):
    if n >1:
        convertBinary(n//2)
    print(n%2,end="")
n = int(input("Enter the number: "))
print("The Binary of the given number is: ")
convertBinary(n)



# more precise
# def convertBinary(n):
#     if n == 0:
#         return "0"
#     if n == 1:
#         return "1"
#     return convertBinary(n // 2) + str(n % 2)

# n = int(input("Enter the number: "))
# if n < 0:
#     print("Please enter a non-negative number")
# else:
#     print(f"The Binary of the given number is: {convertBinary(n)}")
