# ______SETS______

# Sets don't have order
# Sets values can't change
# iterating through SETS will return random values in it
# You can't use the LEN() frunction with SETS


# dir(var) : list methods of the collection
# help(var) : discribtion of methods and attributes of the collection

# to know if an element is present in set:
fruits = {"apple", "pineapple", "banana", "orange", "lemon"}
print("pineapple" in fruits) # bool

# fruits.add(): adds item to a random index
fruits.add("kiwi") 
# fruits.remove() : removes the item
fruits.remove("kiwi")

# set.pop() : meant to remove last item, now random
fruits.pop()

# set.clear() : clear the set
fruits.clear()
