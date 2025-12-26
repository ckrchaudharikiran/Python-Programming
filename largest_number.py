#we are taking float because user can put decimals too

#Correct code    here we will use >= because if two values are same then it will execute else block so we are using >=
# num1 = float(input("Enter 1st number: "))
# num2 = float(input("Enter 2nd number: "))
# num3 = float(input("Enter 3rd number: "))

# if (num1 >= num2) and (num1 >= num3):
#     print(num1, "is the largest")
# elif (num2 >= num1) and (num2 >= num3):
#     print(num2, "is the largest")
# else:
#     print(num3, "is the largest")


#shorter code
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))

print(max(num1, num2, num3), "is the largest")

