class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some generic sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # calls Animal.__init__
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()  # calls Animal.speak
        return f"{parent_sound}. But as a dog, I bark!"


dog = Dog("Buddy", "Golden Retriever")
print(dog.name)        # Buddy
print(dog.breed)       # Golden Retriever
print(dog.speak())     # Some generic sound. But as a dog, I bark!




# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         super().show()
#         print("B")
# class C(B):
#     def show(self):
#         super().show()
#         print("C")
# obj = C()
# obj.show()
