speed = int(input("Enter vehicle speed: "))
hours = int(input("Enter number of hours: "))
for i in range(1, hours+1):
    calc_distance = i * speed
    print(f"Hour: {i}\t\tDistance Traveled: {calc_distance}")