# Match-Case Statement: alternative to 'elif' statements
# cleaner and more readable

#match case_name:
#   case value1:
#       do this
#   case value2:
#       do this
#   case value3 | value4: (or)
#       do this
#   case _: (else)
#       do this

## Only patern maching /= condition checking
# weekdays
def check_today(day):
    match day:
        case 1:
            print("Today is Monday")
        case 2:
            print("Today is Tuesday")
        case 3:
            print("Today is Wednesday")
        case 4:
            print("Today is Thursday")
        case 5:
            print("Today is Friday")
        case 6:
            print("Today is Saturday")
        case 7:
            print("Today is Sunday")
        case _:
            print("Today is invalid")
check_today(3)
check_today("march 12")


# isWorkingDay:

def check_working_day(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("The day is working day")
        case "saturday" | "sunday":
            print("The day is weekend")
        case _:
            print("The day is compleatly invalid")

weekday = input("Enter a day: ")
check_working_day(weekday)

## Integrate Conditions to match case:

def is_smart(brainP):
    match brainP:
        case _ if brainP <= 50:
            return "Inferier"
        case _ if brainP > 50 and brainP <= 250:
            return "Stupid"
        case _ if brainP > 250 and brainP <= 500:
            return "Smart"
        case _ if brainP > 500 and brainP <= 1000:
            return "Genius"
        case _:
            return "GOD"

human = is_smart(750)    
cat = is_smart(100000)

print(human) # Output: Genius
print(cat) # Output: GOD