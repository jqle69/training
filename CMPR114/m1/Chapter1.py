# Module 1 - Chapter 1

# Exercise 1 - Print out your name ##
print("John Le")

## Exercise 2 - Print out calculation ##
salary = float(input("Enter Salary:  "))
bonus = float(input("Enter bonus:  "))
pay = salary + bonus

print("Your pay is ${:,.2f}".format(pay))

# Exercise 3 - Print out your name, address, city, state, and zip ##
firstname = input("Enter First Name:  ")
lastname = input("Enter Last Name:  ")
address = input("Enter Address:  ")
city = input("Enter City:  ")
state = input("Enter State:  ")
zipcode = str(input("Enter Zip Code:  "))

print("\n" + firstname + " " + lastname + "\n" +
      address + "\n" +
      city + ", " + state + " " + zipcode + "\n")

# Exercise 4 - Enter 2 people's name, and calculate pay average
firstname1 = input("Enter Employee#1 First Name:  ")
lastname1 = input("Enter Employee#1 Last Name:  ")
hourlypay1 = float(input("Enter Employee#1 Hourly Pay:  "))
hoursworked1 = float(input("Enter Employee#1 Hours Worked:  "))
subtotal1 = hourlypay1 + hoursworked1

firstname2 = input("Enter Employee#2 First Name:  ")
lastname2 = input("Enter Employee#2 Last Name:  ")
hourlypay2 = float(input("Enter Employee#2 Hourly Pay:  "))
hoursworked2 = float(input("Enter Employee#2 Hours Worked:  "))
subtotal2 = hourlypay2 + hoursworked2

avgpay = (subtotal1 + subtotal2) / 2

print("\nPay for " + firstname1 + " " + lastname1 + " is ${:,.2f}".format(subtotal1))
print("Pay for " + firstname2 + " " + lastname2 + " is ${:,.2f}".format(subtotal2))
print("The average pay for both people is ${:,.2f}".format(avgpay) + "\n")

# Exercise 5 - Calculate sales price based upon original price - discount
baseprice = float(input("Enter base price:  "))
discountpct = .20
discountval = baseprice * discountpct
saleprice = baseprice - discountval

print("\nBase price is ${:,.2f}".format(baseprice))
print("Discount is ${:,.2f}".format(discountval))
print("Sale price is ${:,.2f}".format(saleprice) + "\n")

# Exercise 6 - Calculate MPG
miles = float(input("Enter Miles Driven:  "))
gallons = float(input("Enter Gallons Used:  "))
mpg = miles / gallons

print("\nYour MPG is ", mpg)