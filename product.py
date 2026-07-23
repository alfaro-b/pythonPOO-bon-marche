class Product:
    """
    Représente un produit avec son nom, son stock, l'unité de mesure et son prix
    """
    # ---------------------variables---------------------
    name: str = ""
    price: float = 0.0
    stock: float = 0.0
    unity: str = ""

    # ---------------------Methods---------------------
    """
    Enlève une quantité du stock
    @:param: stock : le stock du produit
    @:param: quantity : la quantité du produit à enlever
    """
    def remove_from_stock(self, quantity) -> None:
        self.stock -= quantity

    """
    Ajoute une quantité au stock
    @:param: stock : le stock du produit
    @:param: quantity : la quantité du produit à ajouter
    """

    def add_to_stock(self, stock, quantity):
        return stock + quantity
    """
    Indique si le produit est toujours disponible
    """

    def is_available(self):
        return self.stock > 0

    # -------------------Constructor--------------------
    """
    Constructeur avec tous les paramètres
    """

    def __init__(self, name, price, stock, unity):
        self.name = name
        self.price = price
        self.stock = stock
        self.unity = unity
