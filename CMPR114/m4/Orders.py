class Orders:
    def __init__ (self, orderid, customer, productprice):
        self.order_id = orderid
        self.customer = customer
        self.productprice = productprice

    def get_total_price(self):
        totalprice = 0
        for product in self.product:
            totalprice+=product.price()

        return totalprice
    
    def display_order(self):
        customer_info = self.customer.get_info()
        product_name = [product.name for product in self.productprice]

        return f"Order ID: {self.orderid} {self.customer} {self.productprice}"