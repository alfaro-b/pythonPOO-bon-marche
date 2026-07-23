from product import Product
from cart_item import CartItem


class Cart:
    """
    Représente le panier d'un client.
    """

    def __init__(self):
        """
        Initialise un panier vide.
        """
        self.items: list[CartItem] = []

    def add_product(self, product: Product, quantity: float) -> None:
        """
        Ajoute un produit au panier.
        :param product: Produit à ajouter.
        :param quantity: Quantité souhaitée.
        """
        pass

    def total(self) -> float:
        """
        Calcule le montant du panier.
        :return: Montant total du panier.
        """
        cart_total: float = 0.0
        for item in self.items:
            cart_total += item.subtotal()
        return cart_total

    def display(self) -> None:
        """
        Affiche le contenu du panier et son montant total.
        """
        for item in self.items:
            print(
                f"{item.product.name} : "
                f"{item.quantity} x {item.product.price:.2f} € "
                f"= {item.subtotal():.2f} € "
            )
        # :.2f permet d'avoir un affichage avec 2 décimales
        print(f"Total : {self.total():.2f} €")
