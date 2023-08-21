#Exercise 1
for i in ['Texas', 'California']:
    birds = int(input(f"Enter the number of birds for {i}: " ))
    print(f"{i} has {birds} birds.\n")

#Exercise 2
def get_fullname():
    lastname = input("Enter Last Name: ")
    firstname = input("Enter First Name: ")
    fullname = firstname + " " + lastname
    return fullname

def get_address():
    address = input("Enter Address: ")
    return address

def get_city():
    city = input("Enter City: ")
    return city

def get_state():
    state = input("Enter State: ")
    return state

def get_zipcode():
    zipcode = input("Enter ZipCode: ")
    return zipcode

name = get_fullname()
address = get_address()
city = get_city()
state = get_state()
zip = get_zipcode()

print("\n" + name)
print(address + ", " + city + " " + state + " " + zip + "\n")

#Exercise 3
def add(num1, num2, num3):
    global total
    total = num1 + num2 + num3
    return total

add(3,4,5)
print(f"Total : {total}")

#Exercise 4
def add():
    global total
    total = num1 + num2 + num3
    return total

global num1, num2, num3
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))
total = 0

add()
avg = total / 3

print(f"Total: {total}")
print(f"Average: {avg}")

#Exercise 5
def calc_pay(hours_worked, hourly_pay):
    totalpay = hours_worked * hourly_pay
    return totalpay

hours_worked = int(input("Enter hours worked: "))
hourly_pay = float(input("Enter hourly pay: "))

totalpay = calc_pay(hours_worked, hourly_pay
                    )
print(f"Hours worked is {hours_worked}")
print(f"Hourly pay is {hourly_pay}")
print(f"Total pay is ${totalpay:,.2f}")