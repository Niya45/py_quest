
#_____STRINGS_____

# print(help(str))

# Different ways to create strings
stri1 = "hello"        # String with double quotes
stri2 = '23'           # String with single quotes
stri3 = "True"         # String can contain any characters
stri4 = 'niya\'s'      # Using escape character for apostrophe

# __f-string__

name = "niya"
age = 14
price = 10.99
is_smart = False

# Embedding variables in strings
print(f"Hello, {name}")
print(f"You are {age} years old")
print(f"The dress costs ${price}")
print(f"Are you smart: {is_smart}")

# Multiple variables in one f-string
print(f"Hello, {name}, {stri1}")

# _______STRING METHODS________
var_min = "I hate the number Four"

## ~~~Length and Case Manipulation~~~

# Length of string
print(len(var_min))  # Get string length

# Case transformations
print(var_min.lower())        # Convert to lowercase
print(var_min.upper())        # Convert to uppercase
print(var_min.capitalize())   # Capitalize first letter
print(var_min.title())        # Capitalize first letter of each word


## ~~~String Checking Methods~~~

# Checking string characteristics
print(var_min.islower())      # Check if all characters are lowercase
print(var_min.isupper())      # Check if all characters are uppercase

# Chaining methods
print(var_min.upper().isupper())  # Convert to uppercase, then check

# Type checking
pi = "314159"
print(pi.isdigit())           # Check if string contains only digits
print(var_min.isalpha())      # Check if string contains only alphabetic characters
print(var_min.count(" "))     # Count occurrences of a substring

## ~~~ Indexing and Accessing Characters ~~~

# Accessing individual characters
print(var_min[0])             # First character
print(var_min.index("F"))     # Index of first occurrence of "F"

## ~~~ String Modification ~~~

# Replacing parts of a string
phrase = "Capibara Academy"
new_phrase = phrase.replace("Capibara", "Llama")  # Returns new string
print(new_phrase)  # Note: original string remains unchanged

# Removing characters
emptied_phrase = phrase.replace("Capibara", "")

## ~~~ String Splitting and Finding ~~~

# Splitting strings
phrase1 = "niya2323.gmail.com"
email_parts = phrase1.split(".")  # Split by period
print(email_parts)

# Finding character positions
name = "albert"
first_a = name.find("a")       # First occurrence of "a"
print(first_a)

name = "llama"
last_a = name.rfind("a")       # Last occurrence of "a"
print(last_a)

## 