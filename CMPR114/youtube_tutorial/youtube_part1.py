#########################################
# 1 - Time for optimized code
#########################################
from timeit import timeit

def normal() -> list[int]:
    return[i for i in (0,1,2,3,4)]

def optimized() -> list[int]:
    return[0,1,2,3,4]

normal: float = timeit(stmt=normal)
optimized: float = timeit(stmt=optimized)

print(f"normal time: {round(normal,4)}s")
print(f"optimized time: {round(optimized,4)}s")

#########################################
# 2 - format json in console
#########################################
from pprint import pprint
my_dict: dict = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Santa Ana',
        'zip': '92670',
        'contact': {
            'phone': '555-1212',
            'emal': 'happy@aol.com'
        }
    },
    'hobbies': ['walking', 'reading', 'cooking']
}
pprint (my_dict)
#########################################
# Adding cost together  
#########################################
class Expense:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __add__(self, other):
        return self.cost + other.cost
    
food = Expense('Food', 10)
fuel = Expense('Fuel', 20)

print(food+fuel)

#########################################
# formatting for print
#########################################
class Fruit:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def __str__(self):
        return f"{self.name} (${self.cost})"
    
banana = Fruit('Banana', 10.5)

print(banana)

#########################################
# check for not a number
#########################################
import math

#nan stands for not a number
value = float('nan') #'inf' is infinite

print(math.isnan(value))

#########################################
# print to file or console
#########################################
import sys
from datetime import datetime
now = datetime.now()
message = f"{now: %H:%M:%S} logged!"  #%d=day, %m=month, %Y=year, %H=hour, %M=minute, %S=seconds

#print to standard output in consile
print(message, file=sys.stdout)

#print to standard error in consile
print(message, file=sys.stderr)

# print to file
with open('Logs.tcxt', 'a') as myfile:
    print(message, file=myfile)

#########################################
# range values
#########################################
positive = range(0,3)
print(list(positive))

negative = range(0, -3, -1)
print(list(negative))

#########################################
# format percentage
#########################################
percent: float = .3754
print(f"{percent:.2%}")

#########################################
# assign same values to different variables
#########################################
a = 'test'
b = 'test'
c = 'test'

#same 
a, b, c = "test"

#same
a = b = c = "test"

#########################################
# while loop with break and else conditions
#########################################
i: int = 0
while i < 2:
    print(i)
    i+=1
    break
else:
    print("out")

#########################################
# while loop with break and else conditions
#########################################
mylist=(1, 'a', True)
a,b,c = mylist

#########################################
# permutations for a list
#########################################
from itertools import permutations
ls = ['a', 'b', 'c']
p = permutations(ls)
print(list(p))
p = permutations(ls,2)
print(list(p))

#########################################
# list comprehension
#########################################
groups = [[1,2],[3,4]]

for g in groups:
    for elem in g:
        print(elem, end=' ')

#sane
c = [elem
     for g in groups 
     for elem in g]

#sane
c = [elem for g in groups for elem in g]


#########################################
# list comprehension
#########################################
money = True
wife = True
house = True
food = True

if money and wife and house and food:
    print("good job")
else:
    print("missing")

#same
req = [money, wife, house, food]
if all(req):
    print("good job")
else:
    print("missing")

#########################################
# string
#########################################
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.printable)

#########################################
# random values
#########################################
import random as r
num = [1,2,3,4,5,6,7,8,9,0]

#return random value from list
value = r.choice(num)
print(value)

#return how many values returned based upon k value
value = r.choices(num, k=2)
print(value)

#########################################
# check value in list meets conditions
#########################################
l = [-1,0,1,2]

# check if anyvalues is greater than 0
if any(n>0 for n in l):
    print ('success')

# check if all values is greater than 2
if all(n>2 for n in l):
    print ('success')

#########################################
# copy a list independent from original
#########################################
a = [[1,2],[3,4]]
b = a.copy()
b[0] = 999

print(f"{a = }")
print(f"{b = }")

#correct
from copy import deepcopy
a = [[1,2],[3,4]]
b = deepcopy(a)
b[0][0] = 999

print(f"{a = }")
print(f"{b = }")

#########################################
# looping thru multiple list
#########################################

m1 = [1,2,3,4,5]
m2 = ['a','b','c','d','e']
m3 = ['!', '#', '$', '%', '&']

for a,b,c in zip(m1,m2,m3):
    print(a,b,c, sep=',')

#########################################
# string comparison
#########################################
text1 = "Strasse"
text2 = "StraBe"

