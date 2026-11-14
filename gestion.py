import json
import os

Savefile = "sauvgarde.json"

stafflist = []

if os.path.exists(Savefile):
    print("Le fichier existe déjà. Chargement des données...")
    with open(Savefile, "r") as f:
        stafflist = json.load(f)
else:
    os.create(Savefile)
