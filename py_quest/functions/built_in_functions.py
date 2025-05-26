# MAP() : apply a function to every item in an interable object
# ------------------------------------------------
nums = [1, 34, 23, 25, 64, 36, 74, 52]

def add_one(num):
    num += 1
    return num

new_nums = map(add_one, nums)

# turn the iterable into a tuple and print it:
print(tuple(new_nums))

# the type of new_nums:
print(type(new_nums))

# MAP WITH LAMBDA:

new_nums1 = map(lambda x: x+5, nums)

print(list(new_nums1))

# FILTER(): remove/keeps items in a list based on a condition
# ------------------------------------------------

def more_than_ten(num):
    return num > 10

nums_more_than_ten = filter(more_than_ten, nums)

# using filter with lambda
lambda_more_than_ten = filter(lambda x: x>10, nums)

print(list(nums_more_than_ten))
print(list(lambda_more_than_ten))


# SUM() : get the sum of all numbers in an interable
# ------------------------------------------------
 
# gets the total of the list 'nums'
total = sum(nums)

# starts adding values from -100
total1 = sum(nums, start=-100)

print(total)
print(total1)

# SORTED() : sort an iterable object
# ------------------------------------------------

sorted_nums = sorted(nums)
reverse_nums = sorted(nums, reverse=True)

people = [
    {"name":"james", "age":23},
    {"name":"john", "age":24},
    {"name":"johnny", "age":83},
    {"name":"ryan", "age":93},
    {"name":"adam", "age":34},
    {"name":"joseph", "age":84},
]

sorted_people = sorted(people, reverse=True, key=lambda person: person["age"])
print(sorted_people)


# ENUMERATE() : get the index of a value in a sorted collection
# ------------------------------------------------

students = ["mathew", "major", "manson", "layman", "lane", "anderson"]

for index,student in enumerate(students):
    print(f"{index+1}. {student}")


# uncomment this to see the format of the return value of 'enumerate'
# print(list(enumerate(students))) 


# ZIP() : takes in many lists, returns a 2D list. Eith each item containing the corresponding items in the inputs's index (better seen than said)
# ------------------------------------------------

names = ["mathew", "major", "manson", "layman", "lane", "anderson"]
ages = [23, 64, 25, 63, 75, 25, 53, 47] 

# longer than names, but zip() doesn't error.
# zip() only combines items as much as the smallest list's index. 

combined = list(zip(names, ages))
    # list structure = [["name", age], ["name", age]]

for name, age in combined:
    print(f"{name} is {age} year old")
