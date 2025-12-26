def NNS(n):
    if n<=1:
        return n
    else:
        return (n+NNS(n-1))
    
n =int(input("Enter the number: "))
if n <=0:
    print("Please Enter Positive Value")
else:
    print(f"The sum of natual numbers upto {n} is {NNS(n)}")
