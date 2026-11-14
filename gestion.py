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

choix = input("Veuillez entrer votre choix (1-5) : ")
while true:
    if choix == 1:
        nom = input("Entrez le nom du staff : ")
        prenom = input("Entrez le prénom du staff : ")
        age = input("Entrez l'âge du staff : ")
        staff = {"nom": nom, "prenom": prenom, "age": age}
        stafflist.append(staff)
        with open(Savefile, "w") as f:
            json.dump(stafflist, f)
        print("Le staff a été ajouté avec succès !")
    elif choix == 2:
        nom = input("Entrez le nom du staff à supprimer : ")
        for staff in stafflist:
            if staff["nom"] == nom:
                stafflist.remove(staff)
                with open(Savefile, "w") as f:
                    json.dump(stafflist, f)
                print("Le staff a été supprimé avec succès !")
                break
        else:
            print("Le staff n'a pas été trouvé.")
    elif choix == 3:
        print("Liste des staff :")
        for staff in stafflist:
            print(f"{staff['nom']} {staff['prenom']}, {staff['age']} ans")
    elif choix == 4:
        nom = input("Entrez le nom du staff à sélectionner : ")
        for staff in stafflist:
            if staff["nom"] == nom:
                print(f"Staff sélectionné : {staff['nom']} {staff['prenom']}, {staff['age']} ans")
                break
        else:
            print("Le staff n'a pas été trouvé.")
    elif choix == 5:
        print("Au revoir !")
    break
