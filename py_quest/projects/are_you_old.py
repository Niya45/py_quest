print("___WELCOME TO 'are you old?'___")
name = input("Insert your name: ")
age = input("what is your age? : ")
confirm = input("are you sure you wanna continue? (Y/n)")

def check(n, a):
    if int(a) < 20:
        return f"Don't worry {n}, you're not old yet."
    if int(a) > 20 and int(a) < 30:
        return f"It's not bad {n} you still have time before being old."
    if int(a) > 30 and int(a) < 40:
        return "According to me, You might start balding soon!. I recommend a NON-BALDING oil to keep your silky hair."
    if int(a) > 40 and int(a) < 60:
        return "You are OLD. I'm sure your head is already balding."
    if int(a) > 60 and int(a) < 90:
        return "You are OOLLLD. Your name is wierd too, "
    if int(a) > 90:
        return "How you sill alive?"


if str(confirm) == "Y":
    print(check(name, age))
else:
    quit()