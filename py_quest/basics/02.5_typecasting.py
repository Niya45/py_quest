# TYPECASTING : the process of converting a variable of one datatype to another
#     str(), int(), float(), bool()
name = "stranger"
age = -15
pi = 3.14159265
smart = True

# returns the datatype of a variable
print(type(name))

# __STRING__

# But if i wanna convert a variable to string i can do this:
var_1 = 34
var_1 = str(var_1)
print(type(var_1))

# converting integer to string
print(str(age))
print(type(str(age)))

# converting float to string
print(str(pi))
print(type(str(pi)))

# converting bool to string
print(str(smart))
print(type(str(smart)))

# __INTEGER__

# you can't convert string to an integer:
    # print(int(name))

# converting float to int: (it rounds down to the closest whole number)
print(int(pi))
print(type(int(pi)))

# converting bool to int: (1 = True , 0 = False)
print(int(smart))
print(type(int(smart)))

# __FLOAT__

# you can't convert string to a float
    # print(float(name))

# converting integer to float
print(float(age))
print(type(float(age)))

# converting bool float (1.0 = True , 0.0 = False)
print(float(smart))


# __BOOLEAN__

# convert string to a bool: (False if empty, True if contains a value)
print(bool(name))
print(type(bool(name)))

# convert int to a bool : (False if 0, True if contains a value)
print(bool(age))
print(type(bool(age)))


# convert float to a bool : (False if 0.0, True if any other value)
print(bool(pi))
print(type(bool(pi)))
