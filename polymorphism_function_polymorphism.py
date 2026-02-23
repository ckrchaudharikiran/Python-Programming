# 1️⃣ Built-in Function Polymorphism
# Example: len()
print(len("Hello"))        # 5
print(len([1, 2, 3]))      # 3
print(len((1, 2, 3, 4)))   # 4
print(len({1, 2, 3}))      # 3


# Example: sum()
# print(sum([1, 2, 3]))        # 6
# print(sum((4, 5, 6)))        # 15

# Example: print()
# print(10)
# print("AI")
# print([1,2,3])



# 2️⃣ User-Defined Function Polymorphism (Dynamic Typing)
# You can write a function that works for multiple types.

# Example
# def add(a, b):
#     return a + b

# Usage:
# print(add(5, 3))          # 8
# print(add("Hi ", "AI"))   # Hi AI
# print(add([1,2], [3,4]))  # [1,2,3,4]
