# using if....else
num = int(input("Enter the Number: "))

if num < 0:
    print("Number is Negative")
elif num ==0:
    print("Number is Zero")
else:
    print("Number is Positive")



# Check number using match-case (switch alternative in Python 3.10+)

# num = int(input("Enter the Number: "))

# match num:
#     case n if n < 0:
#         print("Number is Negative")
#     case 0:
#         print("Number is Zero")
#     case _: if n > 0:                        # for default if all cases not matched this will execute
#         print("Number is Positive")


# using dictionary mapping
# num = int(input("Enter the Number: "))

# check = {
#     num < 0: "Number is Negative",
#     num == 0: "Number is Zero",
#     num > 0: "Number is Positive"
# }

# print(check[True])



# using ternary expression
# num = int(input("Enter the Number: "))

# print("Number is Negative" * (num < 0) or
#       "Number is Zero" * (num == 0) or
#       "Number is Positive" * (num > 0))
