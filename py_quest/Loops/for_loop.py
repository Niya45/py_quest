# FOR LOOP : a set of code that repeats a fixed number of times
li = [1,2,3,4,5]
for i in range(0, 10):
    print(i+1)
print("next part/")

## range(start, stop, step)
    # start: the starting number of the range
    # stop: the number to stop before
    # step: the increment of the range

# increment backwards: starting from the number x
#   range(x, 0, -1)

for i in reversed(li):
    print(i) 
print("next part/")

## reverse(list)
    # built in function, returns a list of items with reversed index.
    # loop through the output to get each value

# skips over odd numbers
for i in range(0, 11):
    if i%2 == 1:
        continue
    else:
        print(i*2)
print("next part/")

# stops when an odd number occurs
for i in range(0, 11):
    if i%2 == 1:
        break
    else:
        print(i*2)
print("next part/")

## CONTINUE: skip over the current iteration
## BREAK: stop the whole loop

## ----NESTED LOOP------
# a loop inside a loop : for every iteration the parent loop makes, the child compleates a cycle

for i in range(5):
    for j in range(0,10):
        print(j, end='')
    print()

# the blank print() creates a blank line