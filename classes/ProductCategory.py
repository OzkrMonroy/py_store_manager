from classes.GeneralClass import GeneralClass


class ProductCategory(GeneralClass):
    def __init__(self, id, name, description) -> None:
        super().__init__(id, name)
        self.description = description
