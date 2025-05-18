# MEMEBERSHIP OPERATORS: used to test if a value is in a sequece
#(string, list, tuple, set, dictionary)

## LIST (same with tuple or set)
students = ["jojo", "linus", "alexa", "Jack sparrow", "Arthur dent", "Freddy Mercury"]

if "giorno" in students:
    print("giorno is a student at llama academy")
else: 
    print("giorno was too dumb to get into llama academy")

if "luffy" not in students:
    print("Luffy was too dumb to get into llama academy")

## STRING
# one exapmle:
name = "lian"
value1 = "b"
value2 = "c"
if value1 in name:
    print( f"{value1} is in the name {name}")
elif value2 in name:
    print( f"{value2} is not the name {name}, but 'c' is !")
else:
    print(f"this is very inefficient. No, the name {name} don't have {value1} or {value2} in it")

# second example:
email = "catfish@yahoocom"
if "@" in email and "." in email:
    print(f"The email {email} is valid")
else:
    print(f"The email {email} is not valid")

## DICTIONARY
students = {
    "light": "A+",
    "L" : "A+",
    "law" : "A",
    "luffy" : "C-",
    "Aizen" : "A+++",
    "giorno" : "A+"
    }
student = input("enter a student name:")

if student in students:
    print(f"{student} is in the list and scored {students[student]}")
else:
    print(f"{student} not(is in) the list")