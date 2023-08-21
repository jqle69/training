# Exercise 1 - Display PII Data
fullname = "John Le"
address = "123 Main St"
city = "Santa Ana"
state = "CA"
zipcode= "92706"
telephoneno = "(800) 555-5555"
major = "Computer Science Engineering"

print("Name: " + fullname + 
      "\nAddress: " + address +
      "\nCity: " + city +
      "\nState: " + state + 
      "\nZipcode: " + zipcode +
      "\nTelephone No: " + telephoneno +
      "\nCollege Major: " + major + "\n")

# Exercise 2 - Calculate Total Purchase Amount
price1 = float(input("Enter item #1 price: "))
price2 = float(input("Enter item #2 price: "))
price3 = float(input("Enter item #3 price: "))
price4 = float(input("Enter item #4 price: "))
price5 = float(input("Enter item #5 price: "))

totalprice = price1 + price2 + price3 + price4 + price5
salestaxpct = .07
salestax = totalprice * salestaxpct
totalamount = totalprice + salestax

print("\nSubtotal: ${:,.2f}".format(totalprice))
print("Sales Tax: ${:,.2f}".format(salestax))
print("Total Amount: ${:,.2f}".format(totalamount))

# Exercise 3 - Complete Sales Tax Program
foodcharge = float(input("Enter food charge:  "))
salestax = round(foodcharge * .07, 2)
tip = round(foodcharge * .18, 2)
totalcharge = foodcharge + salestax + tip

print("Charge: ", foodcharge)
print("Sales Tax: ", salestax)
print("Tip: ", tip)
print("Total charges are ${:,.2f}".format(totalcharge))

# Exercise 4 - Ingredient Adjuster
cookiecnt = int(input("Enter number of cookies: "))

if cookiecnt <= 48:
    batchcnt = 1
else:
    batchcnt = cookiecnt // 48
    remainder = cookiecnt % 48
    if remainder > 0:
        batchcnt = batchcnt + 1

sugar = batchcnt * 1.5
butter = batchcnt
flour = batchcnt * 2.75

print("Total cups of sugar needed: ", sugar)
print("Total cups of butter needed: ", butter)
print("Total cups of flour needed: ", flour)

# Exercise 5 - Quarter of the Year
def calc_quarter(monthval):
    if monthval >= 1 and monthval < 4:
        quarter = "1st"
    elif monthval >= 4 and monthval < 7:
        quarter = "2nd"
    elif monthval >= 7 and monthval < 10:
        quarter = "3rd"
    else:
        quarter = "4th"
    
    return quarter

def validate(monthval):
    if monthval < 1 or monthval > 12:
        return False
    else:
        return True

monthval = int(input("Please enter value between 1 and 12:  "))

result = validate(monthval)

if result == True:
    val = calc_quarter(monthval)
    print("\nIt is the " + val + " Quarter\n")

# Exercise 6 - Hot Dog Cookout Calculator
peoplecnt = int(input("Enter number of people attending:  "))
hotdogcnt = int(input("Minimum number of hot dogs per person: "))

totalhotdogs = peoplecnt * hotdogcnt
hotdogspkg = totalhotdogs // 10
hotdogsrem = totalhotdogs % 10
if hotdogsrem > 0:
    hotdogspkg = hotdogspkg + 1
    hotdogsleftover = (hotdogspkg * 10) - totalhotdogs
else:
    hotdogsleftover = 0

bunspkg = totalhotdogs // 8
bunsrem = totalhotdogs % 8
if bunsrem > 0:
    bunspkg = bunspkg + 1
    bunsleftover = (bunspkg * 8) - totalhotdogs
else:
    bunsleftover = 0

print("Number of hot dog packages required: ", hotdogspkg)
print("Number of buns packages required: ", bunspkg)
print("Number of hot dogs leftover: ", hotdogsleftover)
print("Number of buns leftover: ", bunsleftover)

# Exercise 7 - Software Sales
def calc_discount(quantity):
    discount = 0
    if quantity >= 10 and quantity < 20:
        discount = .1
    elif quantity >= 20 and quantity < 50:
        discount = .2
    elif quantity >= 50 and quantity < 100:
        discount = .3
    else:
        discount = .4
    
    return discount

cost = 99.0
quantity = int(input("Please enter number of packages ordered:  "))

totalcost = quantity * cost
discountpct = calc_discount(quantity)
totaldiscount = totalcost * discountpct
finalprice = totalcost - totaldiscount

print("Initial Cost:  ${:,.2f}".format(totalcost))
print("Discount:  ${:,.2f}".format(totaldiscount))
print("Final Cost:  ${:,.2f}".format(finalprice))
