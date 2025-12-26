# using enumerate method
l = [15,50,36,45,96,85,32,52,]
for index, value in enumerate(l, start=1):
    print(index, " - ", value)



# not using enumerate method

# for index in range(len(l)):
#     value = l[index]
#     print(index,value)