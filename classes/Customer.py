from classes.GeneralClass import GeneralClass


class Customer(GeneralClass):
    def __init__(self, id, name, address, phone, nit) -> None:
        super().__init__(id, name)
        self.address = address
        self.phone = phone
        self.nit = nit
