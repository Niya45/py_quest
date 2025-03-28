# __FUNCTION___ : A block of code that performs a specific functions. By taking in arguments
# names should be all lowercase
# a function can only return one value. Once it returns a value, the code will break

def say_hlo():
    return "Hello"
print(say_hlo())

def say_hlo1():
    print("hello world")
say_hlo1()

# ____Parameters___
    #parameter: a piece of info that you pass into a function and the function use it to execute something.
    #if a function has parameters, passing them is absolute 
def greet(name):
    return ("hello " + str(name))

print(greet("niya"))
print(greet("mr. farenheit"))
print(2)

# ___RETURN____

def organism(g, s):
    if True:
        g = g.lower().capitalize()
        s = s.lower()
        print(f"{g} {s}")

organism("HOMO", "SAPIENS")
