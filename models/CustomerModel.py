import os
import uuid
from classes.Customer import Customer
from classes.ParentModel import ParentModel
from utils.consts import ROOT_PATH, CUSTOMERS_FILE


class CustomerModel(ParentModel):
    customers = []

    def load_customers(self):
        file = self.__open_file("r")
        self.customers = []
        if (file):
            for customer in file:
                customer = customer.rstrip("\n").split(",")
                customer_to_save = Customer(
                    customer[0], customer[1], customer[2], customer[3], customer[4])
                self.__save_customer_to_list(customer_to_save)
            file.close()

    def get_customers(self):
        return self.customers

    def save(self, customer: Customer) -> bool:
        file = self.__open_file("a")
        customer.id = uuid.uuid4()
        if (file):
            file.write(
                f"{customer.id},{customer.name},{customer.address},{customer.phone},{customer.nit}\n")
            file.close()
            self.__save_customer_to_list(customer)
            return True

        return False

    def update(self, customer: Customer) -> bool:
        is_updated = self.__update_in_file(customer)
        if (is_updated):
            index = self.get_element_index(customer, self.customers)
            if (index != None):
                self.customers[index].name = customer.name
                self.customers[index].address = customer.address
                self.customers[index].phone = customer.phone
                self.customers[index].nit = customer.nit
        return is_updated

    def delete(self, customer: Customer):
        print("id", customer.id)
        is_deleted = self.__delete_in_file(customer)
        if (is_deleted):
            self.customers.remove(customer)

        return is_deleted

    def __save_customer_to_list(self, customer: Customer):
        self.customers.append(customer)

    def __open_file(self, open_mode: str):
        try:
            file = open(os.path.abspath(
                f"{ROOT_PATH}\{CUSTOMERS_FILE}"), mode=open_mode, encoding="utf-8")
            return file
        except FileNotFoundError:
            print(f"Sorry, the file {CUSTOMERS_FILE} does not exist.")
            return None

    def __delete_in_file(self, customer: Customer):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            updated_lines = [
                line for line in lines if not line.startswith(str(customer.id))]
            write_file = self.__open_file("w")
            write_file.writelines(updated_lines)
            write_file.close()
            return True
        return False

    def __update_in_file(self, customer: Customer):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            index = self.get_element_index_in_file(customer, lines)
            lines[index] = f"{customer.id},{customer.name},{customer.address},{customer.phone},{customer.nit}\n"
            write_file = self.__open_file("w")
            write_file.writelines(lines)
            write_file.close()
            return True
        return False
