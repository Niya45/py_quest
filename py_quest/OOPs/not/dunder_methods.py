class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    # __str__: Called by str() and print() to get a readable string representation
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    # __repr__: Called by repr() to get an unambiguous string representation
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    # __len__: Called by len() to get the length of the object
    def __len__(self):
        return self.pages
    
    # __add__: Called when using the + operator
    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented
    
    # __eq__: Called when using the == operator
    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title and 
                    self.author == other.author and 
                    self.pages == other.pages)
        return NotImplemented

# Creating book objects
book1 = Book("Python Programming", "John Smith", 300)
book2 = Book("Python Programming", "John Smith", 300)
book3 = Book("Data Science", "Jane Doe", 250)

# Using dunder methods
print(str(book1))      # Output: Python Programming by John Smith
print(repr(book1))     # Output: Book('Python Programming', 'John Smith', 300)
print(len(book1))      # Output: 300
print(book1 + book3)   # Output: 550
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False

# Example of __getitem__ and __setitem__
class Library:
    def __init__(self):
        self.books = []
    
    def __getitem__(self, index):
        return self.books[index]
    
    def __setitem__(self, index, value):
        self.books[index] = value
    
    def add_book(self, book):
        self.books.append(book)

# Using the Library class
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library[0])  # Output: Python Programming by John Smith
library[0] = Book("New Book", "New Author", 400)
print(library[0])  # Output: New Book by New Author 