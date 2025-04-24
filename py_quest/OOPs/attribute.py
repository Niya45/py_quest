
class Employee:
    # Class atritbute : same for every object
    employee_nums = 0
    employer = ""
    def __init__(self, name, salary):
    # Instance attributes : unique for each object
        self.name = name
        self.salary = salary
        # Can't access class attributes by just 'name', so use 'Class.attribute'?? 
        Employee.employee_nums += 1

worker1 = Employee("Niya", 20000)
worker2 = Employee("User", 30000)

# Manually creating : a pain in the ass
Employee.tax = 2

# Call an Attribute
print(Employee.employee_nums) # call a class attribute
print(worker1.employee_nums) # call a class attribute
print(worker1.name) # call a instance attribute

# change attribute: 
Employee.employer = "Disney" # changes for every instance
print(Employee.employer)
worker1.employer = "AWS Japan" # only changes for this instance
print(worker1.employer)
