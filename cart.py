from product import Product


class Cart:
    """
    Représente le panier d'un client.
    """

    def __init__(self):
        """
        Initialise un panier vide.
        """
        self.items: list[CartItem] = []
        # TODO : créer la classe CartItem et l'importer

    def add_product(self, product: Product, quantity: float):
        """
        Ajoute un produit au panier.
        :param product: Produit à ajouter.
        :param quantity: Quantité souhaitée.
        """
        pass

    def total(self):
        """
        Calcule le montant du panier.
        :return: Montant total du panier.
        """
        cart_total: float = 0.0
        for item in self.items:
            cart_total += item.subtotal()
        return cart_total
