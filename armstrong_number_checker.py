#  armstrong number is where sum of cube of each element of number is equal to that number

num = int(input("Enter the number: "))
order = len(str(num))
sum =0
temp=num
while temp>0:
    digit = temp % 10
    sum += digit ** order
    temp //=10
if sum == num:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number")