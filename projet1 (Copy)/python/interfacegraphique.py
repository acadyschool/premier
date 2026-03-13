
from fltk import *
from main import *
from copy import *
from menu import *
import time
import random
from fichier import *
from tkinter import *


def grille(coord_x,coord_y):
    """
    Fonction qui affiche la carte de jeu
    param: coord_x: int
    param: coord_y: int

    """
    
    for colonne in range(coord_x+1):
        for ligne in range (coord_y+1):
            rectangle(50+100*ligne, 50+100*colonne,150,150, epaisseur=2,tag='grille')


def affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier):
    """
    Fonction qui affiche les éléments sur le plateau(moutons,herbes,buissons)
    param: plateau: liste de liste
    param: mouton: liste de tuple
    return list
    """
    efface('mouton')
    liste_herbe = []
    for colonne in range(coord_x):
        for ligne in range (coord_y):
            for pos_mouton in moutons:
                if colonne == pos_mouton[0] and ligne == pos_mouton[1]:
                    image(50+100*ligne+10,50+100*colonne+5,'graphique/sheep.png',ancrage='nw',tag='mouton')
            
            if nom_fichier == 'fichier_map/big2.txt' or nom_fichier == 'fichier_map/huge.txt':
                if plateau[colonne][ligne] == 'B':
                    image(50+100*ligne+10,50+100*colonne+5,'graphique/bush.png',ancrage='nw',tag='buisson')
                if plateau[colonne][ligne] == 'G':
                    herbe = ligne , colonne
                    liste_herbe.append(herbe)
                    image(50+100*ligne+10,50+100*colonne+5,'graphique/grass.png',ancrage='nw',tag='herbe')
            else:
                if plateau[ligne][colonne] == 'B':
                    image(50+100*colonne+10,50+100*ligne+5,'graphique/bush.png',ancrage='nw',tag='buisson')
                if plateau[ligne][colonne] == 'G':
                    herbe = ligne , colonne
                    liste_herbe.append(herbe)
                    image(50+100*colonne+10,50+100*ligne+5,'graphique/grass.png',ancrage='nw',tag='herbe')
                
    return liste_herbe

def enleve_moutons(moutons,liste_herbe):
    """ 
    Une fonction qui enlève le mouton sur une touffe d'herbe,
    elle va nous servir pour la fonction affiche_elements_victoire.
    param: moutons : list
    param: liste_herbe : list
    return liste 
    """
    liste_moutons = []
    for (x,y) in moutons:
        if (x,y) not in liste_herbe:
            tmp = (x,y)
            liste_moutons.append(tmp)
    return liste_moutons


def affiche_elements_victoire(plateau,moutons,coord_x,coord_y):
    """
    Pour la victoire, la fonction remplace les images des touffes d'herbes.
    Par un mouton sur une touffe d'herbe.
    param: plateau : list de list
    param: moutons : list
    param: coord_x : int
    param: coord_y : int


    """
    efface('mouton')
    efface('herbe')

    for colonne in range(coord_x):
        for ligne in range (coord_y):
            if moutons != []:
                for pos_mouton in moutons:
                    if colonne == pos_mouton[0] and ligne == pos_mouton[1]:
                        image(50+100*ligne+10,50+100*colonne+5,'graphique/sheep.png',ancrage='nw',tag='mouton')
                    if plateau[ligne][colonne] == 'B':
                        image(50+100*colonne+10,50+100*ligne+5,'graphique/bush.png',ancrage='nw',tag='buisson')
                    if plateau[ligne][colonne] == 'G':
                        image(50+100*colonne+10,50+100*ligne+5,'graphique/sheep_grass.png',ancrage='nw',tag='herbe')
            else:
                if plateau[ligne][colonne] == 'B':
                    image(50+100*colonne+10,50+100*ligne+5,'graphique/bush.png',ancrage='nw',tag='buisson')
                if plateau[ligne][colonne] == 'G':
                    image(50+100*colonne+10,50+100*ligne+5,'graphique/sheep_grass.png',ancrage='nw',tag='herbe')


    mise_a_jour()


