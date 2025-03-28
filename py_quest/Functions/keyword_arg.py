# KEYWORD ARGUMENT: an argument preceeded by an identifier. Helps with readability


def greeting(occation, name, last):
    return f"Congratulations on your {occation}, {name} {last} !"


# Arguments should be in order: greeting("brithday", "Spongebob", "Squarepants")
# keywords make it possible to mix it up:
print(greeting(name="Giorno", last="Giovanna", occation="promotion"))

# positional arguments first before keyword, keep order when every argument isn't keyword:
print(greeting(name="Johnny", last="Joestar", occation="leg surgery"))


# ~~~~~~PRINT() FUNCTION~~~~~~~~

## END= : adds the specified value to the end
print("niya", end=" not really \n")

## SEP= : if a list of string are to be printed, seperate them by something

print("9744", "4941", "74", sep="-")
