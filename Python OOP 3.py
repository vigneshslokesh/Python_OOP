#diff between methods, class methods and static methods

#regular methods - takes instance as the first arg
#class methods - takes class as the first arg
class Employee:

    num_of_emp = 0
    raise_amt = 1.04 #4%

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+'@gmail.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return "{}{}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod #alternating the func of a method
    def set_raise_amt(cls, amount):
        cls.raise_amt= amount

    @classmethod #class method as alternative constructor
    def from_string(cls, emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod #static methods when no arg needed of class or instance
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True

emp1 = Employee('Vicky', 'Koushal', 200000)
#we use class methods as alternative constructors 
#provides multiple ways of creating a object

# emp_str1 = Employee.from_string("john-ebaon-70000")
# print(emp_str1.email)

#static methods = do nt pass anyrhing
import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
print(Employee.num_of_emp) #print the number of employees


#(The below lines can be reduced using the class methods)
# first,last,pay = emp_str1.split("-")
# new_emp1 = Employee(first,last,pay)
# print(new_emp1.email)








#emp1.set_raise_amt(1.05)
# print(Employee.raise_amt)
# print(emp1.raise_amt)
# emp1.raise_amt=1.05
# emp1.apply_raise()
# print(emp1.pay)