

class Employee:

    def __init__(self,Name,age,salary):
    
        self.Name=Name
        self.age=age
        self.salary=salary
    
    def Employee_details(self):
        print("name of the employee",self.Name)
        print("employee age",self.age)
        print("employee salary",self.salary)
        

e=Employee("Ravi",24,1000)
e.Employee_details()
