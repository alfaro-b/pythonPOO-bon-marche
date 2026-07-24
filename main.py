from product import Product
from store import Store

# -------------------entry point main--------------------------


def main() -> None:
    UNITY_PIECE = "pièces"
    UNITY_KG = "kg"
    products = [
        Product("Clémentine", 2.9, 6, UNITY_KG),
        Product("Datte", 7, 4, UNITY_KG),
        Product("Grenade", 3.5, 3, UNITY_KG),
        Product("Kaki", 4.5, 3, UNITY_KG),
        Product("Kiwi", 3.5, 5, UNITY_KG),
        Product("Mandarine", 2.8, 6, UNITY_KG),
        Product("Orange", 4.5, 3, UNITY_KG),
        Product("Pamplemousse", 2, 8, UNITY_PIECE),
        Product("Poire", 2.5, 5, UNITY_KG),
        Product("Pomme", 1.5, 8, UNITY_KG),
        Product("Carotte", 1.3, 7, UNITY_KG),
        Product("Choux de Bruxelles", 4, 4, UNITY_KG),
        Product("Chou vert", 2.5, 12, UNITY_PIECE),
        Product("Courge butternut", 2.5, 6, UNITY_PIECE),
        Product("Endive", 2.5, 5, UNITY_KG),
        Product("Épinard", 2.6, 4, UNITY_KG),
        Product("Poireau", 1.2, 5, UNITY_KG),
        Product("Potiron", 2.5, 6, UNITY_PIECE),
        Product("Radis noir", 5, 10, UNITY_PIECE),
        Product("Salsifis", 2.5, 3, UNITY_KG)
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
