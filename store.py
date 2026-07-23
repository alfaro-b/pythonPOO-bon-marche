from enum import nonmember

from product import Product
from customer import Customer


class Store:

    # --------------------variables-------------------------
    products = []
    customers = []

    # ---------------------Methods---------------------------
    def search_product(self, product_name) -> Product:
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

    def sell_product(self, customer: Customer) -> None:
        """
        Vend un produit à un client.
        Affiche les produits, demande le produit et la quantité,
        vérifie la disponibilité du stock, met à jour le stock et
        ajoute le produit au panier client.
        :param customer: Client qui effectue l'achat
        """
        self.display_products()

        product_name = input("Quel produit souhaitez-vous acheter? ")
        # Recherche du produit demandé par le client
        product = self.search_product(product_name)
        # Vérifie si le produit existe
        if product is None:
            print("Veuillez choisir un produit disponible.")
            return

        quantity = float(input(f"Quelle quantité de {product.name} souhaitez-vous acheter? "))
        # Vérifie que la quantité saisie est valide
        if quantity <= 0:
            print("La quantité doit être supérieure à zéro.")
            return
        # Vérifie que le stock est suffisant
        if quantity > product.stock:
            print(
                f"Il ne reste pas assez de {product.name}. "
                f"Stock disponible : {product.stock} {product.unity}."
            )
            return
        # Met à jour le stock puis ajoute le produit au panier
        product.remove_from_stock(quantity)
        customer.cart.add_product(product, quantity)
