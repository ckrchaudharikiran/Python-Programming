# def fib(n):
#     if n <=1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# n=int(input("Enter the number: "))
# if n<=0:
#     print("Enter a positive number")
# else:
#     print("Fibonacci Sequence is: ")
#     for i in range(n):
#         print(fib(i))


#optimized

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)   # print each number on new line
        a, b = b, a + b

n = int(input("Enter the number: "))
if n <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Sequence is:")
    fib(n)

