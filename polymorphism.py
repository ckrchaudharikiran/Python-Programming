# Polymorphism with Inheritance (Method Overriding)
class Bird:
    def fly(self):
        return "Bird is flying"

class Ostrich(Bird):
    def fly(self):
        return "Ostrich cannot fly"
b = Bird()
o = Ostrich()

print(b.fly())  # Bird is flying
print(o.fly())  # Ostrich cannot fly


# using spuer
# class Shape:
#     def area(self):
#         return 0

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         parent_value = super().area()  # from Shape
#         return (self.side ** 2) + parent_value
