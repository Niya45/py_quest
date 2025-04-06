# CLASS : (Blueprint) Used to design the structure of an object
# Object : A product with it's own attributes and methods
class Car:
    wheels = 4
    
    def start_car(self):
        return "engine successfully started"
    
supra = Car()

# Get an attribute:
print(supra.wheels)
# Call a method:
print(supra.start_car())


