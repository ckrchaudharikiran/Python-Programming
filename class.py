class Employee:
   "Common base class for all employees"
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

# This would create first object of Employee class
emp1 = Employee("Zara", 2000)
# This would create second object of Employee class
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


# # defining class
# class Smartphone:
#    # constructor    
#    def __init__(self, device, brand):
#       self.device = device
#       self.brand = brand
#    # method of the class
#    def description(self):
#       return f"{self.device} of {self.brand} supports Android 14"
# # creating object of the class
# phoneObj = Smartphone("Smartphone", "Samsung")
# print(phoneObj.description()) 


# class Employee:
#    'Common base class for all employees'
#    empCount = 0
#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
#    def displayCount(self):
#      print ("Total Employee %d" % Employee.empCount)
#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary)
# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__)


# class Point:
#    def __init__( self, x=0, y=0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print (class_name, "destroyed")
# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# # prints the ids of the obejcts
# print (id(pt1), id(pt2), id(pt3))
# del pt1
# del pt2
# del pt3


# class JustCounter:
#    __secretCount = 0  
#    def count(self):
#       self.__secretCount += 1
#       print self.__secretCount
# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.__secretCount


# class Employee:
#    # class attribute    
#    empCount = 0
#    def __init__(self, name, age):
#       self.__name = name
#       self.__age = age
#       # modifying class attribute
#       Employee.empCount += 1
#       print ("Name:", self.__name, ", Age: ", self.__age)
#       # accessing class attribute
#       print ("Employee Count:", Employee.empCount)
# e1 = Employee("Bhavana", 24)
# print()
# e2 = Employee("Rajesh", 26)



# Access Built-In Class Attributes
# To access built-in class attributes in Python, we use the class name followed by a dot (.) and then attribute name
# class Employee:
#    def __init__(self, name="Bhavana", age=24):
#       self.name = name
#       self.age = age
#    def displayEmployee(self):
#       print ("Name : ", self.name, ", age: ", self.age)
# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__ )


# class Student:
#    def __init__(self, name, grade):
#       self.__name = name
#       self.__grade = grade
#       print ("Name:", self.__name, ", Grade:", self.__grade)
# # Creating instances 
# student1 = Student("Ram", "B")
# student2 = Student("Shyam", "C")


