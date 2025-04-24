class Car:
    wheels = 4
    def __init__(self, name, year, price):
        self.name = name
        self.year = year
        self.price = price
        self.model = f"{name}, {year}"
    
    # Instance methods : acesses instance attributes
    def start_engine(self):
        return f"{self.name}'s engine started"

    # parameters other than self should be passed when calling the method
    def new_price(self, raise_amount):
        self.price = int(self.price * raise_amount)

car_1 = Car("supra", 2022, 20000)
car_2 = Car("ferrari", 2001, 100000)

## ~~~~~~~~~~~~~~~~~~Call a method:~~~~~~~~~~~~~~~~~~

print(Car.start_engine(car_1)) # call method with class by passing the object
    # when we pass in the object, it is recieved as 'self' 

print(car_1.start_engine()) # call method using object, which passes in object as 'self'

## Method changing attribute values:
print(car_1.price)
car_1.new_price(2)
print(car_1.price)

## ~~~~~~~~~~~~~~~~~~Instance Methods~~~~~~~~~~~~~~~~~~

# made without decorators
# first parameter : self (instance calling)
# extra arguments should be passed when calling

# Purpose: Operates on instance's data. Modify, access or use attributes of the instance. 

## ~~~~~~~~~~~~~~~~~~Class Methods~~~~~~~~~~~~~~~~~~ ??

# made with decorators: @classmethods
# first parameter : cls (class itself)
# extra arguments should be passed when calling

# Purpose: Operates on class level data(same across all instances). Create or modify class-wide state, or act as alternative constructors


## ~~~~~~~~~~~~~~~~~~USE CASE~~~~~~~~~~~~~~~~~~
class Organism:
    def __init__(self, genus, species, relevance):
        self.genus = genus,
        self.species = species,
        self.relevance = relevance
    # Instance methods
    def org_name(self):
        return f"{self.genus} {self.species}"