# Import "path to file"

# when importing a file, 
    # give access to the functions and modules
    # executes the code inside the imported file: cause confusion and potential security crisises

# Solution:
    # Make sure the code is only executed when called directly
    # The code shouldn't run when it's imported, AND we need access to functions

def greet(name):
    print(f"Hello {name}!")
greet("Main-Branch User")

def greet2(name):
    print(f"Hello {name}! We uses")

if __name__ == "__main__":
    greet2("Main-Branch User")

## if the file is called directly
# __name__ == "__main__" :  
    # prints("main branch speaking")

## if the file is imported:
# __name__ == "side_branch.py"
    # doesn't execute what's inside __name__.


## USAGE:

def main():
    print()
    print("Block of code that triggers")
    greet2("natalie from main")

if __name__ == "__main__":
    main()