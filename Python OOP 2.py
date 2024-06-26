# Similar to the Python OOP1(Employee details) we have made changes by adding and knowing the difference between the
# class variables and instance variables

class Employee:
    raise_amount = 1.04
    num_of_emp = 0

    def __init__(self, first, last, pay): 
        self.first = first #setting the instance variables
        self.last = last #similar to emp1.last = last
        self.email = first.lower()+'.'+last.lower()+'@company.com'
        self.pay = pay

        Employee.num_of_emp+=1
    
    def fullname(self): #self - each method takes the instance as the first argument
        return '{} {}'.format(self.first, self.last) #self - instance as the argument
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('John','Wick',45000) #arguments are the attributes of the object
emp2 = Employee('Corey','Linn',50000)

print(emp1.__dict__)

# emp1.raise_amount=1.05

#print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
# print(emp2.raise_amount)

# print(emp1.__dict__)
# print(Employee.num_of_emp)