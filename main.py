import os
from screens.ScreenManager import ScreenManager
from utils.consts import ROOT_PATH, CUSTOMERS_FILE, PRODUCTS_FILE, USERS_FILE, PRODUCTS_CATEGORY_FILE


def main():
    create_dirs()
    create_files()
    ScreenManager()


def create_dirs():
    if not os.path.exists(ROOT_PATH):
        os.makedirs(ROOT_PATH)
        print("Path has been created successfully")


def create_files():
    files = [CUSTOMERS_FILE, PRODUCTS_FILE, USERS_FILE, PRODUCTS_CATEGORY_FILE]

    for file in files:
        path = f"{ROOT_PATH}\{file}"
        if not os.path.exists(path):
            open(path, 'w').close()


main()
