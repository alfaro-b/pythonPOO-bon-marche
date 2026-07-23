from cart import Cart


class Customer:

    """
    représente un client.
    """

    # --------------------------Methods---------------------

    """
    Obtenir le nom complet du client.
    :return : la nom complet du client.
    """
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    # ------------------------Constructor-------------------

    """
    Constructeur avec tous les paramètres.
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.cart = Cart()
