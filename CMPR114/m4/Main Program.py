from Customers import Customers #use the functions in the customer class
from Orders import Orders #use the functions in the orders class

customer = Customers("Jason Sim","Sim_Jason@sac.edu", '111-111-11111')

class Product:
    def __init__(self, name, price):
        self.name =  name
        self.price = price

products1 = Product("Laptop", 1000)
products2 = Product("Paper", 10)
products3 = Product("Pencils", 5)

#instance of a class
#declaring a variable to be the instance of the class
order = Orders(100, customer,[products1, products2,products3])


print(order.display_order())

print("total price : ", f"{order.get_total_price():,.2f}")









