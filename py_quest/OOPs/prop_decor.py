# PROPERTY DECORATORS--------

# GETTERS: @property
# ------------------------

"""
Access instance data and operate on them
Dispite being a method, can also be called as if it's an attribute.
"""
# EG: obj.getter_name

# SETTERS: @x.setter
# ------------------------

"""Methods allowing to validate and modify instance data"""
"""Dispite being a method, can also be called as if it's an attribute."""
#  EG: obj.getter_name = 'new value' 

# DELETER: @x.deleter
# ------------------------

"""Methods that delete an instances data"""
# EG: del obj.getter_name
class Person: 
    def __init__(self, firstname, lastname, age, job):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.job = job
        
    @property
    def fullname(self):
        print("getting fullname... ")
        return "{} {}".format(self.firstname, self.lastname)
    
    @fullname.setter
    def fullname(self, newname):
        print("setting new fullname...")
        first, last = newname.split(" ")
        self.firstname = first
        self.lastname = last
    
    @fullname.deleter
    def fullname(self):
        print("Deleted Name.")
        self.firstname = None
        self.lastname = None

person_1 = Person("John", "Cena", 46, "Body builder")

print(person_1.fullname) # calling getter
person_1.fullname = "Kevin Hart"# calling setter
print(person_1.fullname) # calling after
del person_1.fullname