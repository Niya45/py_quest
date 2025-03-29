# CONDITIONS : a block of code that runs on specific conditions
age = input("enter your age:")
if int(age) < 14:
    print("You cannot create an account.")
elif int(age) < 18 and int(age) > 14 :
    print("You need parental supervision to create an account")
elif int(age) >= 18:
    print("You successfully made an account.")


# _____Conditional Expressions:_______
    # Single line expression of conditions

# no elifs are possible in this
# logical operators can be used
# can store the conditions in a variable or print them as it is
    # X if condition else Y
var = 0
bul = True if var > 0 and var <= 10 else False

print(bul)
