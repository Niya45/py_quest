# accessing elements in a sequence using [x:y:z]
    # starts with the index x
    # ends right before the index y
    # jumps z indexes each time, 0 if you add nothing

# list[0] : the first index
# list[-1] : the last index. -2 : the secong last and so on.
name = "joseph joestar"

print(name[7:14])
print(name[:-1]) # start at beginning
print(name[2:]) # ends at the end
print(name[::2]) # jumps from one to next+1