import time

# creates a delay or timer of x seconds and runs the program after the time is pu
time.sleep(5)
print("timer is over")

# idea : create a timer that takes in the amount of hours to sleep and count down the seconds

timer = int(input("How many hours do you plan on sleeping (digits): "))
total_sec = timer * 3600

for i in range(total_sec, 0, -1):
    time.sleep(1)
    print(f"{i} more seconds")

print("TIME's UP. WAKE UP!!")