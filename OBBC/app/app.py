"""
Script app.py pour permettre l'initialisation de l'app flask.

Et de la base de donnée pour OBBC.

Author : Lucas Terriel
Date: 31/03/2020

"""
from flask import Flask

# Import du module Flask depuis le package flask

import os

# Import du module os pour permettre à python de
# reconnaitre l'os sur lequel il se situe

from flask_sqlalchemy import SQLAlchemy

# Import du module SQLAlchemy du package flask_sqlalchemy,
# pour utiliser les fonctions relatives à l'appel de la base
# de données, comme les requêtes

# Déclarations liées au module os :

chemin_actuel = os.path.dirname(os.path.abspath(__file__))

# on stocke le chemin du fichier courant

templates = os.path.join(chemin_actuel, "templates")

# on stocke le chemin vers les templates

statics = os.path.join(chemin_actuel, "static")

# on stocke le chemin vers les pages éléments de "statics"


# Instanciation de l'application, il n'est pas utile
# de donner un nom particulier à l'application,
# mais par soucis de clarté et dans le cadre de dévellopements ultérieurs,
# le choix a été fait de conserver un nom personalisé.

# Ajout des paramètres, liens vers les dossiers déclarés par le module os


app = Flask(
    "OBBC",
    template_folder=templates,
    static_folder=statics
)

# Configuration de la base de données :

# Lien avec la base de données sqlite

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db_BB.sqlite'


app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# On initie l'extension SQLAlchemy à l'application Flask;
# la BDD est stocké dans une variable db

db = SQLAlchemy(app)

# On relie les routes à l'application.
# Elles sont situées à la fin, car il faut d'abord déclarer
# la variable app pour que l'import des routes
# soit opérationnel

from .routes import accueil, a_propos, contact, themes, \
    resultatTheme, resultatTheme_affichage, nav_carte_dialectes, \
    resultatDialectes, resultatDialectes_affichage, CGU, sommaire, \
    affichage, chansonXmlTei, page_not_found, affichage_XMLTEI, \
    affichage_XMLTEI2, affichage_XMLTEI3, recherche, galerie