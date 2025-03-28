## DICTIONARIES: a collectionof {key: "value"} pairs. Ordered, changable. NO duplicates

# arrtibutes and methods:
# print(dir(dictionary_name))
# print(help(dictionary_name))
capitals = {
    "Japan" : "Tokyo",
    "USA" : "Washington D.C",
    "France" : "Paris",
    "Russia" : "Moscow",
    "South Korea" : "Seol"
}
# you can't print pairs with index:
#print(countries[1])

# print all key and value:
# print(countries)

# print values from keys:
print(capitals["Japan"])
print(capitals.get("Russia"))

# print a key that don't exist: none
print(capitals.get("Estonia"))


# ADD or UPDATE VALUES: adds non existing ones, update existing ones
capitals.update({"Estonia": "Tailiin"})
capitals.update({"Japan" : "Edo"})
print(capitals)

# Remove a pair using the KEY:
capitals.pop("USA")
print(capitals)

# Remove the last pair, it don't need any input:
capitals.popitem()

# clear all pairs in the dictionary
# capitals.clear()

# get only the keys in a dictionary: returns a list
keys = capitals.keys()
print(keys)

# get only the value in a dictionary: returns a list
values = capitals.values()
print(values)

# get the 
# print KEY: VALUE pair (in different lines): 
    # .items() : return a key and it's value in each iteration
    # dictionary is unordered

for key,value in capitals.items():
    print(f"{key}:{value}")
