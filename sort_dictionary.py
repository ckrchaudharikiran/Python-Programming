dict = {"Kiran":60,"Akshada":65,"Rohan": 52}
print(dict)
sv = sorted(dict.items(), key = lambda x:x[1])
print(sv)


# for using keys we have used 0
# sv = sorted(dict.items(), key = lambda x:x[0])
# print(sv)

#sort only the values
# v = sorted(dict.values())
# print(v)