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

john = Human("John cena", "Homo", "sapiens", 1500)

print(john.brainpower_evaluate())
print(f"Planet: {john.planet}")


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