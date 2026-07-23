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

    def display_products(self) -> None:
        """
        Affiche les produits du magasin.
        """
        # enumerate permet de parcourir la liste en récupérant l'indice (à partir de 1) et le produit
        for index, product in enumerate(self.products, start=1):
            print(
                # :.2f permet d'afficher le prix avec 2 décimales
                f"{index}. {product.name} - "
                f"{product.price:.2f} €/{product.unity} - "
                f"Stock : {product.stock} {product.unity}"
            )
