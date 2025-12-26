num = int(input("Enter the number: "))

if num <=0:
    print("Please enter a positive number")
else:
    sum=0
    while num>0:
        sum+=num
        num-=1
    print(sum)
        


# #  without loop and optimized       we have used floow division // not to get float value, it will round it to int
# num = int(input("Enter the number: "))

# if num <= 0:
#     print("Please enter a positive number")
# else:
#     total = num * (num + 1) // 2
#     print(f"Sum of first {num} natural numbers is {total}")
