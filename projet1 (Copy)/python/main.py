

from copy import *
from collections import deque
import  os
import random




def lire_fichier(plateau,moutons):
    """
    permet de créer un nouveau fichier 
    dans le répertoire sauvegarder 
    param: plateau : list
    param: moutons : list
    

    """
    compteur = random.randint(1,1000)
    fichier = f'save{compteur}.txt'
    filepath = 'brouillon\sauvegarder\\'+ fichier
    for (x,y) in moutons :
        if plateau[x][y] !='G':
            plateau[x][y] = 'S'
        else :
            plateau[x][y] = 'GS'
       
    with open(filepath, 'a+') as fp:
      
        for colonne in range (len(plateau)) :
            for ligne in range (len(plateau[0])):
                if plateau[colonne][ligne] == None:
                    fp.write("_")
                if plateau[colonne][ligne] == 'S':
                    fp.write("S")
                if plateau[colonne][ligne] == 'B':
                    fp.write("B")
                if plateau[colonne][ligne] == 'G':
                    fp.write("G")
                if plateau[colonne][ligne] == 'GS':
                    fp.write("A")
            fp.write("\n")
    




def repertoire_sauvegarde():
    """
    Récupérer un ou plusieurs fichier dans le répertoire sauvegarder.
    return list 
    """
    liste = []
    dossier =r"C:\Users\Lixy\Desktop\projet_Tatiana_Desravines\brouillon\sauvegarder" 
    for _,_, fnames in os.walk(dossier):
        for fname in fnames:
            nom_fichier = os.path.join(fname)
            liste.append(nom_fichier)
    return liste


