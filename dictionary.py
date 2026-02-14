d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
keys = ['two', 'five']
d2={}
for k in keys:
   d2[k]=d1[k]
print (d2)


# d1 = {"one":11, "two":22, "three":33, "four":44, "five":55}
# L1 = list(d1.items())
# print (L1)

# d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}
# vals = list(d1.values())#all values
# uvals = [v for v in vals if vals.count(v)==1]#unique values
# d2 = {}
# for k,v in d1.items():
#    if v in uvals:
#       d = {k:v}
#       d2.update(d)
# print ("dict with unique value:",d2)
