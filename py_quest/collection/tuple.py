# __TUPLES___ : Immutable, iterable collection of items

# you can't use tuple.apped()
# you can't change the value
# have an order and index

# dir(var) : methods of the tuple
# help(var) : discribtion of methods and attributes of tuple


coordinates = (1, 4, 2, 5, 66)
print(coordinates)

# index starts from 0
print(coordinates[0])

#list of tuples
list7 = [("this", "is"), ("tuple", "inside", "list")]

# len(tuple): you can find the length of tuple

# to know if an element is present in set:
fruits = ("apple", "pineapple", "banana", "orange", "lemon")
print("pineapple" in fruits) # bool

# tuple.index("item") : find the index
print(fruits.index("banana"))

# tuple.count("item") : count the repetance of item
print(fruits.count("banana"))