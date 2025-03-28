# ARBITRARY ARG: multiple arguments without specific limit


## *ARGS:~~~~~
# add as many parameters as needed
# args are stored as tuple
# only one args

def spend_mil(*args):
    total_spend = 0
    for arg in args:
        total_spend += arg
    return f"You have {1000000 - total_spend} left!"

print(spend_mil(2, 2, 6666, 6666))

# Display name:
def dis_name(*args):
    name = ""
    for arg in args:
        print(arg, end=" ")

dis_name("Dr.", "Spongebob", "Jacob", "Squarepants", "IV")
print()

## *KWARGS: ~~~~~~~
# add as many keywords as needed
# args are stored as dictionary = "keyword": "value"
# only one kwargs
 
def final(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")

def final_I(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

final_I(
    niya=30, 
    anu=60,
    rinu=40,
    filu=56
    )
print()


### USE BOTH ~~~
# Positional args come before kwargs, even when passing arguments.
def shipping_usr(*args, **kwargs):
    for arg in args: 
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print()
    #if the person has a key called country, they will print the adress:
    if "country" in kwargs:
        print(f"{kwargs.get('country')}, {kwargs.get('state')}, {kwargs.get('city')}")
    else:
        print("no address specified (POTENTIAL SCAMMER)")

shipping_usr("Mr.", "Tony", "Abraham",
            country="japan",
            state="Osaka",
            city="minoh",
            street="2434")


