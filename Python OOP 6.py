#decorators

class Employee:

    num_of_emp = 0 #class variable
    raise_amt = 1.04 #4%

    def __init__(self,first,last,pay): #initialization for the objects
        self.first = first
        self.last = last
        self.pay = pay
        

        Employee.num_of_emp += 1
    @property
    def fullname(self): #regular method taking the instance as the argument i.e. self
        return "{}.{}@gmail.com".format(self.first, self.last)

    def fullname(self): #regular method taking the instance as the argument i.e. self
        return "{} {}".format(self.first, self.last)
    

emp1 = Employee('Jim','Smith')
emp1.first='John'

print(emp1.first)
print(emp1.email)
print(emp1.fullname())