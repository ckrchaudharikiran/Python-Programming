def get_area(shape):
    return shape.area()

class Circle:
    def area(self):
        return 3.14 * 5 * 5

class Square:
    def area(self):
        return 4 * 4

print(get_area(Circle()))
print(get_area(Square()))



# class Dog:
#     def speak(self):
#         return "Bark"

# class Cat:
#     def speak(self):
#         return "Meow"

# def make_sound(animal):
#     print(animal.speak())
