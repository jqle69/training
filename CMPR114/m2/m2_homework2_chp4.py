#Exercise 1
speed = int(input("Enter vehicle speed: "))
hours = int(input("Enter number of hours: "))
for i in range(1, hours+1):
    calc_distance = i * speed
    print(f"Hour: {i}\t\tDistance Traveled: {calc_distance}")



#Exercise 2
years = int(input("Enter number of years: "))

totalrain_year = 0
for year in range(1,years+1):
    totalrain = 0
    print(f"\nFor year {year}")
    for i in range(1,13):
        rain = float(input(f"Enter rain amount for month {i}: "))
        totalrain = totalrain + rain

    print(f"Total rainfall for year {year} in inches: {totalrain}")
    totalrain_year = totalrain_year + totalrain

avgrain = totalrain_year / (years*12)

print(f"\nTotal rainfall amount is {totalrain_year}.")
print(f"Average rainfall per month for period is {avgrain}.")

#Exercise 3
num = 1
totalsum = 0
while num > 0:
    num = int(input("Enter value greater than 0: "))
    if num > 0:
        totalsum = totalsum + num

print(f"Total Sum is {totalsum}.")