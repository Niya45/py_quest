opinion = input("yes or no:").lower()

def check_opi(nu):
    if nu == "yes":
        return "I see, it's a controversial opinion though."
    elif nu == "no":
        return "I see, it's still debatable"
    else:
        return "Your opinion isn't valid"

print(check_opi(opinion))

