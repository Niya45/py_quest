#  2D list: Lists inside lists in 2 dimensions only

Students = [["james", 24], 
            ["joy", 15], 
            ["jane", 23], 
            ["john", 56]
        ]
# print(Students)
# print(Students[0])
# print(Students[0][0])

fruits = ["apple", "banana", "coconut"]
vegetables = ["onion", "carrot", "pepper"]
groceries = [fruits, vegetables]

# print(groceries)
# print(groceries[0])
# print(groceries[0][-1])

# Iterating in 2D list:
# for student in Students:
#     print(student)

#this on prints every element in a 2D list:
# for list in groceries:
#     for food in list:
#         print(food, end=" ")
#     print() #start a new line

# _____2D TUPLE_____ : immutable, ordered

scores = (
    ("niya", "nizar", "abdu", "linu"),
    (20, 10, 43, 100)
    )
# each student and thier mark:
num = 1
for i in range(len(scores[0])):
    print(scores[0][i], scores[1][i])