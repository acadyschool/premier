import db
from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import datetime

app = Flask(__name__)

# Liste des joueurs
app.secret_key = b'd2b01c987b6f7f0d5896aae06c4f318c9772d6651abff24aec19297cdf5eb199'

def tache():
  with db.connect() as conn:
      with conn.cursor() as cur:
          cur.execute("SELECT * FROM bassin")
          liste_bassin = cur.fetchall()
          cur.execute("SELECT * FROM employer")
          liste_employer = cur.fetchall()
          cur.execute("SELECT * FROM activite")
          liste_activite = cur.fetchall()
          return liste_activite,liste_employer,liste_bassin 


@app.route("/premier_page")
def accueil():
  return render_template("premier_page.html")

# connection d'un employer sur son login 
@app.route("/connexion")
def login():
  if "pseudo" in session:
    return redirect(url_for("welcome"))
  return render_template("connexion.html")


@app.route("/verification", methods = ['POST'])
def connect():
    with db.connect() as conn:
        with conn.cursor() as cur:
            pseudo = request.form.get("prenom",None)
            mdp = request.form.get("mdp",None)
            print("pseudo : " , pseudo , "mot de passe :" , mdp)
            if pseudo is not None and mdp is not None:
                cur.execute("SELECT * FROM employer WHERE prenom_employer = %s AND num_securite_social = %s",(pseudo,mdp,))
                info = cur.fetchone()
                if info is not None:  
                    session["pseudo"] = pseudo
                    print("introuvable")
                    return redirect(url_for("welcome"))

            return redirect(url_for("login"))
  
@app.route("/accueil")


def welcome():

  with db.connect() as conn:
      with conn.cursor() as cur:

        if "pseudo" in session:  
          pseudo = session["pseudo"]
          cur.execute("SELECT * FROM employer WHERE prenom_employer = %s",(pseudo,))
          infor = cur.fetchone()
          cur.execute("SELECT * FROM employer WHERE prenom_employer = %s",(pseudo,))
          infor = cur.fetchone()
          
          cur.execute("SELECT date_naissance FROM employer  WHERE prenom_employer = %s",(pseudo,)) 
          date = cur.fetchone()
          print(date)
          cur.execute("SELECT * FROM role_responsable WHERE num_securite_social = %s",(infor.num_securite_social,))
          responsable = cur.fetchone()
          activites ,employes,bassins = tache()
          if not responsable:
            cur.execute("SELECT * FROM role_gestionnaire WHERE num_securite_social = %s",(infor.num_securite_social,))
            gestionnaire = cur.fetchone()
          else:
            return render_template("accueil_responsable.html",prenom = pseudo,nom = infor.nom_employer,addresse = infor.adresse ,date_n =date.date_naissance.strftime("%Y-%m-%d"),stat = "responsable", activite = activites , bassin = bassins , employer = employes)
 
          if not gestionnaire:
            
            
            return render_template("accueil.html",prenom = pseudo,nom = infor.nom_employer,addresse = infor.adresse , date_n =date.date_naissance.strftime("%Y-%m-%d") , stat = "Employer" , activite = activites , bassin = bassins , employer = employes)
          else:
            cur.execute("SELECT * FROM stock")
            liste_stock = cur.fetchall()
            return render_template("accueil_gestionnaire.html",liste = liste_stock,prenom = pseudo,nom = infor.nom_employer,addresse = infor.adresse , date_n=date.date_naissance.strftime("%Y-%m-%d"),stat = "Gestionnaire",activite = activites , bassin = bassins , employer = employes )
          
        return redirect(url_for("login"))
      


@app.route("/deconnexion")

def deconnexion():
  if "pseudo" in session:
    session.pop("pseudo")
  return redirect(url_for("login"))

# # formulaire d'un visiteur souhaitant prendre un rendez-vous


@app.route("/renseignement")
def form():
  with db.connect() as conn:
        with conn.cursor() as cur:
          cur.execute("SELECT id_activite,horaire FROM activite ")
          acts = cur.fetchall()
          return render_template("renseignement.html" , activite = acts)

# Récupération des données du formulaire POST
@app.route("/traiter_demande", methods = ['GET','POST'])

def traitement_formulaire():

    with db.connect() as conn:
        with conn.cursor() as cur:
            
            nom = request.form.get("nom",None)
            prenom = request.form.get("prenom",None)
            identifiant = request.form.get("HEURE",None)
      
            if not nom or not prenom or not identifiant :
                cur.execute("SELECT id_activite,horaire FROM activite ")
                acts = cur.fetchall()
                return render_template("renseignement.html" , activite = acts)
            
            if identifiant is not None:
              cur.execute("SELECT * FROM activite WHERE id_activite = %s",(identifiant,))
              act = cur.fetchone()
              if act is not None:
                  return render_template("rendez_vous.html", bool = True , valeur = act)  
            
    return render_template("rendez_vous.html",bool = False , valeur = "")  

          
              

                

# # Les responsables ajoute une activite 

@app.route("/role_responsable")
def org():
  with db.connect() as conn:
    with conn.cursor() as cur:
      cur.execute("SELECT * FROM activite")
      act = cur.fetchall()
    return render_template("role_responsable.html",activite = act)

@app.route("/post-organisation_responsable", methods = ['POST','GET'])

def organisation_responsable():

    with db.connect() as conn:
        with conn.cursor() as cur:
            jour = request.form.get("date_time",None)
            open = request.form.get("oui") or request.form.get("Non")
            type_activite = request.form.get("Activité",None)
            horaire = request.form["HEURE"]
            chiffre = random.randint(50,10000)
            identifiant = f"act_{str(chiffre)}"
            if not open :
                return redirect(url_for("org"))
          
            date = f'{jour} {horaire}'
            cur.execute("insert into activite(id_activite,jour,horaire,ouverture,type_activite) values (%s,%s,%s,%s,%s)", (identifiant,jour,date,open,type_activite,))
            cur.execute("SELECT * FROM activite")
            liste = cur.fetchall()
            return render_template("role_responsable.html", activite = liste )

# # supprime une activite
@app.route("/role_responsable_supp")

def supp():
  with db.connect() as conn:
      with conn.cursor() as cur:
        cur.execute("SELECT * FROM activite")
        activite = cur.fetchall()
      return render_template("role_responsable_supp.html",activite = activite )

@app.route("/post-organisation_responsable_supp", methods = ['POST','GET'])

def organisation_responsable_supp():

    with db.connect() as conn:
        with conn.cursor() as cur:
          identifiant = request.form.get("identifiant",None)
          print(identifiant)
          if not identifiant:
            return redirect(url_for("supp"))
          cur.execute("DELETE FROM activite WHERE id_activite = %s",(identifiant,))
          cur.execute("SELECT * FROM activite")
          act = cur.fetchall()
          print('liste',act)
          return  render_template("role_responsable_supp.html",activite = act)

@app.route("/information")
def information():

    with db.connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM bassin")
            liste_bassin = cur.fetchall()
            cur.execute("SELECT * FROM employer")
            liste_employer = cur.fetchall()
            cur.execute("SELECT * FROM activite")
            liste_activite = cur.fetchall()
            return render_template("information.html",activite=liste_activite,employer = liste_employer,bassin = liste_bassin )


@app.route("/animal")
def animaux():
  return render_template("animal.html")



if __name__=='__main__':
    app.run(debug = True , port = 5001)
