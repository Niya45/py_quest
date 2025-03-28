# CONDITIONS : a block of code that runs on specific conditions
age = input("enter your age:")
if int(age) < 14:
    print("You cannot create an account.")
elif int(age) < 18 and int(age) > 14 :
    print("You need parental supervision to create an account")
elif int(age) >= 18:
    print("You successfully made an account.")

# LOGICAL OPERATORS : To combine two conditions.
    # or : one in two conditions have to be true
    # and : both conditions have to be true
    # not(condition) : the opposite of the condition

# == : equal to
# != : not equal to
# > : greater than
# >= : greater than or equal to
# < : less than
# <= : less than or equal to

# use booleans directly to check conditions:

que = input("what is the cube root of 512 ? (type H for hint):")
if que == "H":
    print("no hint for you!")
elif not(que == "H"):
    value = int(que)
    if value == 8:
        print("Correct! 1/4 point for you!")
    else:
        print("Nice try but you're way off!")

# another way to use not

name = ''
if not name: #if name have a value, "not" gives False and code breaks. if name doesn't have a value, "not" give True and code runs
    print("the name is invalid")
else:
    print(f"welcome to our service provider, {name}!")


# _____Conditional Expressions:_______
    # Single line expression of conditions

# no elifs are possible in this
# logical operators can be used
# can store the conditions in a variable or print them as it is
    # X if condition else Y
var = 0
bul = True if var > 0 and var <= 10 else False

print(bul)
