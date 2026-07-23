from enum import nonmember

from product import Product
from customer import Customer


class Store:
    """
    Représente un magasin avec ses produits et sa clientèle
    """
    # --------------------variables-------------------------
    products = []
    customers = []

    # ---------------------Methods---------------------------
    """
    Recherche d'un produit dans la liste des produits par son nom avec homogénéisation de la casse.
    :return: retourne le produit s'il existe sinon retourne None
    """
    def search_product(self, product_name):
        for product in self.products:
            name_of_product_in_store = product.name.lower()
            name_of_product_given_by_customer = product_name.lower()
            if name_of_product_in_store == name_of_product_given_by_customer:
                return product
        return None

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

    # -------------------Constructor-------------------------
    """
    Constructeur avec tous les paramètres
    """
    def __init__(self, products, customers):
        self.products = products
        self.customers = customers

