# List comprehension : creating lists based on conditions and loops (below)

# list = [expression for value in iterable if condition]

double = [y*2 for y in range(1,11)]
squares = [x**2 for x in range(1,11)]
print(squares)

# example, no if:
animals = ["llama", "cat", "elephant", "giraffe"]

upper_animals = [animal.upper() for animal in animals]
print(upper_animals)

# example second, with if:

nums = [2, 3, 1, -1, -3, 4, -6, -8]
positives = [num for num in nums if num > 0]
negatives = [num for num in nums if num < 0]
evens = [num for num in nums if num %2 == 0]

print(positives)
print(negatives)
print(evens)