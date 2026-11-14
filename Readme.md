# StaffManager

Un gestionnaire de personnel développé en **Python**, permettant de centraliser, consulter et modifier les informations des membres d'une équipe.

## Présentation

StaffManager est un projet personnel réalisé pour apprendre et approfondir les bases de Python à travers une application concrète.

L'objectif est de développer un système de gestion du staff fonctionnant directement dans un terminal, avec une sauvegarde persistante des données au format JSON.

Le programme doit permettre de retrouver les informations enregistrées après chaque redémarrage, sans perdre les membres déjà ajoutés.

## Fonctionnalités prévues

### Gestion des membres
- Ajouter un nouveau membre du staff.
- Afficher la liste complète des membres.
- Consulter les informations d'un membre.
- Modifier les informations existantes.
- Supprimer un membre.
- Empêcher les doublons.

### Informations enregistrées

Chaque membre possède les informations suivantes :

| Information | Description |
|---|---|
| Nom | Pseudonyme du membre |
| Date d'arrivée | Date d'intégration dans l'équipe |
| Rôle actuel | Grade actuellement occupé |
| Rôle souhaité | Grade maximum visé |
| Motivation | Objectifs et motivations du membre |

### Sauvegarde des données
- Enregistrement des données dans `staffs.json`.
- Chargement automatique des données au démarrage.
- Création d'une liste vide lors de la première utilisation.
- Conservation des données entre les sessions.
- Sauvegarde des modifications.

## Technologies

- **Python 3** — Langage principal.
- **JSON** — Stockage des informations.
- **Terminal** — Interface utilisateur.

Le projet utilise uniquement les bibliothèques standard de Python.

## Installation et utilisation

### Prérequis
- Python 3 installé sur l'ordinateur.

### Lancement

Depuis le dossier du projet :

```bash
python main.py
```

*La commande suppose que le fichier principal est nommé `main.py`.*

## Organisation prévue

```text
StaffManager/
├── main.py
├── staffs.json
└── README.md
```

Le fichier JSON pourra être créé automatiquement au premier enregistrement.

## Objectifs pédagogiques

Ce projet permet de pratiquer :

- Variables et types de données.
- Listes et dictionnaires.
- Boucles `for` et `while`.
- Conditions `if`, `elif` et `else`.
- Fonctions et organisation du code.
- Manipulation des fichiers.
- Lecture et écriture JSON.
- Gestion des erreurs.
- Validation des saisies utilisateur.

## Évolutions possibles

- Recherche d'un membre par pseudonyme.
- Calcul automatique de l'ancienneté.
- Historique des changements de grade.
- Gestion des avertissements.
- Statistiques de l'équipe.
- Interface graphique.
- Migration vers une base de données SQLite.

## État du projet

**En développement**

Le projet est réalisé progressivement dans un objectif d'apprentissage. Les fonctionnalités présentées constituent la feuille de route et ne sont pas nécessairement toutes implémentées.

## Licence

Projet personnel à vocation éducative.

<sub>Entièrement développé par Kofu, sans l'aide d'outils externes.</sub>
