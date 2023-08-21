class Orders:
    def __init__ (self, order_id, customer, productsPrice):
        self.order_id = order_id
        self.customer = customer
        self.productsPrice = productsPrice

    def get_total_price(self):
        total_price = 0
        for product in self.productsPrice:
            total_price+=product.price #pass and calculate the prices from the self.products
        return total_price

    def display_order(self):
        customer_info = self.customer.get_info()
        product_names = [product.name for product in self.productsPrice]
        return f"Order ID: {self.order_id} {self.customer} {self.productsPrice}"


