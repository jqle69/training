#Exercise 1
max_temp = 102.5
checkval = True
loopno = 0
totalval = 0

while checkval == True:
    tempval = float(input("Enter temperature under 102.5:  "))
    if tempval < max_temp:
        totalval = totalval+tempval
        loopno = loopno + 1
    else:
        checkval = False

avgval = totalval / loopno

print("Total value: ", str(totalval))
print("Average value: ", avgval)

#Exercise 2
checkval = 0
totalsales = 0.0
totalcomm = 0.0

while checkval < 4:
    sales = float(input("Enter the sales amount:  "))
    comm_rate = float(input("Enter the commission amount:  "))
    commission = sales * comm_rate
    totalsales = totalsales + sales
    totalcomm = totalcomm + commission
    checkval = checkval + 1
    
print("Total Sales Amount: $", format(totalsales, ",.2f"), sep="")
print(f"Total Commission Amount: ${totalcomm:,.2f}")

#Exercise 3
evenstr = ""
oddstr = ""
for num in [1,2,3,4,5,6,7,8,9,10]:
    numtype = num % 2
    if numtype == 0:
        evenstr = evenstr + str(num) + ","
    else:
        oddstr = oddstr + str(num) + ","

print("Even Numbers: " + evenstr[:-1])
print("Odd Numbers: " + oddstr[:-1])

#Exercise 4
for lname in ["Le"]:
    for fname in ["John"]:
        print(f"Your full name is {lname} {fname}")

#Exercise 5
for x in range(1, 11):
    print("Hello World - ", str(x))
