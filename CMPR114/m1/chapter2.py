# Module 1 - Chapter 2

# Exercise 1
future_value = float(input("Enter the desired future value:  "))
rate = float(input("Enter the annual interest rate:  "))
years = int(input("Enter the number of years the money will grow:  "))

present_value = future_value / (1.0 + rate) ** years

print("You will need to deposit this amount", int(present_value))

# Exercise 2
totalsales = float(input("Enter Projected Total Sales Amount:  "))
profitpct = .23
profit = totalsales * profitpct

print("Estimated profit amount will be", profit)

# Exercise 3
billamt = float(input("Enter Bill Amount:  "))
taxamt = billamt * .07
tip = billamt * .18
totalbill = billamt + taxamt + tip

print("\nOriginal Bill Amount is ${:,.2f}".format(billamt))
print("Tax Amount is ${:,.2f}".format(taxamt))
print("Tip Amount is ${:,.2f}".format(tip))
print("Total Bill Amount is ${:,.2f}".format(totalbill))

# Exercise 4
mencnt = float(input("Enter number of men in class:  "))
womencnt = float(input("Enter number of women in class:  "))

total = mencnt + womencnt
menpct = (mencnt / total) * 100
womenpct = (womencnt / total) * 100

print("Percentage of men in class is %{:,.2f}".format(menpct))
print("Percentage of women in class is %{:,.2f}".format(womenpct))

# Exercise 5
sharesheld = 2000
purchase_shareprice = 40.00
sold_shareprice = 42.75
commpct = .03

origvalue = sharesheld * purchase_shareprice
currvalue = sharesheld * sold_shareprice
commission = origvalue * commpct
profit = currvalue - origvalue - commission

print("\nOriginal Value:  ${:,.2f}".format(origvalue))
print("Broker Fee Amount:  ${:,.2f}".format(commission))
print("Current Value:  ${:,.2f}".format(currvalue))
print("Total Profit:  ${:,.2f}".format(profit) + "\n")
