class Student:
    def __init__(self, name, rollno, age):
        self.name=name
        self._rollno=rollno
        self.__age=age
    def __display(self):
        print(f"Hi myself {self.name} {self.__age} years old with rollno {self._rollno} from Student.")
    def displayPrivateData(self):
        self.__display()

    def get_age(self):
        return self.__age
    def set_age(self, age):
        if age > 35:
            print("Invalid age Given, Age should be less than 35.")
        else:
            self.__age=age
class Branch(Student):
    def show(self):
        print(f"My rollno is {self._rollno}")


b1=Branch("Nisha", 45, 23)
b1.show()
s1=Student("Kiran", 23, 20)
print(s1.get_age())
s1.set_age(34)
print(s1.get_age())