a = text1.lower() #use casefold() which is caseless comparison
b = text2.lower()
print(f"{a}=={b}")
print(f"{a}=={b}")

#########################################
# get public IP address
#########################################
import requests as req
url: str = "https://checkip.amazonaws.com"
request = req.get(url)
ip: str = request.text

print(f"public ip address: {ip}")

#########################################
# lambda function
#########################################
add = lambda a,b: a+b
print(add(5,10))

names =  ['Sam', 'Kate', 'Lee', 'Jonathan', 'Andrew']
sortlist = sorted(names, key=lambda x:len(x))
print(list(sortlist))

#########################################
# use alt-shift to change multiple value names
#########################################
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0

#########################################
# sentinel values used to trigger the end of loop
#########################################
while True:
    user_input: str = input(">>")
    print(user_input, "<<")
    if user_input=="-1":
        print("done")
        break

#########################################
# exit or quit
#########################################
exit()
quit()

#instead
import sys
sys.exit()


#########################################
# retrieve values from dictation
#########################################
items: dict = {'a':1, 'b':2, 'c':3}
print(items['a'])

#instead so you can set default value if search item does not exists
print(items.get('x', None))

#########################################
# translate dictionary
#########################################
text: str = "l0ppx! pxp."

trans: dict = {'l': 'H', 
               '0':'e',
               'p':'l',
               'x':'o',
               '!':','}

table: dict = text.maketrans(trans)

print("Table: ", table)
print("Input: ", text )
print("Output: ", text.translate(table))

#########################################
# combine dictionary using union
#########################################
d1 = {'a':1,'b':2}
d2 = {'b': None,'c':3,'d':4}
d3 = {'e':5,'f':6}

combined = d1|d2|d3

print(combined)

#########################################
# find unique values in list
#########################################
numbers = [1,2,3,4,1,2,1,2,3,5]

unique = {num for num in numbers}
print(unique)

#########################################
# generate unique identifiers
#########################################
from uuid import uuid4
users = {'Mario':uuid4(), 'Luigi':uuid4()}
for name, id in users.items():
    print(name, id, sep=": ")

#########################################
# reduce code
#########################################
weather: str = 'CLEAR'
message: str = ''
if weather == 'CLEAR':
    message = "Nice"
else:
    message = "Bad"

print(message)

#instead
message: str = 'Nice' if weather == 'CLEAR' else 'Bad'
print(message)

#########################################
# using semicolon as statement separator
#########################################

text='Hi'; print(text)
a,b =1,2; c=a+b; print(c)

#########################################
# list using extend
#########################################
lista = [1,2,3]
listb = ['a','b','c']
newlist = lista+listb
print(newlist)

#instead
lista.extend(listb)
print(lista)


#########################################
# list all attributes/command for str and integer
#########################################
text: str = 'text'
number: int = 10

print(dir(text))
print(dir(number))

#instead
for a in dir(text):
    print(a)

for a in dir(number):
    print(a)

#########################################
# switch values
#########################################
a: int = 1
b: int = 2

c=a
a=b
b=c
del c
print('a', a)
print('b', b)

#instead
a, b = b, a

#########################################
# check if number exists in list
#########################################
if number in numlist:
    print("good")

#########################################
# dictionary comprehension
#########################################
names = ['John', 'Edward', 'James']

dict = {name: len(name) for name in names}

print(dict)

#########################################
# remove duplicates in list
#########################################
lista = [1,1,2,3,3,4,4,5,6,6,7]

new = list(set(lista))
print(new)


#########################################
# handling for loops
#########################################
for i in range(3):
    print(i)
    if i==1:
        break
else:
    print("done")

#########################################
# types of strings
#########################################
#formatted string
f_string = f"Results = {1+1}"
print(f_string)
#raw string
r_string = r"c:\user\folder\file"
print(r_string)
#friends string
fr_string = fr"c:\user\{1+1}"
print(fr_string)

#########################################
# merge dictionary
#########################################
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

new_dict = {**dict1, **dict2}
print(new_dict)


#########################################
# unlimited number of arguments for a function
#########################################
def add(*numbers):
    print(numbers)
    print(sum(numbers))

add(1,2,3,4,5)

#########################################
# Get CPU Count
#########################################
import multiprocessing as mp
print("CPUs: ", mp.cpu_count())

#########################################
# Generate 100 random numbers
#########################################
import random
rn = [random.randint(0,100)
      for _ in range(100)]
print(rn)


#########################################
# padding string values
#########################################
text = "12345"
print(f"{text}")
print(f"{text:0<10}")
print(f"{text:0>10}")