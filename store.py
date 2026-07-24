from customer import Customer
from product import Product


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

    def search_product(self, product_name) -> Product | None:
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
        print("\n")
        # enumerate permet de parcourir la liste en récupérant l'indice (à partir de 1) et le produit
        for index, product in enumerate(self.products, start=1):
            print(
                # :.2f permet d'afficher le prix avec 2 décimales
                f"{index}. {product.name} - "
                f"{product.price:.2f} €/{product.unity} - "
                f"Stock : {product.stock} {product.unity}"
            )

    """
    Création d'un nouveau client et ajout dans la liste des clients du magasin.
    :param prénom_client: prénom du client
    :param nom_client : nom du client
    :return: client
    """

    def create_customer(self, customer_first_name, customer_last_name):
        customer = Customer(customer_first_name, customer_last_name)
        self.customers.append(customer)
        return customer

    def sell_product(self, customer: Customer) -> None:
        """
        Vend un produit à un client.
        Affiche les produits, demande le produit et la quantité,
        vérifie la disponibilité du stock, met à jour le stock et
        ajoute le produit au panier client.
        :param customer: Client qui effectue l'achat
        """
        self.display_products()

        product_name = input("\nSaisissez le nom du produit que vous souhaitez acheter? ")
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

    def daily_report(self) -> None:
        """
        Affiche le bilan de la journée :
        affiche la liste des clients avec le montant de leurs achats
        et le stock restant de chaque produit.
        """
        print("----- Clients -----")

        for customer in self.customers:
            print(
                f"- {customer.get_full_name()} : "
                f"{customer.cart.total():.2f} € "
            )

        print("\n----- Stock restant -----")

        for product in self.products:
            print(
                f"- {product.name} : "
                f"{product.stock:.2f} {product.unity} "
            )

    # -------------------Constructor-------------------------
    """
    Constructeur avec tous les paramètres
    """

    def __init__(self, products, customers):
        self.products = products
        self.customers = customers
