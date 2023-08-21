class Patient:
    def __init__(self, firstname, middlename, lastname, address, city, state, zipcode, phone, emergency_contact, emergency_phone):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.phone = phone
        self.emergency_contact = emergency_contact
        self.emergency_phone = emergency_phone

    def get_firstname(self):
        return self.firstname 

    def get_middlename(self, value):
        return self.middlename

    def get_lastname(self, value):
        return self.lastname

    def get_address(self, value):
        return self.address

    def get_city(self, value):
        return self.city

    def get_state(self, value):
        return self.state

    def get_zipcode(self, value):
        return self.zipcode

    def get_phone(self, value):
        return self.phone

    def get_emergency_contact(self, value):
        return self.emergency_contact

    def get_emergency_phone(self, value):
        return self.emergency_phone

    def get_patient_info(self):
        msg = f"Patient Name: {self.lastname}, {self.firstname} {self.middlename}\n"
        msg = msg + f"Address: {self.address}, {self.city}, {self.state} {self.zipcode}\n"
        msg = msg + f"Phone No: {self.phone}\n"
        msg = msg + f"Emergency Contact: {self.emergency_contact}\n"
        msg = msg + f"Emergency Contact Phone: {self.emergency_phone}\n"
             
        return msg
        
    def set_firstname(self, value):
        self.firstname = value

    def set_middlename(self, value):
        self.middlename = value

    def set_lastname(self, value):
        self.lastname = value

    def set_address(self, value):
        self.address = value

    def set_city(self, value):
        self.city = value

    def set_state(self, value):
        self.state = value

    def set_zipcode(self, value):
        self.zipcode = value

    def set_phone(self, value):
        self.phone = value

    def set_emergency_contact(self, value):
        self.emergency_contact = value

    def set_emergency_phone(self, value):
        self.emergency_phone = value
