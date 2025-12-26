num = int(input("Enter a number: "))

sqrt = num ** (1/2)
cube_root = num ** (1/3)

# sqrt = int(sqrt)   # if want for integer
# cube_root = int(cube_root)   # if want for integer

print(f"Square root of {num} is {sqrt}")
print(f"Cube Root of {num} is {cube_root}")


# using math     - cube root doesnt exist in math but we can use pow

# import math
# sqrt = math.sqrt(num)
# if num > 0:
#     cube_root = math.pow(num, 1/3)
# else:
#     cube_root = -math.pow(num, 1/3)
# print(f"Square root of {num} is {sqrt}")
# print(f"Cube Root of {num} is {cube_root}")

