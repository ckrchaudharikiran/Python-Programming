# method overloading
class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

m = Math()
print(m.add(10))        # 10
print(m.add(10, 20))    # 30
print(m.add(10, 20, 30))  # 60



# method overriding
# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Bark!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"


# both overloading and overriding
# class Calculator:
#     # Overloading-like behavior
#     def multiply(self, a, b=1):
#         return a * b


# class AdvancedCalculator(Calculator):
#     # Overriding: child modifies parent method
#     def multiply(self, a, b=1):
#         print("Using advanced multiplication...")
#         return a * b
