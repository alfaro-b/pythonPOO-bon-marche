from enum import nonmember

from product import Product
from customer import Customer


class Store:

    # --------------------variables-------------------------
    products = []
    customers = []

    # ---------------------Methods---------------------------
    def search_product(self, product_name):
        for product in self.products:
            name_of_product_in_store = product.name.lower()
            name_of_product_given_by_customer = product_name.lower()
            if name_of_product_in_store == name_of_product_given_by_customer:
                return product
        return None

    # -------------------Constructor-------------------------

    def __init__(self, products, customers):
        self.products = products
        self.customers = customers