def evenement_clavier(x):
    """
    Fonction recevant la direction choisie par le joueur
    param: x : int
    
    return string
    """
    dir = ['Left','Right','Up','Down']
    
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev =='ClicGauche':
            coord_x , coord_y = abscisse(ev), ordonnee(ev)
            if x - 15 <= coord_x <= x + 30 and  10 <=coord_y <= 40:
                return None,-2
        if tev == 'Quitte':
            return False,-1
        if tev == 'Touche' :
            direction = touche(ev)
            if direction in dir:
                return direction,0
            elif direction == 'a' or direction =='A':
                # annuler un coups
                return direction,1
            
            elif direction =='Escape':
                # retourner au menu principal
                return direction,2
            elif direction == 'P' or direction =="p":
                return direction,3
            elif direction == 'S' or direction =="s":
                return direction,4
        if tev == 'Quitte':
            return False,None
        
        
            
        mise_a_jour()
        
        

def affichage_victoire(x,y):
    """
    Un message de félicitations s’affichera et 
    proposera au joueur de revenir au menu.
    param: x : int
    param: y : int

    """
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev =='ClicGauche':
            coord_x , coord_y = abscisse(ev), ordonnee(ev)
            
            if x/2-120 <= coord_x <= x/2 + 120 and y/2 + 30 <=coord_y <= y/2 + 100:
                return False

        efface('couleur')
        choix_couleur = random.choices(couleur)
        texte(x/2-200, y/2 - 150, "Victoire !", couleur=choix_couleur, taille=90,tag = 'couleur')
        rectangle(x/2 - 120 , y/2 + 30, x/2 + 120, y/2 + 100,couleur=choix_couleur,epaisseur= 2, remplissage="gray") 
        texte(x/2 - 100, y/2 + 50, "Revenir au menu ", couleur='black', taille= 20,tag = 'couleur')
        mise_a_jour()


def init_plateau_sauvegarde(plateau):
    """
    La fonction permet de créer un nouveau plateau.
    param: plateau : liste de liste
    return liste de liste
    """
    plateau_jeu = []
    tmp = []
    for i in range(len(plateau)):
        tmp = []
        for j in range(len(plateau[0])):
            tmp.append(plateau[i][j])


        
        plateau_jeu.append(tmp)
    return plateau_jeu 

def annuler(compteur,memoire):
    """
    La fonction permettant au joueur d’annuler le dernier coup qu’il a joué.
    Cette fonction pourra être répétée autant que désiré, 
    jusqu’à revenir à l’état initial.
    param: compteur : int
    param: memoire : list
    return list
    
    """
    return memoire[compteur]


    
    


#_____menu_principal________#
recup_fichier = menu_principal()

if recup_fichier != None and recup_fichier != False :
    plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
    ferme_fenetre()
else :
    if recup_fichier != False and recup_fichier == None :
        recup_fichier = ouvrir_fichier()
        
        ferme_fenetre()
        
        plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
    
#_____taille_de_la_fenetre________#


if recup_fichier == False :
    ferme_fenetre()

