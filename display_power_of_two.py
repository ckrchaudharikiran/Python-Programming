nterms = int(input("Enter the number of nterms here: "))
result = list(map(lambda x: 2**x, range(nterms+1)))
print(result)
for i in range(nterms+1):
    print("The value of 2 raised to power",i,"is",result[i])