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


## weekdays
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


## isWorkingDay:

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