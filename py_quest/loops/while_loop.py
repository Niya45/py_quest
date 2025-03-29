## WHILE LOOP : execute a set of code WHIlE a condition stays true

name = input("enter your name: ")
age = int(input("enter your age: "))


#if not name:
#    print("the name is invalid")
#else:
#    print(f"welcome to our service provider, {name}!")

## ANOTHER WAY USING WHILE LOOP:
while not name:
    print("Your name is invalid")
    name = input("enter your name: ")
print(f"welcome to our service provider, {name}!")

# if not given a statement or action that could stop the loop, it might be infinite.

while age < 0:
    print("your age is invalid")
    age = int(input("enter your age:"))
print(f"your age is {age}")


