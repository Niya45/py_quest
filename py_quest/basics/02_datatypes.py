# A "variable" is a pointer or placeholder that points to a specific data that can change or vary.
# "Data types" are types of data that you can store in variables

name = "diavolo" #String
num = 4 #Number
fl = 4.4 #Float
isSmart = True #Boolean

# you can usually change the value of variables by redefining them like this:
name = "guido"
# to find the data type of a variable, you can use the "type()" function, it returns the data type of the argument
print(type(fl))
# you can print multiple values
print("hello this is ", name)
# you can print multiple values
print("hello this is " + name) 
    #only works for strings and you should convert the values to string.