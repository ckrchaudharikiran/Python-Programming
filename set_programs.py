# Defining a set with multiple elements
my_set = {1, 2, 3, 4, 5}

# Converting the set to an iterator
set_iterator = iter(my_set)

# Looping through each item in the set using a while loop
while True:
   try:
      # Getting the next item from the iterator
      item = next(set_iterator)
      # Performing operations on each element
      print("Item:", item)
   except StopIteration:
      # If StopIteration is raised, break from the loop
      break


# l1=[1,2,3,4,5]
# l2=[4,5,6,7,8]
# s1=set(l1)
# s2=set(l2)
# commons = s1&s2 # or s1.intersection(s2)
# commonlist = list(commons)
# print (commonlist)


# s1={1,2,3,4,5}
# s2={4,5}
# if s2.issubset(s1):
#    print ("s2 is a subset of s1")
# else:
#    print ("s2 is not a subset of s1")


# T1 = (1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2)
# s1 = set(T1)
# print (s1)
