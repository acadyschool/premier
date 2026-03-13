
from main import *
from fltk import *
import time


fichier = ['fichier_map/map1.txt','fichier_map/map2.txt','fichier_map/map3.txt','fichier_map/big1.txt','fichier_map/big2.txt','fichier_map/big3.txt','fichier_map/onegrass.txt','fichier_map/one_sheep.txt','fichier_map/one_sheep2.txt','fichier_map/huge.txt'] 
x , y = 800 , 500
y_save = 150 
color = 'gray'
chargement = ['chargement en cours .','chargement en cours ..','chargement en cours ...']
save = True




def menu_principal():
    """
    La gestion du menu principal 
    et du sous-menu 
    return string
    ou 
    return booléan 

    """
    cree_fenetre(x,y)
    compteur = 0
    Appel_sousmenu = True
    i = 0
    while True:
        ev = donne_ev()
        tev = type_ev(ev)

        if tev =='ClicGauche':
            coord_x , coord_y = abscisse(ev), ordonnee(ev)
            
            
            if 330 <= coord_x <= 530 and 240 <=coord_y <= 330:
                #bouton play
                while Appel_sousmenu:
                    ev = donne_ev()
                    tev = type_ev(ev)


                    if tev == 'Quitte':
                        return False
                    if tev =='ClicGauche':
                        coord_x , coord_y = abscisse(ev), ordonnee(ev)
                        

                    if 50 <= coord_x <= 157 and 50 <=coord_y <= 155:
                        return fichier[0]
                    if 289 <= coord_x <= 394 and 50 <=coord_y <= 160:
                        return fichier[1]
                        
                    if 500 <= coord_x <= 610 and 50 <=coord_y <= 160:
                        return fichier[2]
                        

                    if 50 <= coord_x <= 190 and 210 <=coord_y <= 320:
                        return fichier[3]
                        
                    
                    
                    if 500 <= coord_x <= 610 and 200 <=coord_y <= 320:
                        return fichier[5]
                        


                    if 50 <= coord_x <= 170 and 370 <=coord_y <= 480:
                        return fichier[6]
                        
                    if 289 <= coord_x <= 400 and 370 <=coord_y <= 490:
                        return fichier[7]
                        
                    if 500 <= coord_x <= 620 and 370 <=coord_y <= 485:
                        return fichier[8]
                        
                    if compteur < 5:

                        efface_tout()
                        rectangle(0,0,700,500,remplissage='black',couleur= 'black')
                        chargeur = chargement[i]
                        texte(250, 240, chargeur , couleur='white', taille= 16,tag = 'couleur')
                        i = i + 1
                        
                        
                    if i == len(chargement):
                        i = 0
                    compteur = compteur +  1
                    time.sleep(0.4)
                    mise_a_jour()

                    if compteur >= 10:
                        # Sous-menu
                        efface_tout()
                        rectangle(0,0,800,500, remplissage = color,couleur= 'black')
                        texte(300, 10, ' Les maps ' , couleur='white', taille= 16,tag = 'couleur')
                        rectangle(0,40,800,170, remplissage = color,couleur= 'black')
                        image(50,50,"map_moutons/map_1.PNG",ancrage='nw')
                        image(290,50,"map_moutons/map_2.png",ancrage='nw')
                        image(500,50,"map_moutons/map_3.PNG",ancrage='nw')
                        texte(290, 170, ' Les big maps ' , couleur='white', taille= 16,tag = 'couleur')
                        rectangle(0,200,800,327, remplissage = color,couleur= 'black')
                        image(50,210,'map_moutons/map_4.PNG',ancrage='nw')
                        image(500,205,"map_moutons/map_6.PNG",ancrage='nw')
                        texte(220, 330, " Les maps à une touffe d'herbe " , couleur='white', taille= 16,tag = 'couleur')
                        rectangle(0,360,800,500, remplissage = color,couleur= 'gray')
                        image(50,370,"map_moutons/onegrass1.PNG",ancrage='nw')
                        image(290,370,"map_moutons/one_sheep1.PNG",ancrage='nw')
                        image(500,370,"map_moutons/one_sheep_2.PNG",ancrage='nw')



    
                    
            if 330 <= coord_x <= 530 and 330 <=coord_y <= 390 :

                #bouton save
                ferme_fenetre()
                return None
                
                
            if 330 <= coord_x <= 530 and 415 <=coord_y <= 475 :

                # bouton quit

                return False

        if compteur == 0:

            # Présentation du menu principal
            rectangle(0,0,800,500,remplissage=color,couleur= color)
            image(430,150,'graphique/logo_small.png',ancrage='center')
            rectangle(330, 240, 530, 300,couleur= 'black' ,epaisseur= 3 )
            rectangle(330, 390, 530, 330,couleur= 'black' ,epaisseur= 3 )
            rectangle(330, 415, 530, 475,couleur= 'black' ,epaisseur= 3 )

            texte(400, 255, " Play ", couleur='black', taille= 20,tag = 'couleur')
            texte(400, 345, " Save ", couleur='black', taille= 20,tag = 'couleur')
            texte(400, 430, " Quit ", couleur='black', taille= 20,tag = 'couleur')


        if tev == 'Quitte':
            return False
        mise_a_jour()
      

        







         








