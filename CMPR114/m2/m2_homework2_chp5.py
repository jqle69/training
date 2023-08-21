#Project 1
def calc_property_tax(input):
    global assesmentval
    assesmentval = input * .6
    property_tax = (assesmentval // 100) * .72
    return property_tax

def main():
    actualval = float(input("Enter Actual Property Value: "))

    tax = calc_property_tax(actualval)
    print(f"Assessment Value:  {assesmentval:,.2f}")
    print(f"Property Tax: {tax:,.2f}")

main()

#Project 2
def calc_totalsales(input1,input2,input3):
    totalsales = (input1 * 20) + (input2 * 15) + (input3 * 10)
    return totalsales

def main():
    salesA = float(input("Enter ticket sales for Class A: "))
    salesB = float(input("Enter ticket sales for Class B: "))
    salesC = float(input("Enter ticket sales for Class C: "))

    totalsales = calc_totalsales(salesA, salesB, salesC)
    print(f"Total Sales Amount:  {totalsales:,.2f}")

main()

#Exercise 3
def calc_statetax(input1):
    tax = (input1 * .05) 
    return tax

def calc_countytax(input1):
    tax = (input1 * .025) 
    return tax

def main():
    totalsales = float(input("Enter total sales for month: "))

    statetax = calc_statetax(totalsales)
    countytax = calc_countytax(totalsales)
    totaltax = countytax + statetax

    print(f"Total County Tax Amount:  {countytax:,.2f}")
    print(f"Total State Tax Amount:  {statetax:,.2f}")
    print(f"Total Monthly Sales Tax Amount:  {totaltax:,.2f}")

main()