# DUNDER METHOD : double underscore methods or magic methods

## built in dunder methods:

# INIT METHOD: __init__()
# Initializer for the attributes
# -----------------------------------------------------

# REPRESENTING METHOD: __repr__()
#   define the official string representation of an object. For Devs
#   When using "print()" : python fall back and use this if __str__ is not defined
# -----------------------------------------------------

# STR METHOD: __str__()
# define the official string representation of an object. For users
# When using "print()" : python calls this method
# -----------------------------------------------------


class Book:
    def __init__(self, name, author, genre, pagecount, status=False):
        self.name = name
        self.author = author
        self.genre = genre
        self.pagecount = pagecount # number read
        self.status = status # true == finished. false == not finished    
    
    # !r : uses the apropriate representation of the variable (quotation for string)
    
    def __repr__(self):
        return "{}(name={!r}, author={!r}, genre={!r}, pagecount={!r} status={!r})".format(self.__class__.__name__, self.name, self.author, self.genre, self.pagecount, self.status)
    
    def __str__(self):
        return (
            f"Book : {self.name}\n"
            f"Author : {self.author}\n"
            f"Genre : {self.genre}\n"
            f"Status : {'finished' if self.status else 'not finished'}"
        )
    
    def __len__(self):
        return len(self.name)

book1 = Book("Metamorphosis", "Franz Kafka", "Literary fiction", 100, True)
book2 = Book("And Then There Were None", "Agatha Christie", "Thriller", 25, False)

print(book1)
print(str(book2))
print(repr(book1))

## other built in dunder methods: and more

print("--------------------")

print(int.__add__(2,3)) # addition of two items :  2+3
print(str.__add__("ca", "t")) # concatenates two items : cat
print(f"The {book1.name} name's length {len(book1)}")
