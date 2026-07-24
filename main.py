from product import Product
from store import Store

# -------------------entry point main--------------------------


def main() -> None:
    products = [
        Product("Clémentine", 2.90, 6, "kg"),
        Product("Datte", 7, 4, "kg"),
        Product("Grenade", 3.50, 3, "kg"),
        Product("Kaki", 4.50, 3, "kg"),
    ]
    customers = []
    store = Store(products, customers)

    while True:
        print("\n----- Au bon marché -----")
        print("1. Nouveau client")
        print("2. Bilan de la journée")
        print("3. Quitter")

        choice = input("Votre choix : ")

        if choice == "1":
            # Création du client
            first_name = input("Prénom du client : ")
            last_name = input("Nom du client : ")
            customer = store.create_customer(first_name, last_name)

            # Constitution du panier
            add_a_product = "o"
            while add_a_product == "o":
                store.sell_product(customer)
                add_a_product = input("Souhaitez-vous ajouter un nouveau produit? (o/n) ").lower()

            # Affichage du ticket de caisse
            print("\n-----Ticket de caisse-----")
            customer.cart.display()

        elif choice == "2":
            store.daily_report()

        elif choice == "3":
            print("Fermeture du magasin.")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
