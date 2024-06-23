#Python Object-Oriented Programming
#classes - group our data & functions to reuse
#attributes - data
#method - function associated with a class

#class - blueprint
#objects - instance of the class    

class Employee:
    def __init__(self, first, last, pay): 
        self.first = first #setting the instance variables
        self.last = last #similar to emp1.last = last
        self.email = first.lower()+'.'+last.lower()+'@company.com'
        self.pay = pay
    
    def fullname(self): #self - each method takes the instance as the first argument
        return '{} {}'.format(self.first, self.last) #self - instance as the argument




emp1 = Employee('John','Wick',45000) #arguments are the attributes of the object
emp2 = Employee('Corey','Linn',50000)

print(emp2.fullname())
print(Employee.fullname(emp1)) #from class pass instance as the argument usually done for background flow check

# print(emp1.fullname())
# print(emp2.fullname())
print(emp1.email)
print(emp2.email)

