# 🐑 Ricosheep - Jeu de réflexion en Python

**Ricosheep** est un jeu de réflexion où vous contrôlez des moutons sur une grille à l’aide du clavier. Le jeu propose une interface graphique, plusieurs niveaux, un système de sauvegarde et un solveur automatique.

---

## 📁 Structure du projet

Ricosheep/ 

    └── brouillon
    / ├── main.py 
    ├── interfacegraphique.py 
    ├── menu.py
    ├── sauvegarde.py 
    └── fltk.py


---

## ▶️ Lancement du jeu

1. Ouvrir le dossier **`Ricosheep/brouillon`**.
2. Assurez-vous que les fichiers suivants sont présents :
   - `main.py`
   - `interfacegraphique.py`
   - `menu.py`
   - `sauvegarde.py`
   - `fltk.py`
3. Ouvrir un terminal dans ce dossier.
4. Lancez le jeu avec la commande suivante :

```bash
python3 interfacegraphique.py
```

## 🎮 Navigation dans les menus

**Play** : Accède au sous-menu de sélection de grille.

**Save** : Charge une sauvegarde précédente.

**Quit** : Ferme le jeu.

Une fois dans le sous-menu, cliquez sur une grille pour la sélectionner.

## 🚀 Démarrer une partie

Cliquez sur le bouton Play depuis le menu principal.

Attendez le chargement.

Choisissez la grille sur laquelle jouer.

Utilisez les touches directionnelles pour déplacer les moutons.

## ⌨️ Commandes clavier
* Touche	Action

* Flèches	Déplacer les moutons\
**s**      &nbsp;&nbsp;&nbsp;&nbsp;      Sauvegarder la partie\
**p**	   &nbsp;&nbsp;&nbsp;&nbsp;     Activer le solveur en profondeur\
**a**	    &nbsp;&nbsp;&nbsp;&nbsp;    Annuler le dernier coup\
**Échap**	  &nbsp;&nbsp;&nbsp;&nbsp;  Revenir au menu principal\