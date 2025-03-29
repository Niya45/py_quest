# DEFAULT ARGUMENTS: Assigning default values to parameters so the function will still work without anything passed to it

# default tax is 5
def price(price, tax=4):
    return f"$ {price + (price * (tax/100))}"

print(price(100))
# default arg can be overridden by an argument:
print(price(100,70))

# Default arguments comes after positional arguments
def count(end,start=0):
    while start<=end:
        print(start)
        start += 1
        
count(10,1)