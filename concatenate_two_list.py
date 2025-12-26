l1 = [2,6,5,8,6,]
l2= [5,"f","e"]

l3 = l1+l2
print(l3)

l4= list(set(l1+l2))       #   -----set remove duplicate value
print(l4)

# l1.extend(l2)       --- extend does not return new variable, it will add l2 into l1
# print(l1)