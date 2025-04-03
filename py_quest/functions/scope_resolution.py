# SCOPE : Where a function is accessible and visible
# Scope resolution : Local - Enclosed - Global - Built_in
    # the order in which variables with same name is considered

## LOCAL Variables : functions

# any variable and function inside a parent function is not accessible outside the parent
# you can call the function inside the parent
def funct1():
	x = 2
	def funct2():
		x = 3
		print(x)
	funct2()
	print(x)
funct1()
#funct2() : can't access due to scope issues
# When printing "x" from parent and the child function, the local one overrides others


## ENCLOSED Variables : inside parent functions
def funct1():
	y = 2
	def funct2():
		print(y)
	funct2()
	print(y)
funct1()
# child function can access an enclosed variable from it's parent, if the variable isn't locally present

## GLOBAL Variables : Outside of any function

z = 6
def funct1():
    print(z)
	
funct1()


## BUILT-IN Variable :  variables that come with the python language

from math import e
def funct1():
	print(e)
	
# e = 5 : is on a closer level than e
funct1()