if recup_fichier != False :
    x = 100 * len(plateau[0]) + 100 
    y = 100 * len(plateau[0]) + 100 
    coord_x = len(plateau) 
    coord_y = len(plateau[0])
    cree_fenetre(x,y)

    grille(coord_x,coord_y)
    affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
    x_img,y_img = x-50 , 10
    image(x_img,y_img,'graphique/aide.png',ancrage='nw')
    couleur = ['red','purple','orange','green','blue','black','gray']

    #_____Coups_annuler________#
    compteur = 0
    memoire = [] 
    liste_moutons = copy(moutons)
    memoire.append(liste_moutons)
    nouveau_moutons = list(moutons)
    commencement =  True
    solveur_profondeur = True
    liste_direction = None

    if recup_fichier != 'fichier_map/big1.txt' :
        liste_direction = solveur(moutons,plateau,nombre_herbe)

    if __name__ == '__main__' :
        while commencement :
            direction , gestion = evenement_clavier(x_img)
            efface('sauvegarde')



            if gestion == -2 :
            #_____Aide________#
                
                fenetre = Tk()
                fenetre.geometry("175x175")
                
                var = StringVar(fenetre, "1")
                
                
                dico_aide = {"Sauvegarde press S" : "1",
                        "Solveur en Profondeur press P" : "2",
                        "Revenir au menu press Echap": "3",
                        "Annuler un coup press A": "4",
                }
                
            
                for text,value in dico_aide.items():
                    Radiobutton(fenetre, text = text, variable = var,
                                value = value, indicator = 0,
                                background = "light blue").pack()
                
                direction , gestion = evenement_clavier(x_img)
            
                
            if gestion == - 1 :
            #_____Quitter________#
                commencement = False



            if gestion == 0 :
            #_____Utilisateur_qui_joue________#

                jouer(plateau,moutons,direction)
                grille(coord_x,coord_y)
                liste_herbe = affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
                liste_moutons = copy(moutons)
                memoire.append(liste_moutons)
                compteur = compteur + 1 
                annule = compteur
            
                

                
            if gestion == 1 :
            #_____Annuler_un_ou_plusieurs_coups________#
                
                annule = annule - 1
                if annule >= 0 :
                    liste_moutons = annuler(annule,memoire)
                    grille(coord_x,coord_y)
                    liste_herbe = affiche_elements(plateau,liste_moutons,coord_x,coord_y,nom_fichier)
                    moutons = copy(liste_moutons)



            if gestion == 2 :
            #_____Retourner_au_menu________#
                
                ferme_fenetre()
                recup_fichier = menu_principal()
                if recup_fichier == False:
                    commencement = False
                    ferme_fenetre()
                if recup_fichier != None:
                    plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                    ferme_fenetre()
                else:
                    recup_fichier = ouvrir_fichier()
                    
                    ferme_fenetre()
                x = 100 * len(plateau)+100
                y = 100 * len(plateau[0])+100
                coord_x = len(plateau[0])
                coord_y = len(plateau)
                cree_fenetre(x,y)
                grille(coord_x,coord_y)
                affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)

            if liste_direction == None :
                texte(x/3,y-50,'impossible récursive infinie =( ',taille = 12,tag = 'sauvegarde')
                gestion = 0
                
            if gestion == 3 and liste_direction != None :
            #_____Solveur_en_profondeur________#

                print("Le solveur en profondeur :", liste_direction)

                #solveur en profondeur mode graphique
                solveur_profondeur = True
                image(x/2,20,'graphique/solveur.png',ancrage='center',tag='ordinateur')
                
                while solveur_profondeur:
                    for _dir in liste_direction:

                        ev = donne_ev()
                        tev = type_ev(ev)
                        if tev == "Touche":
                            gestion = touche(ev)
 
                        if solveur_profondeur == True and gestion != 'Escape' and tev != "Quitte":       
                            if len(liste_direction) < 15:
                                # Baisse la vitesse lorsque la grille est petite 
                                time.sleep(0.4)
                                jouer(plateau,moutons,_dir)
                                grille(coord_x,coord_y)
                                liste_herbe = affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
                                mise_a_jour()
                            else:
                                mise_a_jour()
                                time.sleep(0.4)
                                jouer(plateau,moutons,_dir)
                                grille(coord_x,coord_y)
                                liste_herbe = affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
                                mise_a_jour()

                            if victoire(plateau,moutons,nombre_herbe):
                                efface('ordinateur')
                                moutons = enleve_moutons(moutons,liste_herbe)
                                affiche_elements_victoire(plateau,moutons,coord_x,coord_y)
                                mise_a_jour()
                                time.sleep(1)
                                efface_tout()
                                affiche_elements_victoire(plateau,moutons,coord_x,coord_y)
                                mise_a_jour()
                                time.sleep(1)
                                efface_tout()
                                tmp = affichage_victoire(x,y)
                                if tmp == False:
                                    ferme_fenetre()
                                    recup_fichier = menu_principal()
                                    if recup_fichier == False:
                                        commencement = False
                                        ferme_fenetre()

                                    if recup_fichier != None:
                                        plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                                        ferme_fenetre()
                                    else:
                                        # sauvegarde 
                                        recup_fichier = ouvrir_fichier()
                                        ferme_fenetre()
                                    plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                                    x = 100 * len(plateau)+100
                                    y = 100 * len(plateau[0])+100
                                    coord_x = len(plateau[0])
                                    coord_y = len(plateau)
                                    solveur_profondeur = False
                                    cree_fenetre(x,y)
                                    image(x_img,y_img,'graphique/aide.png',ancrage='nw')
                                    grille(coord_x,coord_y)
                                    affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
                                liste_direction = solveur(copy(moutons),plateau,nombre_herbe) 
                                
                        if gestion == 'Escape' or tev == "Quitte":
                            # Quitter le solveur en profondeur 
                            solveur_profondeur = False
                            ferme_fenetre()
                            recup_fichier = menu_principal()
                            if recup_fichier == False:
                                commencement = False
                                ferme_fenetre()

                            if recup_fichier != None:
                                plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                                ferme_fenetre()
                            else:
                                # sauvegarde 
                                recup_fichier = ouvrir_fichier()

                                ferme_fenetre()
                            plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                            x = 100 * len(plateau)+100
                            y = 100 * len(plateau[0])+100
                            coord_x = len(plateau[0])
                            coord_y = len(plateau)
                            cree_fenetre(x,y)
                            grille(coord_x,coord_y)
                            image(x_img,y_img,'graphique/aide.png',ancrage='nw')
                            affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
                            direction , gestion = evenement_clavier(x_img)


            if gestion == 4:
                #_____Sauvegarder_un_fichier________#
                
                plateau_jeu = init_plateau_sauvegarde(plateau)
                liste_mout = list(moutons)
                lire_fichier(plateau_jeu,liste_mout)
                texte(x/3,y-50,'sauvegarde réussi ! ',taille = 12,tag = 'sauvegarde')
                gestion = 0

                

            if victoire(plateau,moutons,nombre_herbe) :
                
                moutons = enleve_moutons(moutons,liste_herbe)
                grille(coord_x,coord_y)
                affiche_elements_victoire(plateau,moutons,coord_x,coord_y)
                mise_a_jour()
                efface_tout()
                time.sleep(1)
                efface_tout()
                tmp = affichage_victoire(x,y)
                if tmp == False:
                    # retourne sur le menu 
                    ferme_fenetre()
                    recup_fichier = menu_principal()
                    if recup_fichier == False:
                        commencement = False
                        ferme_fenetre()

                    if recup_fichier != None:
                        plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                        ferme_fenetre()
                    else:
                        # accèder à la sauvegarde 
                        recup_fichier = ouvrir_fichier()
                        ferme_fenetre()
                        plateau,moutons,nombre_herbe,nom_fichier = charger(recup_fichier)
                    
                    x = 100 * len(plateau)+100
                    y = 100 * len(plateau[0])+100
                    coord_x = len(plateau[0])
                    coord_y = len(plateau)
                    cree_fenetre(x,y)
                    image(x_img,y_img,'graphique/aide.png',ancrage='nw')
                    grille(coord_x,coord_y)
                    affiche_elements(plateau,moutons,coord_x,coord_y,nom_fichier)
                    
                        


            
                
        if gestion == -2 : 
            #aide        
            fenetre.mainloop()        
            









