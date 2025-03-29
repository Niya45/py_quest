# RANDOM: Get a random number
import random

# random.randit(start, end) : get a random number between
high = 20
ranum = random.randint(1, high)
print(ranum)

rantwo = random.random()
print(rantwo)

students = ["Rock", "Paper", "Scissors"]
print(random.choice(students))


nums = ["@", "1", "2", "3", "4", "5", "6"]
random.shuffle(nums)
print(nums)
