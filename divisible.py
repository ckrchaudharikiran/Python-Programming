#  using for loop
# for i in range(0,100):
#     if i %13 ==0:
#         print(i)


# using lambda function

# l = [ 15, 13, 26, 52, 75, 62, 21, 0]
# result = list(filter(lambda x: x%13 ==0, l))
# print("The numbers divisible by 13 are: ",result)

# shorter using list comprehension
l = [ 15, 13, 26, 52, 75, 62, 21, 0]
result = [x for x in l if x%13 == 0]
print("The numbers divisible by 13 are: ",result)