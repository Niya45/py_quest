# ITERABLES: an object or collection that can return one value at a time, allowing it to be looped through

## basic example with list:
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if not(numbers[-1] == number):
        print(number, end=", ")
    elif numbers[-1] == number:
        print(number)

# reversed order:
for number in reversed(numbers):
    if not(numbers[0] == number):
        print(number, end=", ")
    if numbers[0] == number:
        print(number)
    

## basic example with tuple:
numbers_t = (1,2,3,4,5,6,7,8,9)
for number_t in numbers_t:
    print(number_t, end=" ")
print()

# reversed order:
for number_t in reversed(numbers_t):
    print(number_t, end=" ")
print()

## Sets won't return items in order, as it's unordered: 
# (but if the numbers are in order, python will print them in order)
names = {"niya", "jack", "john", "arthur"}
for name in names:
    print(name, end=" ")
print()
# set objects aren't reversible: print(reversed(numbers_s))

## DITCIONARIES: 
# marks of students out of 100
scores = {
    "light": 100,
    "L" : 100,
    "law" : 98,
    "luffy" : 5,
    "Aizen" : 1000,
    "giorno" : 105
    }

# keys:
for student in scores.keys():
    print(student, end=" ")
print()

# values:
for score in scores.values():
    print(score, end=" ")
print()

# both: (dictionary is unordered)
for student,score in scores.items():
    print(f"{student} : {score}")

