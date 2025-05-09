import json
import os

DATA_FILE = "data/user_data.json"

def charger_donnees():
    if not os.path.exists(DATA_FILE):
        return {"rappels": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def sauvegarder_donnees(donnees):
    with open(DATA_FILE, "w") as f:
        json.dump(donnees, f, indent=4)

def ajouter_rappel():
    donnees = charger_donnees()
    titre = input("Titre du rappel (ex: Vidange, pneus...) : ")
    date = input("Date prévue (JJ/MM/AAAA) : ")
    rappel = {"titre": titre, "date": date}
    donnees["rappels"].append(rappel)
    sauvegarder_donnees(donnees)
    print("✅ Rappel ajouté.")

def afficher_rappels():
    donnees = charger_donnees()
    if not donnees["rappels"]:
        print("Aucun rappel enregistré.")
    else:
        print("\n📅 Vos rappels :")
        for i, r in enumerate(donnees["rappels"], 1):
            print(f"{i}. {r['titre']} → {r['date']}")
