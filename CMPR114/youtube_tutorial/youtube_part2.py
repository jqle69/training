###########################################################
# Compare two strings to find location where does not match
###########################################################

seq1 = 'abdckehdslkeidksalekdia'
seq2 = 'abdckehds2keidksalekdia'

zip_seqs = zip(seq1, seq2)
#print(list(zip_seqs))

enum_seqs = enumerate(zip_seqs)
#print(list(enum_seqs))

for i, (a,b) in enum_seqs:
    if a != b:
        print(f"index: {i}")


###########################################################
# Compare two strings to find location where does not match
###########################################################
mytuple = ([1,2],[3])
mytuple[1].append(4)

print(mytuple)

###########################################################
# Iterate through list indefinitely
###########################################################
import time
from itertools import cycle

lights = [('green', 2), ('yellow', 0.5), ('red', 2)]

colors = cycle(lights)
while True:
    c,s = next(colors)
    print(c)
    time.sleep(s)

###########################################################
# Remove prefix and suffix from values in list
###########################################################
links = ['www.b001.io', 
         'www.yahoo.com',
         'www.google.com',
         'www.people.com']

for link in links:
    print(link.removeprefix("www."))

for link in links:
    print(link.removesuffix(".com"))

for link in links:
    name = '.'.join(link.split('.')[0:-1])    #REMOVE LAST ITEM
    print(name)

###########################################################
# Caching functions for better performance
###########################################################
from functools import lru_cache

@lru_cache
def increment(num):
    print("running lines of code ")
    return(num)

print(increment(1))
print(increment(2))
print(increment(3))
print(increment(1))

###########################################################
# running code in parallel
###########################################################
import time
from threading import Thread

def do_this():
    print("starting this...")
    time.sleep(2)
    print("did this...")

def do_that():
    print("starting that...")
    time.sleep(3)
    print("did that...")

t1 = Thread(target=do_this)
t1.start()
t2 = Thread(target=do_that)
t2.start()

###########################################################
# random move mouse pointer
###########################################################
import pyautogui as pag
import random
import time

while True:
    x = random.randint(900,1500)
    y = random.randint(400,500)
    pag.moveTo(x,y, 0.2)
    time.sleep(1)

###########################################################
# Merge dictionary with default values
###########################################################
defval = {
    'name': 'NA',
    'email': 'NA',
    'phone': 'NA'
}

user_input = {
    'name': 'john',
    'phone': '714-555-1212'
}

defval |= user_input

print(defval)

###########################################################
# moving items to the beginning of list
###########################################################
items = [
    'knife',
    'plates',
    'glasses',
    'bowls',
    'bottles'
]

index = items.index("glasses")
item = items.pop(index)
items.insert(0, item)
print(items)

###########################################################
# list insert method
###########################################################
x = [1,2,3]
x.insert(5,3)
print(x)

###########################################################
# Capitalize first and last name
###########################################################
first = 'jOHN'
last = 'lE'
print(f'{first} {last}'.title())

###########################################################
# number of parameters changes
###########################################################
def average(a, b,c):
    avg = (a+b+c)/3
    return avg

print(average(10,20,25))

#instead
def average(*args):
    avg = sum(args)/len(args)
    return avg

print(average(10,20,25, 30, 50))
