#Exercise 1
MAX = 5
total = 0.0

print("This program calculates the sum of ")
print(f"{MAX} numbers you will enter.")

for counter in range(MAX):
    number = int(input("Enter a number: "))
    total = total + number

avgval = total / MAX
print(f"The total is {total}.")
print(f"The average is {avgval}.")

#Exercise 2
xval = 10
product = 0
while product < 100:
    user_input = int(input("Enter a number: "))
    product = user_input * xval
    if product < 100:
        print(f"The product value is {product}.")
    else:
        print("The product value is greater than 100.")
        break

    

#Exercise 3
MAX= 5
totalcnt = 0
for days in range(MAX):
    bugcnt = int(input(f"Enter number of bugs collected for Day {days+1}: "))
    totalcnt = totalcnt + bugcnt

print(f"Total bugs collected:  {totalcnt}")

#Exercise 4
calsmin = 4.2
for display in (10,15,20,25,30):
    totalcal = display * calsmin
    print(f"Total calories burned in {display} minutes is {totalcal}.")

#Exercise 5
from datetime import time
maxval = 0
minval = 0
totaltime = 0
def convert_to_sec(min, sec):
    total = 0
    if min > 0:
        total = (min * 60)
    
    if sec > 0:
        total = total + sec
    
    return total

counter = int(input("Enter the number of times around the track: "))
for loop in range(counter):
    timestr = input("Enter times in format MM:SS:  ").split()
    for time in timestr:
        min, sec = [int(i) for i in time.split(":")]

    timeval = convert_to_sec(min, sec)
    totaltime = totaltime + timeval
    if timeval < minval or minval == 0:
        minval = timeval
    
    if timeval > maxval:
         maxval = timeval

avgval = totaltime / counter

print(f"\nThe max time is: {maxval} seconds.")
print(f"The min time is: {minval} seconds.")
print(f"The average time is: " + format(avgval, ",.2f") + " seconds.")

