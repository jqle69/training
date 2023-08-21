class automobiles:
    def __init__(self, make, model, mileage, price, doors):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
        self.__doors = doors

    #mutator methods
    def set_make(self, value):
        self.__make = value
    def set_make(self, value):
        self.__model = value
    def set_make(self, value):
        self.__mileage = value
    def set_make(self, value):
        self.__price = value
    def set_doors(self, value):
        self.__doors = value

    #assessor methods
    def get_make(self):
        return self.__make
    def get_model(self):
        return self.__model
    def get_mileage(self):
        return self.__mileage
    def get_price(self):
        return self.__price
    def get_doors(self):
        return self.__doors

class car_demo(automobiles):
    def __init__(self, make, model, mileage, price):
        super().__init__(make, model, mileage, price)
