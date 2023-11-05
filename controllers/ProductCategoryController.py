from models.ProductCategoryModel import ProductCategoryModel
from classes.ProductCategory import ProductCategory


class ProductCategoryController:
    category = ProductCategoryModel()
    is_to_update = None
    element_to_update = None

    def __init__(self) -> None:
        self.load_categories()

    def load_categories(self):
        self.category.load_categories()

    def get_categories(self):
        return self.category.get_categories()

    def save(self, category: ProductCategory) -> bool:
        return self.category.save(category)

    def update(self, category: ProductCategory) -> bool:
        return self.category.update(category)

    def delete(self, category: ProductCategory) -> bool:
        return self.category.delete(category)

    @classmethod
    def set_element_to_update(cls, category: ProductCategory):
        cls.element_to_update = category
        cls.is_to_update = True

    @classmethod
    def get_element_to_update(cls):
        return [cls.is_to_update, cls.element_to_update]
