from product import Product


class CartItem:
    """
    Représente une ligne du panier client.
    """

    def __init__(self, product: Product, quantity: float):
        """
        Initialise une ligne du panier client.
        :param product : Produit ajouté au panier client.
        :param quantity : Quantité achetée.
        """
        self.product: Product = product
        self.quantity: float = quantity

    def subtotal(self) -> float:
        """
        Calcule le sous-total d'une ligne du panier.
        :return: Montant total de cette ligne du panier.
        """
        return self.product.price * self.quantity
