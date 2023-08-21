#Project 1
qty = int(input("Enter the quantity:"))

price = 0

if qty < 10:
    price = qty*5
elif qty<51:
    price = qty*4
else:
    price = qty*3

print(f"Total price: ${price:,.2f}")

#Project 2
salary = int(input("Entery your salary: "))

total = salary + (salary*.1)

print(f"The expected outcome is ${total:,.2f}.")

#Project 3
totalscore = 0

for i in range(4):
    score = int(input("Enter your score: "))
    totalscore += score

avg = totalscore/4

print(f"Expected outcomes is sum = {totalscore}, avg = {avg}")

#Project 4
salesamt = int(input("Enter sales amount: "))

if salesamt >=50000 and salesamt <= 60000:
    commission = 10
elif salesamt >=70000 and salesamt <= 80000:
    commission = 20
elif salesamt >=90000 and salesamt <= 100000:
    commission = 30

print(f"Commission is %{commission}")

#Project 5
cnt = 1
totalscore = 0
score = 0

while cnt < 5: 
        
    score = int(input("Enter your score value between 0 and 100: "))

    totalscore += score
    cnt += 1

avgscore = totalscore / 4

if avgscore > 100:
    print("Please re-enter 4 scores.")
else:
    if avgscore >= 90:
        grade = "A"
    elif avgscore >= 80:
        grade = "B"
    elif avgscore >= 70:
        grade = "C"
    elif avgscore >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f'Average score is : {avgscore:.2f}')
    print(f"Grade:  {grade}")

#Project 6
fat_intake = int(input("Enter fat gram consumed: "))
carb_intake = int(input("Enter carb gram consumed: "))

calories_fat = fat_intake* 9
calories_carb = carb_intake* 4

total = calories_fat + calories_fat

print(f"Calories from fat: {calories_fat}")
print(f"Calories from carbohydrates: {calories_carb}")
print(f"Total calories with a day:  {total}")

#Porject 7
file = open("C:\\Users\\17147\\Desktop\\CMPR114\\m3\\Coffee.txt", "r")
content = file.read()
print(content)

x = (1, 2, 3)
y = (4, 5, 6)
print(x + y)

count = 1
while count <= 5:
    print(count)
    count += 1

word = "Python"
for char in word:
    print(char)

x = 10
while x > 0:
    x -= 2
    print("1")
print(x)

x = (1, 2, 3)

y = (4, 5, 6)

print(x + y)