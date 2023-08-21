#Module 1 - Chapter 3

# Project 1 - Write code to handle exceptions 
def get_grade(score):
    if score >= 90 and score < 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

def checkinput(score):
    if score < 0 or score > 100:
        print("Invalid value.  Please enter values between 0 and 100")
        return False
    else:
        return True

score = int(input("Enter the score:  "))
result = checkinput(score)

if result == True:
    lettergrade = get_grade(score)
    print("Your grade is ", lettergrade)

# Project 2 -Complete existing code
import tkinter as tk

def submit():
    lastname = entry_lastname.get()
    firstname = entry_firstname.get()
    address = entry_address.get()
    city = entry_city.get()
    state = entry_state.get()
    zipcode = entry_zipcode.get()

    if lastname and firstname and address and city and state and zipcode:
        print("Last Name: ", lastname)
        print("First Name: ", firstname)
        print("Address: ", address)
        print("City: ", city)
        print("State: ", state)
        print("Zip Code: ", zipcode)
    else:
        print("Please fill in all fields.")

window = tk.Tk()

label_lastname = tk.Label(window, text = "Last Name: ")
label_lastname.pack()
entry_lastname = tk.Entry(window)
entry_lastname.pack()

label_firstname = tk.Label(window, text = "First Name: ")
label_firstname.pack()
entry_firstname = tk.Entry(window)
entry_firstname.pack()

label_address = tk.Label(window, text = "Address: ")
label_address.pack()
entry_address = tk.Entry(window)
entry_address.pack()

label_city = tk.Label(window, text = "City: ")
label_city.pack()
entry_city = tk.Entry(window)
entry_city.pack()

label_state = tk.Label(window, text = "State: ")
label_state.pack()
entry_state = tk.Entry(window)
entry_state.pack()

label_zipcode = tk.Label(window, text = "Zip Code: ")
label_zipcode.pack()
entry_zipcode = tk.Entry(window)
entry_zipcode.pack()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

window.mainloop()

# Project 3
def validate(val):
    if val < 0 or val > 36:
        print("Invalid value.  Please enter value between 0 and 36.")
        return False
    else:
        return True

def get_numtype(val):
    remainder = val % 2
    if remainder > 0:
        numtype = "odd"
    else:
        numtype = "even"

def get_color(val):
    numtype = get_numtype(val)

    if val == 0:
        return "Green"
    elif val >= 1 and val < 11:
        if numtype == "even":
            return "Black"
        else:
            return "Red"
    elif val >= 11 and val < 19:
        if numtype == "even":
            return "Red"
        else:
            return "Black"
    elif val >= 19 and val < 28:
        if numtype == "even":
            return "Black"
        else:
            return "Red"
    elif val >= 29 and val < 37:
        if numtype == "even":
            return "Red"
        else:
            return "Black"

val = int(input("Enter value between 0 and 36: "))

result = validate(val)

if result == True:
    color = get_color(val)
    print("The color is ", color, sep = "")
    
# Project 4 - Calculate Shipping Cost
def validate(weight):
    if weight < 0: 
        print("Invalid weight.  Please enter value greater than 0.")
        return False
    else:
        return True

def calculate_price(weight):
    if weight > 0 and weight <= 2:
        price = weight * 1.5
    elif weight > 2 and weight <= 6:
        price = weight * 3.0
    elif weight > 6 and weight <= 10:
        price = weight * 4
    else:
        price = weight * 4.75
    
    return price

weight = float(input("Enter shipping weight: "))

result = validate(weight)
if result == True:
    shippingprice = calculate_price(weight)
    print("Total shipping price is ${:,.2f}".format(shippingprice))