# Format specifiers : {value:flags}
# formatting a value based on the flags inserted

## DECIMAL POINTS
price = 100.9999999
age = 32.5
string1 = f"the price is {price:.2f}" #shows only two decimal points, rounds up the number if it's close
string2 = f"the age is {age:.3f}" #can concatenate 0s at the end if that many float points doesn't exist

print(string1, price)

## ALLOCATE SPACE TO DISPLAY VALUE (includes the value too)
price1 = 499.99
string3 = f"the price of that product is {price1:10}"
string4 = f"the price of that product is {price1:5}"
print(string3)
print(string4)

# the spaces will be 0 patted
print(f"the price of that product is {price1:10}")
# Left justify. Spaces will be at the end
print(f"the price of that product is {price1:<10}")
# Centre align. Text will be between the spaces
print(f"the price of that product is {price1:^10}")


# Adds + at the start IF the number is positive
print(f"the price of that product is {price1:+10}")
# Seperate thousands place with commas
print(f"the price of that product is {10000:,}")

## combine
price3 = 10000.533431
print(f"the price is {price:,.2f}")