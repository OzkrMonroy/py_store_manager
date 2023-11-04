from models.ProductModel import ProductModel
from classes.Customer import Customer


class ProductController:
    product = ProductModel()
    is_to_update = None
    element_to_update = None

    def __init__(self) -> None:
        self.load_products()

    def load_products(self):
        self.product.load_products()

    def get_products(self):
        return self.product.get_products()

    def save(self, product: Customer) -> bool:
        return self.product.save(product)

    def update(self, product: Customer) -> bool:
        return self.product.update(product)

    def delete(self, product: Customer) -> bool:
        return self.product.delete(product)

    @classmethod
    def set_element_to_update(cls, product: Customer):
        cls.element_to_update = product
        cls.is_to_update = True

    @classmethod
    def get_element_to_update(cls):
        return [cls.is_to_update, cls.element_to_update]
