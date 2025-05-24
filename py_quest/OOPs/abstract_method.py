# ABSTRACT METHODS
# ----------------------------

'''
- A method that's declared in a class but acts like a place holder
- Any non-abstract class that inherits from an abstract class must implement all of its abstract methods
- Helps to define a common interface for all subclasses
'''
# ABSTRACT CLASS : a class that contains one or more abstract methods
'''
- Cannot be instantiated
- Can contain both abstract methods and concrete methods (methods with implementation)
'''

from abc import ABC, abstractmethod
'''
- abc : Abstract Base Class (tells python that this is an abstract class)
- ABC : Base class for defining abstract classes
- abstractmethod : Decorator to declare a method as abstract
'''

class Animal(ABC):
    # Abstract method declaration:
    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):
    def __init__(self, sound):
        self.sound = sound
    # Abstract method implementation with concrete logic:
    def speak(self):
        return f"Cat says {self.sound}"
    
class Horse(Animal):
    def __init__(self, sound):
        self.sound = sound
    # Abstract method implementation with concrete logic:
    def speak(self):
        return f"Horse says {self.sound}"

class RussianBlue(Cat): 
    # Animal -> Cat -> RussianBlue
    def __init__(self, sound):
        super().__init__(sound)
    # Abstract method implementation with concrete logic:  
    def speak(self):
        return f"Russian Blue says {self.sound}"

# Example usage:

def animeal_say(animal: Animal):
    print(animal.speak())
    # Create a function that takes an Animal object and calls its speak method
    # This function takes in any subclass of Animal

# Can't instantiate an abstract class directly:
# animal = Animal()  # This returns an error

cat = Cat("Meow")
horse = Horse("Neigh")
animeal_say(cat)    # Output: Meow
animeal_say(horse)  # Output: Neigh
