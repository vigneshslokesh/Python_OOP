
class Employee:

    num_of_emp = 0 #class variable
    raise_amt = 1.04 #4%

    def __init__(self,first,last,pay): #initialization for the objects
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+'@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self): #regular method taking the instance as the argument i.e. self
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee({},{},{})".format(self.first, self.last,self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
    
emp1 = Employee('Vicky', 'Koushal', 200000)

print(emp1)