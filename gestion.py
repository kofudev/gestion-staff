import json
import os

Savefile = "sauvgarde.json"

stafflist = []

if os.path.exists(Savefile):
    print("Le fichier existe déjà. Chargement des données...")
    with open(Savefile, "r") as f:
        stafflist = json.load(f)
else:
    with open(Savefile, "w") as f:
        json.dump(stafflist, f)

print("Bienvenue dans le programme de gestion des staff !")
print("1. Ajouter un staff")
print("2. Supprimer un staff")
print("3. Afficher la liste des staff")
print("4. selectionner un staff")
print("5. Quitter le programme")


while True:
    choix = input("Veuillez entrer votre choix (1-5) : ")
    if choix == "1":
        nom = input("Entrez le nom du staff : ")
        prenom = input("Entrez le prénom du staff : ")
        stafflist.append({"nom": nom, "prenom": prenom})
        with open(Savefile, "w") as f:
            json.dump(stafflist, f)
        print(f"Le staff {nom} {prenom} a été ajouté avec succès !")
    elif choix == "2":
        nom = input("Entrez le nom du staff à supprimer : ")
        prenom = input("Entrez le prénom du staff à supprimer : ")
        staff_to_remove = {"nom": nom, "prenom": prenom}
        if staff_to_remove in stafflist:
            stafflist.remove(staff_to_remove)
            with open(Savefile, "w") as f:
                json.dump(stafflist, f)
            print(f"Le staff {nom} {prenom} a été supprimé avec succès !")
        else:
            print(f"Le staff {nom} {prenom} n'existe pas dans la liste.")
