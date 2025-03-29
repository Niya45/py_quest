
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