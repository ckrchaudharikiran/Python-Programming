# nums= [1,5,6,2,7,8]
# iterate = iter(nums)
# print(iterate.__next__())
# print(iterate.__next__())
# print(iterate.__next__())
# print(next(iterate))
# print(next(iterate))

# for i in nums:
#     print(i)


class Fantastic_Five:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=5:
            value = self.num
            self.num+=1
            return value
        else:
            raise StopIteration
FF = Fantastic_Five()
for i in FF:
    print(i)


