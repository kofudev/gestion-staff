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
        age = input("Entrez l'âge du staff : ")
        date = input("Entrez la date d'embauche du staff (format : AAAA-MM-JJ) : ")
        role = input("Entrez le rôle du staff : ")
        ojectif = input("Entrez le role visée pare le staff : ")
        motivation = input("Entrez les motivation du staff")
        stafflist.append({"nom": nom, "age": age, "date": date, "role": role, "objectif": ojectif, "motivation": motivation})
        with open(Savefile, "w") as f:
            json.dump(stafflist, f)
        print(f"Le staff {nom} {prenom} a été ajouté avec succès !")
    elif choix == "2":
        nom = input("Entrez le nom du staff à supprimer : ")
        staff_to_remove = {"nom": nom,}
        if staff_to_remove in stafflist:
            stafflist.remove(staff_to_remove)
            with open(Savefile, "w") as f:
                json.dump(stafflist, f)
            print(f"Le staff {nom} {role}a été supprimé avec succès !")
        else:
            print(f"Le staff {nom} {role}n'existe pas dans la liste.")
    elif choix == "3":
        if not stafflist:
            print("La liste des staff est vide.")
        else:
            print("Liste des staff :")
            for staff in stafflist:
                print(f"- {staff['nom']} {staff['role']}")
    elif choix == "4":
        nom = input("Entrez le nom du staff à sélectionner : ")
        staff_to_select = {"nom": nom}
        if staff_to_select in stafflist:
            print(f"Le staff {nom}  a été sélectionné avec succès !")
            print(f"que souhaiter vous faire avec {nom} ")
            print("1. change son nom")
            print("2. changer son role")
            print("3. changer sa date d'adesion")
        else:
            print(f"Le staff {nom} n'existe pas dans la liste.")
    elif choix == "5":
        print("Merci, au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
