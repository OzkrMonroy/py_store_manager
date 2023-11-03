from models.CustomerModel import CustomerModel
from classes.Customer import Customer


class CustomerController:
    customer = CustomerModel()
    is_to_update = None
    element_to_update = None

    def __init__(self) -> None:
        self.load_customers()

    def load_customers(self):
        self.customer.load_customers()

    def get_customers(self):
        return self.customer.get_customers()

    def save(self, customer: Customer) -> bool:
        return self.customer.save(customer)

    def update(self, customer: Customer) -> bool:
        return self.customer.update(customer)

    def delete(self, customer: Customer) -> bool:
        return self.customer.delete(customer)

    @classmethod
    def set_element_to_update(cls, customer: Customer):
        cls.element_to_update = customer
        cls.is_to_update = True

    @classmethod
    def get_element_to_update(cls):
        return [cls.is_to_update, cls.element_to_update]
