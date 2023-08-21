class Customers:
    def __init__(self, name, address, city, state, zipcode, phone):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone= phone

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address
    
    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state
    
    def set_zipcode(self, zipcode):
        self.__zipcode = zipcode
    
    def set_phone(self, phone):
        self.__phone = phone
