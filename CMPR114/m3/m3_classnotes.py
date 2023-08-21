def write():
    outfile = open('sample.txt', 'w')
    outfile1 = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\sample1.txt", "a")

    outfile.write("John\n")
    outfile.write("Ella\n")
    outfile.write("Jose\n")
    outfile.write("Betty\n")

    outfile1.write("Edward")
    outfile1.write("Bella")
    outfile1.write("Jake")
    outfile1.write("Screech")

    outfile.close
    outfile1.close

write()

def read():
    infile = open('sample.txt', 'r')
    infile1 = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\sample1.txt", "r")

    fileContent = infile.read()
    fileContent1 = infile.read()

    print(fileContent)
    print(fileContent1)

    infile.close
    infile1.close

read()

import random

def r():
    min = 1
    max = 6

    global num 

    again = 'y'

    while again == 'y':
        num = random.randint(min, max)
        print('rolling the dice')
        print('the values are ')
        print(num)
    
        again = input("roll again. press y for yes or n for no? ").lower()

r()

outfile = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise3.txt", "a")
outfile.newlines
outfile.write("Number rolled:  " + str(num))
print("Recorded data.")

#Exercise 4
def sales():
    num_days = int(input("days of sales: "))
    sales_file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise3.txt", "w")

    for item in range(1,num_days+1):
        sale = input(f"enter sales for day {item}: " )
        sales_file.write(f"Sale Amount for day {item} is {sale}")
        sales_file.newlines

    sales_file.close
    print("record sales")

sales()

def readsales():
    sale_file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\exercise3.txt", "r")
    line = sale_file.readline()

    while line != '':
        amount=float(line)
        print(format(amount, ',.2f'))

        line = sale_file.readline()

    sale_file.close
    print("read done")

readsales()

numbers1 = [1,2,3,4,5,6,7,8,9,10]
numbers2 = [[1,2,3,4,5],[6,7,8,9,10]]
numbers3 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(numbers1[7])
print(numbers2[1][3])
print(numbers3[2][2])

#Arrays 
names = {"Jason", "Jane", "Juan", "1", 2, 3}
numbers = {1,2,3,4,5}
sum_of_numbers = 0

for n in names :
    #sum_of_numbers+=n
    print(sum_of_numbers)
    print(str(names[n]))
    sum_of_numbers+=1

print("The sum is :", sum_of_numbers)




