class Product:
    name: str = ""
    price: float = 0.0
    stock: float = 0.0
    unity: float = 0.0

    # ---------------------Methods---------------------
    def remove_from_stock(self, stock, unity):
        self.stock = stock - unity
        return self.stock

    # -------------------Constructor--------------------


def __init__(self, name, price, stock, unity):
    self.name = name
    self.price = price
    self.stock = stock
    self.unity = unity
