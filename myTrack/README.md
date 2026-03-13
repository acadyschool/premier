# Traceur d'allocation


## 2. Description

Le traceur d'allocation, comme son nom l'indique, permet de suivre toutes les allocations et libérations de mémoire dans un programme. Son objectif est de détecter les erreurs liées aux fuites de mémoire et aux problèmes d'allocation, afin d'améliorer la fiabilité et la gestion des ressources.

## 3. Prérequis

<b> Pour utiliser ce projet, vous aurez besoin de :</b>

- Un éditeur de code tel que Visual Studio Code, Geany, ou tout autre éditeur de votre choix.

- Un compilateur C ```gcc```, ```clang```

- Les bibliothèques standard du langage C, notamment :
```stdlib.h```,```stdio.h```,```assert.h```

## 4. Installation

1. Téléchargez le fichier compressé ```MYTRACK.zip```.
2. Décompressez-le dans le répertoire de votre choix.
3. Accédez au dossier en exécutant la commande suivante dans un terminal : ```cd myTrack```

4. Placez le fichier à tester dans le répertoire ```myTrack```.
5. Modifiez la ligne suivante dans le fichier ```Makefile``` :

```bash 
FICHIER_TEST = $(SRC)/main.c
```

Remplacez ```main.c``` par le nom du fichier que vous souhaitez tester.

## 5. Utilisation
Pour utiliser le traceur :

1. Compilez le traceur avec la commande :

```bash
make
```

2. Exécutez le programme avec :
```bash
./main
```
