num1 = float(input("Enter the number1: "))
num2 = float(input("Enter the number2: "))

print("1. for Addition, Press 1 \n2. For Substraction, Press 2 \n3. for Multiplication, Press 3 \n4. for Division, Press 4")
choice = int(input("Enter the choice from 1 to 4: "))

if choice ==1:
    result = num1+num2
    print(f"Addition of {num1} and {num2} is {result}")
elif choice ==2:
    result = num1 - num2
    print(f"Subtraction of {num1} and {num2} is {result}")
elif choice == 3:
    result = num1*num2
    print(f"Multiplication of {num1} and {num2} is {result}")
elif choice == 4:
    result = num1/num2            # we cant divide float by zero, use below code for such situation
    print(f"Division of {num1} and {num2} is {result}")
else:
    print("Please Enter Valid Choice")


# num1 = float(input("Enter the number1: "))
# num2 = float(input("Enter the number2: "))

# print("1. For Addition, Press 1")
# print("2. For Subtraction, Press 2")
# print("3. For Multiplication, Press 3")
# print("4. For Division, Press 4")

# choice = int(input("Enter the choice from 1 to 4: "))

# if choice == 1:
#     result = num1 + num2
#     print(f"Addition of {num1} and {num2} is {result}")
# elif choice == 2:
#     result = num1 - num2
#     print(f"Subtraction of {num1} and {num2} is {result}")
# elif choice == 3:
#     result = num1 * num2
#     print(f"Multiplication of {num1} and {num2} is {result}")
# elif choice == 4:
#     if num2 != 0:
#         result = num1 / num2
#         print(f"Division of {num1} and {num2} is {result}")
#     else:
#         print("Error: Division by zero is not allowed!")
# else:
#     print("Please Enter Valid Choice")
