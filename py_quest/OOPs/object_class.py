# CLASS : (Blueprint) Used to design the structure of an object
# Object : An instance with it's own attributes and methods made with a class

    
class Car:
    wheels = 4
    # Initializer : runs automatically when an object is created 
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.model = f"{name}, {year}"


## ~~~~~~~~~~~~~~~~~~Creating Instances:~~~~~~~~~~~~~~~~~~
car_1 = Car("supra", 2022, 20000)
car_2 = Car("ferrari", 2001, 100000)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## SELF : refers to the object that is calling the method or attribute

# self.attribute = attribute
    # attribute : the attribute passed to __init__
    # self.attribute : object.attribute
    # EG: car_1.attribute = 'supra'
    # initializing, assigning the values to object


## INITIALIZER : __init__(self, attibute1, attribute2)

# __init__ gets called when an instance is created
# inside init method, instance attributes are initialized