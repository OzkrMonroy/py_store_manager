import os
import uuid
from classes.ProductCategory import ProductCategory
from classes.ParentModel import ParentModel
from utils.consts import ROOT_PATH, PRODUCTS_CATEGORY_FILE


class ProductCategoryModel(ParentModel):
    categories = []

    def load_categories(self):
        file = self.__open_file("r")
        self.categories = []
        if (file):
            for category in file:
                category = category.rstrip("\n").split(",")
                category_to_save = ProductCategory(
                    category[0], category[1], category[2])
                self.__save_category_to_list(category_to_save)
            file.close()

    def get_categories(self):
        return self.categories

    def save(self, category: ProductCategory) -> bool:
        file = self.__open_file("a")
        category.id = uuid.uuid4()
        if (file):
            file.write(
                f"{category.id},{category.name},{category.description}\n")
            file.close()
            self.__save_category_to_list(category)
            return True

        return False

    def update(self, category: ProductCategory) -> bool:
        is_updated = self.__update_in_file(category)
        if (is_updated):
            index = self.get_element_index(category, self.categories)
            if (index != None):
                self.categories[index].name = category.name
                self.categories[index].description = category.description
        return is_updated

    def delete(self, category: ProductCategory):
        is_deleted = self.__delete_in_file(category)
        if (is_deleted):
            self.categories.remove(category)

        return is_deleted

    def __save_category_to_list(self, category: ProductCategory):
        self.categories.append(category)

    def __open_file(self, open_mode: str):
        try:
            file = open(os.path.abspath(
                f"{ROOT_PATH}\{PRODUCTS_CATEGORY_FILE}"), mode=open_mode, encoding="utf-8")
            return file
        except FileNotFoundError:
            print(f"Sorry, the file {PRODUCTS_CATEGORY_FILE} does not exist.")
            return None

    def __delete_in_file(self, category: ProductCategory):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            updated_lines = [
                line for line in lines if not line.startswith(str(category.id))]
            write_file = self.__open_file("w")
            write_file.writelines(updated_lines)
            write_file.close()
            return True
        return False

    def __update_in_file(self, category: ProductCategory):
        read_file = self.__open_file("r")
        if read_file:
            lines = read_file.readlines()
            read_file.close()
            index = self.get_element_index_in_file(category, lines)
            lines[index] = f"{category.id},{category.name},{category.description}\n"
            write_file = self.__open_file("w")
            write_file.writelines(lines)
            write_file.close()
            return True
        return False
