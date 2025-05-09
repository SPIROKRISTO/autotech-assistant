from modules import reminder

def menu():
    while True:
        print("\n=== Assistant Auto-Tech ===")
        print("1. Ajouter un rappel d'entretien")
        print("2. Voir les rappels existants")
        print("3. Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            reminder.ajouter_rappel()
        elif choix == "2":
            reminder.afficher_rappels()
        elif choix == "3":
            print("À bientôt !")
            break
        else:
            print("Choix invalide. Essayez encore.")

if __name__ == "__main__":
    menu()
