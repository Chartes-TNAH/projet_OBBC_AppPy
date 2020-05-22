"""

Script pour permettre la création d'un document XML TEI valide
pour récupérer une chanson du dataset Barzaz-Breiz.xml

Author : Lucas Terriel
Date: 10/04/2020

"""

# Import du package lxml et du module etree renommé ET

from lxml import etree as ET

# Import du module deepcopy afin de conserver
# le noeud dans la mémoire du parent (l.162)

from copy import deepcopy

# Import de la source XML (dataset) qui contient l'emsemble des chansons

from .constantes import source_doc


def layoutDivP(attributeContent, xpathElement, parent):

    """ Routine de la fonction chansonXmlTei() pour
    construire une sous-arborescence avec des éléments <div>.

    :param attributeContent: contenu de @type de <div>
    :type attributeContent: str
    :param xpathElement: variable qui stocke le résultat
    d'une partie du contenu d'un document XML par rapport à un motif XPATH
    :type xpathElement: list
    :param parent: élément du nouvel
    arbre XML sous lequel
    on contruit la nouvel arborescence
    :type parent: noeud XML
    :return: sous-arborescence d'un document XML
    :rtype : XML
    """

    # création d'un sous-élément <div> contenu dans un élément parent à définir
    # suivant l'arborescence que l'on souhaite obtenir

    div = ET.SubElement(parent, 'div')

    # création d'un @type sur l'élement <div> créé

    div.set('type', attributeContent)

    # liste vide intermédiaire pour récupérer les élements
    # de la liste de la variable xpathElement

    list = []

    # première itération pour récupérer les élements  correpondants
    # au xpath de la liste issue de la méthode findall()

    for x in xpathElement:

        # création d'un sous-élément <p> contenu dans <div>

        paragraph = ET.SubElement(div, 'p')

        # on ajoute à la liste intermédiaire les
        # éléments cotenus dans la liste générée par .findall()

        list.append(x.text)

        # seconde itération afin de placer les éléments de la
        # liste intermédiaire dans l'élément <p> grâce à l'attribut .text

        for y in list:
            paragraph.text = y



def Song2XmlTei(chanson_id):
    """ Fonction principale qui permet de générer
    dynamiquement un modèle XML, TEI compatible,
    avec le contenu spécifique d'une chanson extrait d'un dataset XML initial
    grâce à son id (chanson_id).

    :param chanson_id: identifiant de la chanson
    :type chanson_id: int
    :return: document XML-TEI de la chanson
    :rtype: XML-TEI
    """

    # Création des variables qui stockent les
    # contenus spécifiques du dataset(source_doc) grâce
    # à la méthode .findall() qui contient un motif XPATH à
    # l'intérieur duquel on opère une concaténation
    # du paramètre de la fonction (chanson_id) qui
    # correspond à l'id  de la chanson

    # Le teiHeader_content récupère le teiHeader
    # du dataset dans son entier pour l'injecter
    # dans le nouveau document XML

    nodeTeiHeader = source_doc.findall('teiHeader')

    titles = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/head")

    arguments = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'argument']/*")

    transcriptions = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'transcription']/lg/*")

    originals = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'original']/lg/*")

    Ne = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'Ne']/*")

    #  Création de l'élément racine TEI et du conteneur XML-TEI

    #  --- (Rappel :)

    #  Méthodes du module etree (lxml) :

    # .Element('nom_de_l'élément') : créer un élément

    # .set('nom_de_l'attribut', 'contenu_de_l'attribut') :
    # ajout d'un attribut à un élément ou à un sous-élément
    # .comment : ajout de commentaire
    # .insert : insertion du commentaire ou
    # d'une partie du dataset suivant une position
    # .SubElement(élement_parent, 'nom_sous-élement') :
    # création d'un sous-élément
    # .text(''): contenu de l'élément ou
    # du sous-élement que l'on souhaite ajouter

    TEI = ET.Element('TEI')

    TEI.set('xmlns',
            'http://www.tei-c.org/ns/1.0')

    warning_comments = ET.Comment("INSTRUCTIONS : 1) Copier-coller le code dans un éditeur XML **" \
        "2) Rajouter les schémas RelaxNG TEI ALL " \
        "pour obtenir un document valide  **" \
        "3) Supprimer ce commentaire **")

    TEI.insert(1, warning_comments)

    # TeiHeader

    for elements in nodeTeiHeader:
        TEI.append(deepcopy(elements))

    # Text

    text = ET.SubElement(TEI, "text")

    # Body

    body = ET.SubElement(text, 'body')

    divGeneral = ET.SubElement(body, 'div')

    divGeneral.set('type', 'chanson')

    # Titre

    head = ET.SubElement(divGeneral, 'head')
    for title in titles:
        head.text = title.text

    # Appelle de la sous-fonction de traitement layoutDivP()

    # div Argument

    layoutDivP('argument', arguments, divGeneral)

    # div transcription

    layoutDivP('transcription', transcriptions, divGeneral)

    # div original

    layoutDivP('original', originals, divGeneral)

    # div Notes et éclaircissements

    layoutDivP('notes_et_éclaircissements', Ne, divGeneral)

    # methode .tostring() du module etree qui permet de décoder
    # une byte string en chaine de caractère unicode et
    # de produire un document xml lisible

    Song2TEI = ET.tostring(TEI,
                                encoding="UTF-8",
                                method="xml",
                                pretty_print=True,
                                xml_declaration=True,
                                standalone=True)

    return Song2TEI
