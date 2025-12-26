text = str(input("Enter something here: "))
w = text.split()
for i in range(len(w)):
    w[i]=w[i].lower()
w.sort()
print(w)
for i in w:
    print(i)