import os # to interact with the OS

# FILE HANDLING
# -------------------------------------------------------

"""
- R : read : error if file does not exist
- A : append : create if not exists, write at end
- W : write : create if not exists, overwrite if exists
- X : create (fails if file exists) : create if not exists, error if exists

- R+ : read and write : file must exist
- W+ : write and read : file must exist, overwrites if exist
- A+ : append and read : file must exist, writes at end
- X+ : create and read : file must not exist, creates it
"""

# READ THE FILE: 
# -------------------------------- 

# Open a file :~  
file = open("references/students.txt", "r")


# read the whole file:
file.read() 

# read the first 4 characters:
file.read(4) 

# reads the first line: 
file.readline()
file.readline() # reads next line

# reads all the lines:
file.readlines() 

"""
- loop through the file and print each line:

for line in file:
    print(line)
"""

# Close the file:~
file.close()

    
# APPEND TO THE FILE: adds to the end
# -------------------------------- 

def read_file(path):
    with open(path, "r") as file:
        print(file.read())
        # automatically closes the file

def append_file(path, info):
    with open(path, "a") as file:
        file.write(f"\n{info}")
        # automatically closes the file

book = input("Enter a book's name : ")

read_file("references/books.txt")
print("-----------------")
append_file("references/books.txt", book)
read_file("references/books.txt")

# WRITE TO THE FILE: overrides it
# -------------------------------

def write_file(path, info):
    with open(path, "w") as file:
        file.write(f"{info}\n")
        print("I deleted all what's already in this file --- ")
        # automatically closes the file


author = input("Enter an author's name : ")

read_file("references/authors.txt")
print("-----------------")
write_file("references/authors.txt", author)
read_file("references/authors.txt")

# Creates a file if doesn't exist with writing
write_file("references/new_file.txt", "New file")

# CREATE THE FILE: creates, errors if exists
# -------------------------------- 

def create_file(file_path):
    if os.path.exists(file_path):
        print("You cannot create the flie, it already exists")
    else:
        file = open(file_path, "x")
        file.close()
newf = input("Provide a name for the new file: ")
create_file(newf)


# DELETE THE FILES: deletes if exist, errors if not

def del_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("the file don't exist. How am i supposed to delete that?")

del_f = input("Enter the path to the file which i shall delete: ")
del_file(del_f)