# Aquarium Management System

## Description
Ce projet est un site web pour la **gestion d’un aquarium**. Il permet :  
- La gestion des employés et de leurs activités entrantes et sortantes.  
- La réservation de rendez-vous par les visiteurs.  
- L’exposition des bassins et de leurs informations.  

Le site est développé en **Python avec Flask** et utilise **SQL** pour la gestion de la base de données.  
La connexion et la création des tables se font automatiquement via une fonction dédiée.

---

## Technologies utilisées
- **Python 3.x**  
- **Flask** – framework web  
- **SQL** – base de données relationnelle  
- **HTML/CSS** – pages web  
- **JavaScript** – interactivité côté client  



---

## Installation & Lancement
1. Installation & Lancement

1. Créer un environnement virtuel (optionnel mais recommandé) :

```bash
# Sur Windows
python -m venv venv
venv\Scripts\activate

# Sur Mac/Linux
python3 -m venv venv
source venv/bin/activate

2. Lancer l’application Flask :


```bash
python main.py
```
3. Accéder au site depuis le navigateur :

```bash
http://127.0.0.1:5001/premier_page
```

La base de données et toutes les tables nécessaires sont créées automatiquement à l’exécution.

## Fonctionnalités

### Pour les employés

- Connexion et gestion des activités entrantes et sortantes.

- Suivi des tâches et planning.

### Pour les visiteurs

- Consultation des bassins et expositions.

- Réservation de rendez-vous pour visiter l’aquarium.

### Administration

- Visualisation des données des employés et visiteurs.

- Gestion des bassins exposés.


## Structure du projet

```bash
/aquarium
│
├─ /static/          # Images, CSS, JS
│   └─ images/       # Photos des bassins, logos
│
├─ /templates/       # Fichiers HTML
│   ├─ accueil.html
│   ├─ login.html
│   └─ ...
│
├─ /db/              # Base de données (créée automatiquement)
│   └─ aquarium.db   
│
├─ main.py           # Fonctions principales, routes Flask et création automatique de la DB
└─ README.md         # Documentation
```


## Connexion à la base de données

Toutes les interactions avec la base se font via **main.py** grâce à une fonction de connexion qui :

- Crée la base et les tables si elles n’existent pas

- Permet l’ajout, la modification et la suppression des employés et des réservations

- Gère les bassins et expositions

Exemple simplifié de fonction de connexion :

```bash
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('db/aquarium.db')
    conn.row_factory = sqlite3.Row
    # Création automatique des tables si nécessaire
    create_tables(conn)
    return conn
```
## Navigation

- Page d’accueil : ```/premier_page```

- Pages accessibles depuis le menu :

- Gestion employés (connexion)

- Réservations visiteurs (visiteurs)

- Expositions bassins (nos animaux)
