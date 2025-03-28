#               _____INTEGERS_____

# we can work with natural numbers, decimals and real numbers etc. in python
print(1)
print(3.14159265)
print(-1.4239)
print(2/3)

#           ________OPERATIONS_________

# it's possible to use arithametic in python:
print(3+4) #addition
print(4-3) #subraction
print(4/2) #division float
print(4//2) #division int
print(4*2) #multiplication
print(4%3) #modulate
print(4**2) #exponentiation

## Operating : var x= 3  : x= operation

# python uses PEMDAS to do operations.
print(3+4*5)
# But using paranthesis, I can manipulate the order.
print((3+4)*5)

# We can store operations in variables:
oper_1 = 4+3
oper_2 = 10*3
#and we can print them:
print(oper_1)
print(oper_2)
#or do operations with the value of those variables:
print(oper_2 - oper_1)

#                   ______OTHER OPERATIONS_______

# To find the ABSOLUTE VALUE of a number
var_2 = -4.5
print(abs(var_2))

# To find any power of a number
var_3 = 3
print(pow(var_3, 3)) #3^3

# to find the max and min of two numbers
print(max(2,8)) #returns the largest of the two
print(min(2,8)) #returns the smallest of the two

# To ROUND UP or DOWN a number
print(round(4.3))
