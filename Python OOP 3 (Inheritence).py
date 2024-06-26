#Python class Inheritence
#allows us to inherit attributes and methods from a parent classes
#usefull fro creating subclasses - to get all the functionality of the parent class
#overide and add new func without affecting the parent class

class Employee:

    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower()+"."+last.lower()+"@gmail.com"

        Employee.num_of_emp += 1

    def fullname(self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

#create developers and managers

class Developer(Employee):  #creating a new class Developer inherting the Employee class
                            #access the attributes and methods that were set in the parent class
    raise_amt = 1.10 #the class variable is overriden here 

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #initialize the first, last, apy from the super class itself
        # Employee.__init__(self,first,last,pay) #alternate 
        self.prog_lang = prog_lang #initializing a additional variable for the developer class

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None): #never pass a mutable datatype as a default argument (list, dict)
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees 
        
    def add_emp(self, emp): #method to add the employees into the employees of the manager object
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp): #method to remove the employees from the manager object
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self): #method that prints out the employees under the manager object
        print('List of employees : ')
        for emp in self.employees:
            print('--->', emp.fullname())

#walk up the chain of inheritence - method resolutioner



dev_1 = Developer('Corey','Schafer', 50000,'Python')
dev_2 = Developer('Nicolas','Burrich', 55000,'Java')

# print(help(Developer)) #helper for the flow or walk up the chain

mgr_1 = Manager("Susan","Nana", 10000, [dev_1])
print(f"Name : {mgr_1.fullname()}")
print(f"Email : {mgr_1.email}")

mgr_1.add_emp(dev_2)
mgr_1.rem_emp(dev_1)
mgr_1.print_emp()

#The below in-built functions is used to test the inheritence (experimenting)
print(isinstance(mgr_1,Employee)) #if an object is instance of a class
print(issubclass(Manager,Employee)) #if an class is a subclass of a parent class

# print(dev_1.prog_lang)
# print(dev_1.pay)
# dev_1.apply_raise() #the parent class method will be called
# print(dev_1.pay)