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
            pass
            # à faire

        elif choice == "2":
            store.daily_report()

        elif choice == "3":
            print("Fermeture du magasin.")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
