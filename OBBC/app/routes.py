"""
Script routes.py pour définir les différentes routes URL de l'application OBBC.

Author : Lucas Terriel
Date: 31/03/2020

"""

from flask import render_template, request, send_file
from sqlalchemy import or_
from .app import app
from .constantes import source_doc, xslt_transformer_1, \
    xslt_transformer_2, xslt_transformer_3
from .chansonXML import Song2XmlTei
from .modeles.donnees import SongsBB

# Route vers la page d'acceuil


@app.route('/')
def accueil():
    return render_template('pages/accueil.html')


# Route vers la recherche par thèmes


@app.route('/themes')
def themes():
    themes = source_doc.xpath("//body/div[@type]/head")
    return render_template('pages/recherche_par_themes.html', themes=themes)


#  Route vers les résultats par thèmes
#  On donne une condition ici car il n'existe que quatre thèmes dans l'ouvrage


@app.route("/themes/<int:theme_id>")
def resultatTheme(theme_id):
    if (theme_id <= 4 and theme_id != 0):
        output_doc = xslt_transformer_2(source_doc, themeXsl=str(theme_id))
        return render_template('pages/resultats_theme.html',
                           resultattheme=str(output_doc),
                           theme_id=theme_id)
    else:
        return page_not_found(404)


#  Route qui permet d'appeler la fonction affichage après le choix du thème


@app.route("/themes/affichage/<int:chanson_id>")
def resultatTheme_affichage(chanson_id):
        return affichage(chanson_id)



# Route vers la navigation sur la carte intéractive


@app.route('/nav_carte_dialectes')
def nav_carte_dialectes():
    return render_template('pages/nav_carte_dialectes.html')


#  Route vers les resultats dialectes
#  On donne une condition ici car il n'existe que quatre dialectes en Basse-Bretagne

@app.route("/nav_carte_dialectes/<int:dialecte_id>")
def resultatDialectes(dialecte_id):
    if (dialecte_id <= 4 and dialecte_id != 0):
        output_doc = xslt_transformer_3(source_doc, dialecteXsl=str(dialecte_id))
        return render_template('pages/resultats_dialectes.html',
                               resultatDialecte=str(output_doc),
                               dialecte_id=dialecte_id)
    else:
        return page_not_found(404)

#  Route qui permet d'appeler la fonction affichage après le choix du dialecte


@app.route("/nav_carte_dialectes/affichage/<int:dialecte_id>")
def resultatDialectes_affichage(dialecte_id):
    return affichage(dialecte_id)


# Route vers le sommaire


@app.route('/sommaire')
def sommaire():
    titres = source_doc.xpath("//div[@type='chanson']/head")
    numeros = source_doc.xpath("//div[@type='chanson']/@n")
    return render_template("pages/sommaire.html",
                           titres=titres,
                           n=numeros)

# Route vers la page d'affichage des chansons (affichage)


@app.route("/affichage/<int:chanson_id>")
def affichage(chanson_id):
    if(chanson_id != 0):
        output_doc = xslt_transformer_1(source_doc,
                                        numero=str(chanson_id))
        return render_template('pages/affichage.html',
                               chanson=str(output_doc),
                               id=chanson_id,
                               chanson_id=chanson_id)
    else:
        return page_not_found(404)

# Route vers la page de galerie de partitions


@app.route("/galerie")
def galerie():
    IMAGES_PAR_PAGES = 3

    page = request.args.get("page", 1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1

    cheminsImg = SongsBB.query.filter(SongsBB.id).paginate(
        page=page,
        per_page=IMAGES_PAR_PAGES)

    return render_template('pages/Galerie_partitions.html',
                           Images=cheminsImg)

# Routes qui permettent vers l'affichage en XML/TEI


@app.route('/affichage/download/<int:chanson_id>')
def affichage_XMLTEI(chanson_id):
    return Song2XmlTei(chanson_id)



@app.route('/nav_carte_dialectes/affichage/download/<int:chanson_id>')
def affichage_XMLTEI2(chanson_id):
    return Song2XmlTei(chanson_id)



@app.route('/themes/affichage/download/<int:chanson_id>')
def affichage_XMLTEI3(chanson_id):
    return Song2XmlTei(chanson_id)


# Route pour la recherche plein-texte


@app.route('/recherche')
def recherche():

    #  On initialise une variable motclef pour
    #  récupérer une chaîne de caractère

    motclef = request.args.get("keyword", None)

    #  On initialise une liste vide de résultat

    resultats = []

    #  Redit pour le titre de la page

    titre = "Recherche"

    #  Si un motclef est entré alors on stocke dans la
    #  liste resultats les concordances avec une requête SQL :
    #  SELECT * FROM ChansonBB.titre_fr, ChansonBB.titre_brz,
    #  ChansonBB.chanson_fr, ChansonBB.chanson_brz
    #  WHERE motclef LIKE ('%motclef%')
    #  ORDER BY ChansonBB.titre_fr ASC traduite suivant la syntaxe SQLAlchemy

    if motclef:
        resultats = SongsBB.query.filter(
            or_(
                SongsBB.title_fr.like("%{}%".format(motclef)),
                \
                SongsBB.title_brz.like("%{}%".format(motclef)),
                \
                SongsBB.song_fr.like("%{}%".format(motclef)),
                \
                SongsBB.song_brz.like("%{}%".format(motclef)),
            )
        ).order_by(SongsBB.title_fr.asc()).all()

    #  Dans la variable titre concaténation
    #  du motclef avec une chaîne de caractère

    titre = "Résultats pour la recherche '" + motclef + "'"

    return render_template(
        "pages/recherche.html",
        resultats=resultats,
        titre=titre,
        keyword=motclef
    )


# Route vers la page bibliographie


@app.route('/bibliographie')
def bibliographie():
    return render_template('pages/Bibliographie.html')

# Route vers le téléchargement du fichier BibTex
# de la bibliographie


@app.route('/bibliographie/download/BibTex')
def download_bibTex():
    BibTex = 'app/data_files/Bibliographie_OBBC.bib'
    return send_file(BibTex,
                     attachment_filename='Bibliographie_OBBC.bib',
                     as_attachment=True)

# Route vers le téléchargement du fichier XML-TEI
# de la bibliographie


@app.route('/bibliographie/download/BibXml')
def download_bibXml():
    BibXml = 'app/data_files/Bibliographie_OBBC.xml'
    return send_file(BibXml,
                     attachment_filename='Bibliographie_OBBC.xml',
                     as_attachment=True)


# ROUTES DES PAGES ANNEXES


# Route vers la page à propos


@app.route('/a_propos')
def a_propos():
    return render_template('pages/a_propos.html')


# Route vers la page contact

@app.route('/contact')
def contact():
    return render_template('pages/contact.html')

# Route vers les Conditions générales d'utilisation


@app.route('/CGU')
def CGU():
    return render_template('pages/CGU.html')

#  ROUTES PAGES ERREURS

#  .errorhandler() pour retourner une page erreur,
#  si le code de la réponse HTTP renvoyé est 404 (Not Found) ou 500 (Internal Server Error)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500
