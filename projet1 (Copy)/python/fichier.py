
from fltk import *
from main import *




def ouvrir_fichier():
    """
    ouvre le dossier sauvergarder pour accéder aux fichiers sauvegardés
    return string
    """
    i = 0
    liste = repertoire_sauvegarde()

    if liste == []:
        i = None
    else:
        save = liste[i]
    cree_fenetre(350,350)
    while True:
        ev = donne_ev()
        tev = type_ev(ev)
        if tev == 'Quitte':
            return False
        if i == None:
            texte(130,150,'Pas de sauvegarde ',taille=10)
           
        else:
            if tev =='ClicGauche':
                coord_x , coord_y = abscisse(ev), ordonnee(ev)
                if 130 <= coord_x <= 230 and 190 <=coord_y <= 210:
                    

                    efface('autre_fichier')
                    i = i + 1
                    if i > len(liste)-1:
                        i = 0
                    save = liste[i]
                if 130 <= coord_x <= 230 and 220 <=coord_y <= 240:
                    return "sauvegarder\\"+save

            texte(150,150,save,taille=10,tag = 'autre_fichier')  
            rectangle(130,210,230,190)
            rectangle(130,240,230,220)

            texte(160,192,'choisir',taille=10)
            texte(160,220,'Valider',taille=10)
            image(135,40,'graphique/fichier.png',ancrage='nw',tag='buisson')
            
        mise_a_jour()
        
        
        
        




