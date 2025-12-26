a = 0
b = 1
num = int(input("Enter the number of terms: "))

if num <= 0:
    print("Please enter a positive number")
elif num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a + b
        a = b
        b = c
        print(c)
