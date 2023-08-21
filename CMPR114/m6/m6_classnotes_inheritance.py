class vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")

class car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_model(self):
        print(f"Model: {self.model}")

car = car ("toyota", "tacoma")
car.show_brand()
car.show_model()

class shape:
    def area(self):
        pass

class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius
    
rect = rectangle(5,4)
cir = circle(7)

print(rect.area())
print(cir.area())
