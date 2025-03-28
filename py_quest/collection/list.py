# ____LIST____ : iterable and mutable collection of items that have index.
# elements count from 0 onwards

# dir(var) : list methods of the collection
# help(var) : discribtion of methods and attributes of the collection


ls = ["sero", "one", "two", "three"]
# Add an element to the end of the list
ls.append(4)
print(ls)
# get the element based on index
print(ls[0])
# get the last element in the list
print(ls[-1])
#get the second last:
print(ls[-2])
# get the length of list
print(len(ls))
#change the item based on index:
ls[1] = "ONE" 
print(ls) 
#__SLICING__
    #A way to grab specific items in an iterable by the index{
    # iterable[start:end:step]
        #start: which index to start from
        #end: which index to end on. Grabs only the ones before it
        #step: how may index to skip in each step

list1 = ["a", "e", "i", "o", "u"]
print(list1[1:4])

# ___LIST FUNCTIONS____

    # list.extend(list2)
nouns = ["house", "island", "jacket"]
nouns1 = ["kite", "lamp", "mountain"]
nouns.extend(nouns1)
print(nouns)

    #list.append(newItem)
    #add new item to the end of list
nouns2 = ["jack"]
nouns2.append("leg")
    
    #list.insert(index, newItem)
nouns2.insert(0, "lamp")
print(nouns2)

    #list.remove(ItemValue) : removes item with value
nouns3 = ["paper", "bag", "rum", "lime"]
nouns3.remove("paper")
print(nouns3)

    #list.clear(ItemValue) : get rid of every single element
nouns4 = ["paper", "bag", "rum", "lime"]
nouns4.clear()
print(nouns4)

    #list.pop(index) : remove items with index. REMOVES the LAST item if index is not given
nouns5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nouns5.pop(0)
print(nouns5)

    #list.index(value) : return the index of the element from value. If repeated the index of first value will be returned
list2 = ["jim", "tim", "limb", "rib", "broken"]
print(list2.index("rib"))

    #list.count(value) : count the repeatance of a value
list3 = ["jim", "tim", "limb", "rib", "broken", "rib"]
print(list3.count("rib"))

    #list.sort() : sort the list alphabetical or numerical
list4 = ["jim", "tim", "limb", "rib", "broken", "carlos"]
list4.sort()
print(list4)

    #list.reverse() : return the list with the elements in reverse
list5 = ["jim", "tim", "limb", "rib", "broken", "carlos"]
list5.reverse()
print(list5)

    #list.copy() :make a copy of a list and assign it to another
list6 = list5.copy()
print(list5)
