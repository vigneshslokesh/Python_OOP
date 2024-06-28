#decorators

class Employee:

    num_of_emp = 0 #class variable
    raise_amt = 1.04 #4%

    def __init__(self,first,last): #initialization for the objects
        self.first = first
        self.last = last
        
    
        Employee.num_of_emp += 1

    @property #defining as a method and accessing as a attribute
    def email(self): #regular method taking the instance as the argument i.e. self
        return "{}.{}@gmail.com".format(self.first.lower(), self.last.lower())
   
    @property #defining as a method and accessing as a attribute
    def fullname(self): #regular method taking the instance as the argument i.e. self
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter #setter
    def fullname(self, name):
        first , last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter #deleter
    def fullname(self):
       print('Delete Name!')
       self.first = None
       self.last = None

emp1 = Employee('Jim','Smith')

emp1.fullname='Corey Shiner'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname