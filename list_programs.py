new_list = [expression for item in iterable if condition]

# string = "hello world"
# uppercase_letters = [char.upper() for char in string if char.isalpha()]
# print(uppercase_letters)  

# original_list = [1, 2, 3, 4, 5]
# doubled_list = [(lambda x: x * 2)(x) for x in original_list]
# print(doubled_list)  

# list1=[1,2,3]
# list2=[4,5,6]
# CombLst=[(x,y) for x in list1 for y in list2] 
# print (CombLst)

# list1=[x for x in range(1,21) if x%2==0]
# print (list1)

# chars=[]
# for ch in 'TutorialsPoint':
#    if ch not in 'aeiou':
#       chars.append(ch)
# print (chars)

# listObj = [x for x in iterable]

# chars = [ char for char in 'TutorialsPoint' if char not in 'aeiou']
# print (chars)

# squares = [x*x for x in range(1,11)]
# print (squares)


# import random
# L1 = []
# for i in range(5):
#    x = random.randint(0, 100)
#    L1.append(x)
# print (L1)


# L1 = [1, 9, 1, 6, 3, 4]
# ttl = 0
# for x in L1:
#    ttl+=x
# print ("Sum of all numbers Using loop:", ttl)
# ttl = sum(L1)
# print ("Sum of all numbers sum() function:", ttl)


# L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]
# L2 = []
# for x in L1:
#    if x not in L2:
#       L2.append(x)
# print (L2)
