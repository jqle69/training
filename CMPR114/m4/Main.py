from Customers import Customers
from Orders import Orders

customer = Customers("John Le", "abc@ghc.com", "800-111-2222")

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

product1 = Product("Laptop", 1999)
product2 = Product("Monitor", 300)
product3 = Product("Keyboard", 45)

order = Orders(100, customer, [product1,product2,product3])

print(order.display_order())
print(f"total price: {order.get_total_price:,.2f}")

