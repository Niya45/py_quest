# How to take inputs from the user:
    # you insert prompts inside the input() to ask the user something
name = input("Insert your name: \n")
# The input() takes in the user input as a string.
age = int(input("Insert your age in numbers:\n"))

print("Hello", name, "How are you?")

# the input is always string: change it to the required type
age = int(age)
age += 1
print(age)

# OR----------
# var = datatype("what is your age?")
