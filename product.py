class Product:
    name: str = ""
    price: float = 0.0
    stock: float = 0.0
    unity: str = ""

    # ---------------------Methods---------------------
    def remove_from_stock(self, stock, quantity):
        return stock - quantity

    def add_to_stock(self, stock, quantity):
        return stock + quantity

    def is_available(self):
        return self.stock > 0

    # -------------------Constructor--------------------


def __init__(self, name, price, stock, unity):
    self.name = name
    self.price = price
    self.stock = stock
    self.unity = unity
