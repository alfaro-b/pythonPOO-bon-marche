from product import Product
from customer import Customer


class Store:

    # --------------------variables-------------------------

    # ---------------------Methods---------------------------

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
