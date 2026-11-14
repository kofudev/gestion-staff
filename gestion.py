from hmac import new
import json
import os
import time

Savefile = "sauvgarde.json"

stafflist = []

if os.path.exists(Savefile):
    print("Le fichier existe déjà. Chargement des données...")
    with open(Savefile, "r") as f:
        stafflist = json.load(f)
else:
    with open(Savefile, "w") as f:
        json.dump(stafflist, f)




while True:
    print("Bienvenue dans le programme de gestion des staff !")
    print("1. Ajouter un staff")
    print("2. Supprimer un staff")
    print("3. Afficher la liste des staff")
    print("4. selectionner un staff")
    print("5. Quitter le programme")
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
        print(f"Le staff {nom} a été ajouté avec succès !")
    elif choix == "2":
        nom = input("Entrez le nom du staff à supprimer : ")
        staff_to_remove = None
        for staff in stafflist:
            if staff["nom"] == nom:
                staff_to_remove = staff
                break
        if staff_to_remove is not None:
            stafflist.remove(staff_to_remove)
            with open(Savefile, "w") as f:
                json.dump(stafflist, f)
            print(f"Le staff {nom} a été supprimé avec succès !")
        else:
            print(f"Le staff {nom} n'existe pas dans la liste.")
    elif choix == "3":
        if not stafflist:
            print("La liste des staff est vide.")
        else:
            print("Liste des staff :")
            for staff in stafflist:
                print(f"- {staff['nom']} {staff['role']} {staff['date']} {staff['objectif']} {staff['motivation']}")
                time.sleep(3)
    elif choix == "4":
        nom = input("Entrez le nom du staff à sélectionner : ")
        staff_to_select = None

        for staff in stafflist:
            if staff["nom"] == nom:
                staff_to_select = staff
                break

        if staff_to_select is not None:
            print(f"Le staff {nom} a été sélectionné avec succès !")
            print(f"Que souhaitez-vous faire avec {nom} ?")
            print("1. Changer son nom")
            print("2. Changer son rôle")
            print("3. Changer sa date d'adhésion")
            print("4. Changer son objectif de rôle")
            print("5. Changer ses motivations")
            print("6. Ne rien faire")

            select = input(f"Choisissez une action pour {nom} : ")

            if select == "1":
                new_nom = input("Entrez le nouveau nom du staff : ")
                staff_to_select["nom"] = new_nom
                with open(Savefile, "w") as f:
                    json.dump(stafflist, f)
                print(f"Le nom du staff {nom} a été changé en {new_nom} avec succès !")

            elif select == "2":
                new_role = input("Entrez le nouveau rôle du staff : ")
                staff_to_select["role"] = new_role
                with open(Savefile, "w") as f:
                    json.dump(stafflist, f)
                print(f"Le rôle du staff {nom} a été changé en {new_role} avec succès !")

            elif select == "3":
                new_date = input("Entrez la nouvelle date d'adhésion du staff (format : AAAA-MM-JJ) : ")
                staff_to_select["date"] = new_date
                with open(Savefile, "w") as f:
                    json.dump(stafflist, f)
                print(f"La date d'adhésion du staff {nom} a été changée en {new_date} avec succès !")

            elif select == "4":
                new_objectif = input("Entrez le nouvel objectif du staff : ")
                staff_to_select["objectif"] = new_objectif
                with open(Savefile, "w") as f:
                    json.dump(stafflist, f)
                print(f"L'objectif du staff {nom} a été changé en {new_objectif} avec succès !")

            elif select == "5":
                new_motivation = input("Entrez les nouvelles motivations du staff : ")
                staff_to_select["motivation"] = new_motivation
                with open(Savefile, "w") as f:
                    json.dump(stafflist, f)
                print(f"Les motivations du staff {nom} ont été changées avec succès !")

            elif select == "6":
                print(f"Aucune modification n'a été effectuée pour le staff {nom}.")

            else:
                print("Choix invalide.")

        else:
            print(f"Le staff {nom} n'existe pas dans la liste.")
    elif choix == "5":
        print("Merci, au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