def init_plateau(plateau):
    """
    permet de créer un nouveau plateau.
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




def premiere_case_vide(plateau,pos,i):
    ''' Retourne la 1ere case adjacente à 'pos' vide'''

    liste_dir = [(0,1),(0,-1),(1,0),(-1,0)]
    case_vide = (pos[0],pos[1])

    
    case = plateau[pos[0]+liste_dir[i][0]][pos[1]+liste_dir[i][1]]
    if(case == None) or (case == 'G'):
        case_vide = (pos[0]+liste_dir[i][0],pos[1]+liste_dir[i][1])
    return(case_vide)

         

def jouer(plateau,moutons,direction):
    """
    recevant en paramètre l’état du jeu et une direction représentée par la
    chaine 'Left', 'Right', 'Up' ou 'Down'. La fonction ne renvoie rien et met directement à jour
    les positions des moutons dans la liste moutons en respectant les règles du jeu. 
    param: plateau : list
    param: moutons : list de tuple
    param: direction : string
    """
    
    
    plateau_jeu = init_plateau(plateau)
    droite = len(moutons) - 1
    gauche = 0
    bas = len(moutons) - 1
    haut = 0
    memoire = set()
    compteur_droite = moutons[droite][1]
    compteur_gauche = moutons[gauche][1]
    compteur_haut = moutons[haut][0]
    

    if (direction == 'Right') :
        while droite >= 0 :

         
            if compteur_droite == len(plateau[0])-1 :
                x,y = moutons[droite][0] , moutons[droite][1]
                if (x,y) in memoire:
                    moutons[droite] = x , y - 1
                    mout = x , y - 1
                    memoire.add(mout)
                if (x,y) not in memoire:
                    mout = x , y
                    memoire.add(mout)
                    
                plateau_jeu[moutons[droite][0]][moutons[droite][1]] = 'S'
                droite -= 1
                compteur_droite = moutons[droite][1]
            if droite >= 0 and compteur_droite < len(plateau)-1 :  
                moutons[droite] = premiere_case_vide(plateau_jeu,moutons[droite],0)
                compteur_droite += 1
                
    if (direction == 'Left') :

        while gauche <= len(moutons) - 1:    
           
            if  compteur_gauche > 0:  
                moutons[gauche] = premiere_case_vide(plateau_jeu,moutons[gauche],1)
                compteur_gauche -= 1
            else:
                x,y = moutons[gauche][0] , moutons[gauche][1]
                if (x,y) in memoire:
                    moutons[gauche] = x , y + 1
                    mout = x , y + 1
                    memoire.add(mout)
                    
                    
                if (x,y) not in memoire:
                    mout = x , y
                    memoire.add(mout)
                    
                    
                plateau_jeu[moutons[gauche][0]][moutons[gauche][1]] ='S'
                
                
                gauche += 1
                if gauche < len(moutons):
                    compteur_gauche = moutons[gauche][1]

    if (direction == 'Down') :
        
        compteur_bas = moutons[bas][0]

        while bas >= 0:
            
            if compteur_bas == len(plateau[0])-1:
                x,y = moutons[bas][0] , moutons[bas][1]
                if (x,y) in memoire:
                    moutons[bas] = x - 1 , y 
                    mout = x - 1 , y 
                    memoire.add(mout)
                    
                if (x,y) not in memoire:
                    mout = x , y
                    memoire.add(mout)

                plateau_jeu[moutons[bas][0]][moutons[bas][1]] = 'S'
                bas -= 1
                compteur_bas = moutons[bas][0]
            if bas >= 0 and compteur_bas < len(plateau)-1 :  
                moutons[bas] = premiere_case_vide(plateau_jeu,moutons[bas],2)
                compteur_bas += 1
        
    if (direction == 'Up'):

        while haut <= len(moutons) - 1:
           
            if  compteur_haut > 0 :  
                moutons[haut] = premiere_case_vide(plateau_jeu,moutons[haut],3)
                compteur_haut -= 1
            else:
                x,y = moutons[haut][0] , moutons[haut][1]
                if (x,y) in memoire:
                    moutons[haut] = x + 1 , y 
                    mout = x + 1 , y 
                    memoire.add(mout)
                    
                if (x,y) not in memoire:
                    mout = x, y
                    memoire.add(mout)
                plateau_jeu[moutons[haut][0]][moutons[haut][1]] ='S'
                haut += 1
                if haut < len(moutons):
                    compteur_haut = moutons[haut][0]
    return moutons 



def victoire(plateau,moutons,nombre_herbe):
    """
    la victoire sera détectée par une fonction victoire(plateau,
    moutons) renvoyant True si la partie est actuellement gagnée (chaque touffe d’herbe est couverte
    par un mouton) et False sinon.
    param: plateau : list
    param: moutons : list de tuple
    return boolean
    """
    moutons_sur_herbe = []

    for ligne in range(len(plateau)):
        for colonne in range(len(plateau)):
            for mouton_actuel in moutons :
                if ligne == mouton_actuel[0] and colonne == mouton_actuel[1] :
                    if plateau[ligne][colonne] == 'G' :
                        moutons_sur_herbe.append('présent')
    if len(moutons_sur_herbe) == nombre_herbe :
        return True
    return False


def charger(fichier):
    """
    une fonction charger(fichier) recevant en
    paramètre le chemin d’accès d’un fichier et renvoyant les structures de données que vous aurez
    choisies lors de la tâche 1, correctement remplie avec les informations contenues dans le fichier.
    La fonction renverra None si le fichier proposé n’est pas correctement formaté
    param: fichier : string
    return list de list , list , int , string

    """
    plateau = []
    nombre_herbe = 0
    tmp = []
    moutons = []
    file = open(fichier,"r")
    for numero_ligne,ligne in enumerate (file):
        tmp = []
        for numero_colonne, carac in enumerate(ligne):
            if carac == '_':
                tmp.append(None)
            if carac == 'B':
                tmp.append('B')
            if carac == 'G':
                tmp.append('G')
                nombre_herbe += 1
            if carac == 'S':
                tmp.append(None)
                mouton =  numero_ligne, numero_colonne
                moutons.append(mouton)
            if carac == 'A':
                tmp.append('G')
                mouton =  numero_ligne, numero_colonne
                nombre_herbe += 1
                moutons.append(mouton)

                
        plateau.append(tmp)
        
    return plateau,moutons,nombre_herbe,fichier




def solveur(moutons,plateau,nombre_herbe,visite=set()):
    """
    Le rôle du solveur est de déterminer s’il est possible
    de gagner à partir d’un état du jeu donné. En cas de réponse positive, le solveur doit aussi fournir
    une solution à la grille, c’est-à-dire une liste des coups à jouer pour arriver à la victoire.
    param: plateau : list
    param: liste_direction : list
    param: moutons : list de tuple
    param: visite : set 
    """
    
    
    if victoire(plateau,moutons,nombre_herbe) :
        return deque()

    if tuple(moutons) in visite :     
        return None   
                
    visite.add(tuple(moutons))
    
    for dir in ['Left','Right','Up','Down']:
        nouveaux_moutons = list(moutons)
        nouveaux_moutons = sorted(moutons)
        jouer(plateau,nouveaux_moutons,dir)
        
        sol = solveur(nouveaux_moutons,plateau,nombre_herbe,visite)
        

        if sol is not None :
            sol.appendleft(dir)
            return sol
       
    return None

       
        
        




        



















































































































































































































































































































































































































































      



