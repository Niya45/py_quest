#  INHERITANCE: 
# --------------------------------------------------------------------------

# Definition: Mechanism where a child class (subclass) inherits attributes and methods from a parent class (superclass)
# Merits: Promotes reusablity by creating connection between classes

class Animal:
    planet = "Earth"
    def __init__ (self, name, genus, species, bp):
        self.name = name, 
        self.genus = genus,
        self.species = species,
        self.bp = int(bp)

    def brainpower_evaluate(self):
        if self.bp <= 30:
            return "Inferior"
        if self.bp > 30 and self.bp <= 60:
            return "Stupid"
        if self.bp > 60 and self.bp <= 100:
            return "Plain"
        if self.bp > 100 and self.bp <= 500:
            return "Smart"
        if self.bp > 500 and self.bp <= 1000:
            return "Clever"
        if self.bp > 1000 and self.bp <= 1500:
            return "Genius"
        else:
            "GOD"

# instance of superclass:
tiger = Animal("tiger", "Panthera", "tigris", 130)
print(tiger.brainpower_evaluate())
print(f"Planet: {tiger.planet}")

# SUBCLASS:
# --------------------------------------------------------------------------

# Instance of subclass: have the attributes of parent + it's own

# Method Resolution Order: the order in which python searches for methods:
    # class-parentclass-grandparentclass-greadgrandparentclass---


class Human(Animal):
    planet = "Mars"
    # INITIALIZING in inherited methods:
    def __init__(self, name, genus, species, bp, job, friends=None):
        super().__init__(name, genus, species, bp) # calls the parent's __init__ methods and passes in the required arguments.
        self.job = job
        if friends == None:
            self.friends = []
        else:
            self.friends = friends

    def add_friend(self, new_f):
        if new_f not in self.friends:
            self.friends.append(new_f)
    
    def remove_friend(self, old_f):
        if old_f not in self.friends:
            self.friends.remove(old_f)
    
    def print_frnd(self):
        for friend in self.friends:
            print(f"Friend {self.friends.index(friend)+1} is {friend}")


john = Human("John", "Homo", "sapiens", 1500, "doctor", ["james", "anne", "clair", "layman"])

print(john.brainpower_evaluate())
print(f"Humans Planet: {john.planet}")
print(f"{john.name}'s job : {john.job}")
john.remove_friend("clair")
john.print_frnd()


# TYPES OF INHERITANCE:
# --------------------------------------------------------------------------

## Single inheritance: inherit one parent
# class Child(parent):
#     pass

## Multiple inheritance: inerit multiple parent
# class Child(parent1, parent2):
#     pass

## Multilevel Inheritance: multiple subclasses inherit from one parent
# class Child1(parent):
#     pass
# class Child2(parent):
#     pass
# class Child3(parent):
#     pass

## Hierarchical inheritance: inherit a parent inheriting a grandparent
# class Grandchild(Child):
#     pass

## Hybrid Inheritance: mix of inheritance (multiple + hierarchical)
# class Grandchild(Child, Parent)
#   pass

