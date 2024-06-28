
class Employee:

    num_of_emp = 0 #class variable
    raise_amt = 1.04 #4%

    def __init__(self,first,last,pay): #initialization for the objects
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower()+"."+last.lower()+'@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self): #regular method taking the instance as the argument i.e. self
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self): #returns the attributes of the instance #priority 2 >> special method 1
        return "Employee({},{},{})".format(self.first, self.last,self.pay)
    
    def __str__(self): #priority 1 >> special method 2
        return "{} - {}".format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
    
emp1 = Employee('Vicky', 'Koushal', 200000)
emp2 = Employee('Ranveer','Seth',60000)

print(emp1) #if printed with just the object name - it shows only the location of the object not the items of the objects #priority 1 __str__ printed
print(repr(emp1)) #prints only the repr method
print(str(emp1)) #prints only the str method
#in order to print the necessary attributes of the object we make use of the special methods
#>>> repr method (inbuilt function)
#>>> str method (inbuilt method)

print(emp1+emp2) #automatically the __add__ method is called '+' by this

#print(len('test')) #length of a string
#print('test'.__len__()) #length of a string using the inbuilt func

print(len(emp1)) #returns the length of the full name of a employee object

#if we want to make this len function to work on our object then we have to create a new len special method (__len__)