"""
Script donnees.py pour créer la base de données et la relier au dataset XML.

Author : Lucas Terriel
Date: 10/04/2020

"""


from app.app import db
from copy import deepcopy
from ..constantes import source_doc

# On créé une class pour l'unique table SongBB qui hérite de db.Model
# et on définit sa structure pour permettre le mapping par l'ORM SQLAlchemy


class SongsBB(db.Model):
    __tablename__ = "chansonBB"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title_fr = db.Column(db.String(45))
    title_brz = db.Column(db.String(45))
    dialect = db.Column(db.String(64))
    theme = db.Column(db.String(64))
    song_fr = db.Column(db.Text)
    song_brz = db.Column(db.Text)
    MusicSheetPath = db.Column(db.String(64))

    def __init__(self, id, title_fr, title_brz, dialect, theme, song_fr, song_brz, MusicSheetPath):
        self.id = id
        self.title_fr = title_fr
        self.title_brz = title_brz
        self.dialect = dialect
        self.theme = theme
        self.song_fr = song_fr
        self.song_brz = song_brz
        self.MusicSheetPath = MusicSheetPath

# Création des listes vides pour stocker par la suite les
# contenus des noeuds récupérés par le xpath

list_song_fr = []
list_song_brz = []
list_title_fr = []
list_title_brz = []
list_dialect = []
list_theme = []
list_lyricsFr = []
list_lyricsBrz = []

# Une exception : le choix a été fait, sûrement discutable, de remplir
# les chemins vers les images à la main. Cependant, on pourra par la suite
# selon l'accroissement du corpus (dataset XML) intégrer les chemins vers les
# images directement dans le dataset XML

list_MusicSheetPath = ['<img src="/static/images/img_partitions/chansonPR.jpg">',
                       '<img src="/static/images/img_partitions/chansonMA.jpg">',
                       '<img src="/static/images/img_partitions/chansonLR.jpg">',
                       '<img src="/static/images/img_partitions/chansonSG.jpg">',
                       '<img src="/static/images/img_partitions/partitionV.jpg">',
                       '<img src="/static/images/img_partitions/partitionV.jpg">',
                       '<img src="/static/images/img_partitions/partitionV.jpg">',
                       '<img src="/static/images/img_partitions/partitionV.jpg">',
                       '<img src="/static/images/img_partitions/chansonEnfer.jpg">',
                       '<img src="/static/images/img_partitions/chansonParadis.jpg">']


def extraction_lyrics(list_song, list_lyrics):
    """ fonction extraction_lyrics permet de récupérer
    l'ensemble des paroles pour une chanson.

        :param list_song: liste qui stocke les éléments du noeud
        recherché par le xpath
        :type attributeContent: list
        :param list_lyrics: liste intérmédiaire pour stocker les
        éléments de list_song
        :type xpathElement: list
        :return: paroles de la chanson
        :rtype : list
        """
    for song in list_song:
        list_lyrics.append(song)
        for verse in list_lyrics:
            verses = verse
    return verses


# La boucle for itère sur le numéro des chansons issu du xpath (@n)
# qui est équivalent à liste = list(range(1,11)) (actuellement on compte
# 10 chansons dans le corpus).
# L'avantage d'itérer sur le xpath est de pouvoir modifier
# le datasetXML, sans avoir a toucher au script de donnees, c'est-à-dire
# d'éviter d'avoir a gérer les flux de la fonction range().
# Chaque node vient récupérer la partie du dataset XML qui l'intéresse
# selon la variable element qui varie selon la position du @n.

for element in source_doc.xpath("//body/div/div/div[@type='chanson']/@n"):
    node_titre_fr = source_doc.xpath("//text/body/div/div/div[@type='chanson'][@n=" + str(
        element) + "]/div[@type='transcription']/head[@type='titre-français']/text()")
    list_title_fr.append(deepcopy(node_titre_fr[0]))
    node_titre_brz = source_doc.xpath("//div/div/div[@type='chanson'][@n=" + str(
        element) + "]/div[@type='original']/head[@type='titre-breton']/text()")
    list_title_brz.append(deepcopy(node_titre_brz[0]))
    node_dialecte = source_doc.xpath(
        "//body/div/div/div[@type='chanson'][@n=" + str(element) + "]/ancestor::div[@type='D']/head/text()")
    list_dialect.append(deepcopy(node_dialecte[0]))
    node_theme = source_doc.xpath(
        "//body/div/div/div[@type='chanson'][@n=" + str(element) + "]/ancestor::div[@type='T']/head/text()")
    list_theme.append(deepcopy(node_theme[0]))
    node_chanson_fr = source_doc.xpath(
        "//div[@type='chanson'][@n='" + str(element) + "']/div[@type = 'transcription']/lg/l/text()")
    list_song_fr.append(deepcopy(node_chanson_fr))
    node_chanson_brz = source_doc.xpath(
        "//div[@type='chanson'][@n='" + str(element) + "']/div[@type = 'original']/lg/l/text()")
    list_song_brz.append(deepcopy(node_chanson_brz))
    list_verses_fr = extraction_lyrics(list_song_fr, list_lyricsFr)
    list_verses_brz = extraction_lyrics(list_song_brz, list_lyricsBrz)

    # Pour éviter de créer la table à chaque nouveau démarage du serveur :

    db.drop_all()
    db.create_all()

    # la méthode add() permet d'ajouter des items, ici les contenus du
    # XML selon la position de la variable element, l'index d'une liste commençant
    # à O, il est impératif de soustraire 1 à l'index pour ne pas décaler les données dans la table.
    # la méthode .join() permet de caster une liste en string et de ne pas récupérer seulement
    # le première élément de la liste, c'est pour cela qu'on évite la récupération
    # du contenu de la liste par la méthode de l'index.

    db.session.add(
        SongsBB(
            element,
            list_title_fr[int(element) - 1],
            list_title_brz[int(element) - 1],
            list_dialect[int(element) - 1],
            list_theme[int(element) - 1],
            "".join(list_verses_fr),
            "".join(list_verses_brz),
            list_MusicSheetPath[int(element) - 1]
        )
    )

# Enfin on indique à l'ORM via la méthode .commit()
# de faire les requêtes nécéssaires pour finaliser les
# opérations d'ajouts dans la table.

db.session.commit()
