#Exercise 1
def convert_to_miles(input):
    convert_val = input * 0.6214
    return convert_val

def main():
    userinput = float(input("Enter kilometer(s): "))

    newval = convert_to_miles(userinput)
    print(f"{userinput} kilometer(s) is equivalent to {newval} mile(s).")

main()

#Exercise 2
def yearly_auto_expense(payment, insurance, gas, oil, tires, maintenance):
    totalexpense = (payment + insurance + gas + oil + tires + maintenance) * 12
    return totalexpense 

def main():
    payment = float(input("Enter monthly loan payment: "))
    insurance = float(input("Enter enter monthly insurance payment: "))
    gas = float(input("Enter monthly gas cost: "))
    oil = float(input("Enter monthly oil cost: "))
    tires = float(input("Enter monthly tires cost: "))
    maintenance = float(input("Enter monthly maintenance: "))

    annualexpense = yearly_auto_expense(payment, insurance, gas, oil, tires, maintenance)

    print(f"\nMonthly payment is ${payment:,.2f}.")
    print(f"Monthly insurance is ${insurance:,.2f}.")
    print(f"Monthly gas is ${gas:,.2f}.")
    print(f"Monthly oil is ${oil:,.2f}.")
    print(f"Monthly tires is ${tires:,.2f}.")
    print(f"Monthly maintenance is ${maintenance:,.2f}.")
    print(f"Total automative annual expense is ${annualexpense:,.2f}.")

main()
