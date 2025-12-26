def fact(n):
    if n == 0 or n ==1:
        return 1
    else:
        return (n*fact(n-1))
n = int(input("Enter the number: "))
if n <=0:
    print("Enter a positive number: ")
else:
    print(f"Factorial of {n} is {fact(n)}")



# ⚡ Tip: For very large numbers (say 1000!), recursion may cause a recursion depth error. In that case, an iterative version is safer:
# def fact_iter(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# n = 25
# print(f"Factorial of {n} is {fact_iter(n)}")
