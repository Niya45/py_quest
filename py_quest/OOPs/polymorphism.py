# Polymorphism 
# --------------------

# DUCK TYPING
# --------------------

'''
- Another way to achive polymorphism in Python.
- if it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck
- Objects must have minimum/required methods to be considered as a duck 
'''

class Duck: 
    def quack(self):
        return "Quack!"
    def fly(self):
        return "Flies high!"
class Penguin:              
    def quack(self):
        return "Quack!"
    def fly(self):
        return "Can't fly!"
class Airplane:
    def quack(self):
        return "Quack!"
    def fly(self):
        return "Flies high!"


# Function that uses duck typing
def make_it_quack_and_fly(duck):
    print(duck.quack())
    print(duck.fly())

# Function that accepts any object that has quack and fly methods
duck = [Duck(), Penguin(), Airplane()]

for d in duck:
    if d.fly() == "Flies high!":
        make_it_quack_and_fly(d)

'''
- Eg. of duck typing, the type of the object is determined by its methods and properties rather than its class.
- Allowing for more flexible and dynamic code.
- Powerful feature of Python, enabling developers to write code that can work with any object that meets the required interface.
'''