import os
import uuid
from classes.Product import Product
from classes.ParentModel import ParentModel
from utils.consts import ROOT_PATH, PRODUCTS_FILE


class ProductModel(ParentModel):
    products = []

    def load_products(self):
        file = self.__open_file("r")
        self.products = []
        if (file):
            for product in file:
                product = product.rstrip("\n").split(",")
                product_to_save = Product(
                    product[0], product[1], product[2], product[3], product[4])
                self.__save_product_to_list(product_to_save)
            file.close()

    def get_products(self):
        return self.products

    def save(self, product: Product) -> bool:
        file = self.__open_file("a")
        product.id = uuid.uuid4()
        if (file):
            file.write(
                f"{product.id},{product.name},{product.description},{product.price},{product.quantity}\n")
            file.close()
            self.__save_product_to_list(product)
            return True

        return False

    def update(self, product: Product) -> bool:
        is_updated = self.__update_in_file(product)
        if (is_updated):
            index = self.get_element_index(product, self.products)
            if (index != None):
                self.products[index].name = product.name
                self.products[index].description = product.description
                self.products[index].price = product.price
                self.products[index].quantity = product.quantity
        return is_updated

    def delete(self, product: Product):
        print("id", product.id)
        is_deleted = self.__delete_in_file(product)
        if (is_deleted):
            self.products.remove(product)

        return is_deleted

    def __save_product_to_list(self, product: Product):
        self.products.append(product)

    def __open_file(self, open_mode: str):
        try:
            file = open(os.path.abspath(
                f"{ROOT_PATH}\{PRODUCTS_FILE}"), mode=open_mode, encoding="utf-8")
            return file
        except FileNotFoundError:
            print(f"Sorry, the file {PRODUCTS_FILE} does not exist.")
            return None

    def __delete_in_file(self, product: Product):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            updated_lines = [
                line for line in lines if not line.startswith(str(product.id))]
            write_file = self.__open_file("w")
            write_file.writelines(updated_lines)
            write_file.close()
            return True
        return False

    def __update_in_file(self, product: Product):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            index = self.get_element_index_in_file(product, lines)
            lines[index] = f"{product.id},{product.name},{product.description},{product.price},{product.quantity}\n"
            write_file = self.__open_file("w")
            write_file.writelines(lines)
            write_file.close()
            return True
        return False
