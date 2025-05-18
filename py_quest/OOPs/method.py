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

# CALL A METHOD:
# -------------------------------------

print(Car.start_engine(car_1)) # call method with class by passing the object
    # when we pass in the object, it is recieved as 'self' 

print(car_1.start_engine()) # call method using object, which passes in object as 'self'

## Method changing attribute values:
print(car_1.price)
car_1.new_price(1.20)
print(car_1.price)

# INSTANCE METHODS
# --------------------------------------------

# made without decorators
# first parameter : self (instance calling)
# extra arguments should be passed when calling

# Purpose: Operates on instance's data. Modify, access or use attributes of the instance. 

# CLASS METHODS 
# --------------------------------------------

# made with decorators: @classmethods
# first parameter : cls (class itself)
# extra arguments should be passed when calling

# Purpose: Operates on class level data(same across all instances). Create or modify class-wide state, or act as alternative constructors

# STATIC METHODS
# --------------------------------------------

# made with decorators: @staticmethods
# no specific parameters
# Don't access instances or class

# USE CASE
# --------------------------------------------

class Organism:
    planet = "earth"
    def __init__(self, name, genus, species, brainpower):
        self.name = name
        self.genus = genus
        self.species = species
        self.brainpower = brainpower
    #~ **Instance methods**
    def org_name(self):
        return f"{self.genus} {self.species}"
    def profile(self):
       return f"# {self.name}: \n|-Genus: {self.genus} \n|-Species: {self.species} \n|-brainpower: {self.brainpower} \n|_Planet: {self.planet}"
    #~ **Class methods**
    @classmethod
    def change_planent(cls, np):
        cls.planet = np
    @classmethod
    def break_down(cls, string):
        name, genus, species, brainpower = string.split("-")
        # create a new object & return. The var calling this will be object
        return cls(name, genus, species, int(brainpower))
    #~ **Static methods**
    @staticmethod
    def brainpower_evaluate(bp):
        if bp <= 30:
            return "Inferior"
        if bp > 30 and bp <= 60:
            return "Stupid"
        if bp > 60 and bp <= 100:
            return "Plain"
        if bp > 100 and bp <= 500:
            return "Smart"
        if bp > 500 and bp <= 1000:
            return "Clever"
        if bp > 1000 and bp <= 1500:
            return "Genius"
        else:
            "GOD"
humans = Organism("Human", "Homo", "sapiens", 2000)
cat = Organism("Cat", "Felis", "catus", 100000)

# Using instance method:
print(humans.profile())
print(cat.profile())
print(Organism.profile(cat))

# Using class_method:
Organism.change_planent("mars") # call using class (attribute changes for every instance)
humans.change_planent("saturn") # call using object (attribute changes for every instance)
print(humans.profile()) # the class attribute's value is different now

# Using class methods as alternative constructors
fox_info = "Fox-Vulpes-vulpes-8000"
fox = Organism.break_down(fox_info)
print(fox.profile())

# Using Static methods:
print(Organism.brainpower_evaluate(1000))  


# PUBLIC METHODS
# --------------------------------------------
# PRIVATE METHODS
# --------------------------------------------
