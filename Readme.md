# StaffManager

StaffManager est un outil de gestion d'équipe développé en **Python**, permettant de centraliser, organiser et suivre les informations des membres d'un staff depuis une interface en terminal.

Le projet a été réalisé à des fins éducatives et peut être librement étudié ou reproduit comme exercice de programmation.

## Fonctionnalités

- Ajouter de nouveaux membres.
- Consulter la liste des membres enregistrés.
- Modifier ou supprimer un membre.
- Consulter les informations individuelles.
- Éviter les doublons.
- Sauvegarder les données de manière persistante.
- Retrouver les membres enregistrés après chaque redémarrage.

## Informations des membres

Chaque membre peut disposer des informations suivantes :

| Information | Description |
|---|---|
| Nom | Pseudonyme du membre |
| Date d'arrivée | Date d'intégration dans l'équipe |
| Rôle actuel | Fonction actuellement occupée |
| Rôle souhaité | Fonction ou grade visé |
| Motivation | Motivations et objectifs personnels |

## Technologies utilisées

- **Python 3** — Développement de l'application.
- **JSON** — Stockage et récupération des données.
- **CLI** — Interface en ligne de commande.

Aucune dépendance externe n'est nécessaire.

## Installation

### Prérequis

Python 3 doit être installé sur votre ordinateur.

### Exécution

Clonez le dépôt :

```bash
git clone https://github.com/kofudev/gestion-staff.git
```

Accédez au dossier du projet :

```bash
cd gestion-staff
```

Lancez l'application :

```bash
python gestion.py
```

*Attention : cette commande correspond à mon dépôt GitHub. Si vous créez votre propre dépôt pour héberger ou reproduire ce projet, vous devrez adapter l'URL en remplaçant `VOTRE_PSEUDO_GITHUB` par votre identifiant GitHub.*

```bash
git clone https://github.com/VOTRE_PSEUDO_GITHUB/gestion-staff.git
```

## Stockage des données

Les informations sont enregistrées localement dans un fichier `sauvgarde.json`.

Le système est conçu pour conserver les membres entre les différentes sessions et permettre l'ajout de nouveaux membres sans écraser les données existantes.

## Utilisation et reproduction

StaffManager peut être utilisé comme outil de gestion d'une petite équipe ou comme support éducatif pour découvrir les principes fondamentaux de Python.

Les personnes souhaitant apprendre la programmation peuvent également essayer de reproduire son fonctionnement, de développer leur propre version ou d'y intégrer de nouvelles fonctionnalités.

Le projet est fourni à des fins éducatives. Aucune garantie particulière n'est apportée concernant son utilisation.

## Évolutions envisagées

- Recherche et filtrage des membres.
- Calcul automatique de l'ancienneté.
- Historique des promotions.
- Statistiques de l'équipe.
- Interface graphique.
- Stockage avec SQLite.

---

<sub>Développé par **Kofu** — Code réalisé sans assistance d'outils externes. Projet à vocation éducative.</sub>
Kofu
KOFUDEV
