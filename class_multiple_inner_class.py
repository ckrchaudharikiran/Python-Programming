class Organization:
   def __init__(self):
      self.inner1 = self.Department1()
      self.inner2 = self.Department2()
        
   def showName(self):
      print("Organization Name: Tutorials Point")

   class Department1:
      def displayDepartment1(self):
         print("In Department 1")
            
   class Department2:
      def displayDepartment2(self):
         print("In Department 2")

# instance of OuterClass
outer = Organization() 
# Calling show method
outer.showName()  
# InnerClass instance 1
inner1 = outer.inner1 
# Calling display method
inner1.displayDepartment1() 
# InnerClass instance 2
inner2 = outer.inner2 
# Calling display method
inner2.displayDepartment2() 
