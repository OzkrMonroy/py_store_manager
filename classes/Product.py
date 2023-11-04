from classes.GeneralClass import GeneralClass

# TODO: add category later


class Product(GeneralClass):
    def __init__(self, id, name, description, price, quantity) -> None:
        super().__init__(id, name)
        self.description = description
        self.price = price
        self.quantity = quantity
