"""

Script constantes.py pour la fonction chansonXmlTei()
et la sous-fonction layoutDivP().

Author : Lucas Terriel
Date: 31/03/2020

"""



from lxml import etree as ET

# Import de la source XML (dataset) qui contient l'emsemble des chansons

from .constantes import source_doc


def layoutDivP(attributeContent, xpathElement, parent):

    """ Routine de la fonction chansonXmlTei() pour
    construire une sous-arborescence en <div> avec
    un @type (attributeContent) et un <p> à l'intérieur
    d'un élément parent (parent) du nouveau
    document XML afin de placer des contenus spécifiques (xpathElement)
    extraits du dataset XML initial.

    :param attributeContent: contenu de @type de <div>
    :type attributeContent: str
    :param xpathElement: variable qui stocke le résultat
    d'une partie du contenu d'un document XML par rapport à un motif XPATH
    :type xpathElement: list
    :param parent: élément du nouvel
    arbre XML sous lequel
    on contruit la nouvel arborescence
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

        paragraphe = ET.SubElement(div, 'p')

        # on ajoute à la liste intermédiaire les
        # éléments cotenus dans la liste générée par .findall()

        list.append(x.text)

        # seconde itération afin de placer les éléments de la
        # liste intermédiaire dans l'élément <p> grâce à .text

        for y in list:
            paragraphe.text = y


def chansonXmlTei(chanson_id):
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

    titres = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/head")

    arguments = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'argument']/*")

    transcriptions = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'transcription']/lg/*")

    originaux = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'original']/lg/*")

    Ne = source_doc.findall(
        "//div[@type='chanson'][@n='" + str(chanson_id) +
        "']/div[@type = 'Ne']/*")

    #  Création de l'élément racine TEI et du conteneur XML-TEI

    #  Méthodes du module etree (lxml) :

    # .Element('nom_de_l'élément') : créer un élément

    # .set('nom_de_l'attribut', 'contenu_de_l'attribut') :
    # ajout d'un attribut à un élément ou à un sous-élément
    # .comment : ajout de commentaire
    # .insert : insertion du commentaire suivant une position
    # .SubElement(élement_parent, 'nom_sous-élement') :
    # création d'un sous-élément
    # .text(''): contenu de l'élément ou
    # du sous-élement que l'on souhaite ajouter

    TEI = ET.Element('TEI')

    TEI.set('xmlns',
            'http://www.tei-c.org/ns/1.0')

    comment = ET.Comment(
        "Rajouter les schémas RNG TEI ALL pour obtenir un document valide")

    TEI.insert(1, comment)

    # TeiHeader

    teiHeader = ET.SubElement(TEI, 'teiHeader')

    avertissementOBBC = ET.SubElement(
        teiHeader, "p")

    avertissementOBBC.text = \
        "!!!!!!!!!=============CLIC DROIT DANS LE NAVIGATEUR POUR " \
        "AFFICHER LE CODE SOURCE ET RECUPERER " \
        "LE FICHIER EN XML/TEI==============" \
        "!!!!!!!!"

    # fileDesc

    fileDesc = ET.SubElement(teiHeader, 'fileDesc')

    # titleStmt

    titleStmt = ET.SubElement(fileDesc, 'titleStmt')

    title = ET.SubElement(titleStmt, "title")

    title.text = "Barzaz Breiz, chants populaires de la Bretagne"

    title2 = ET.SubElement(titleStmt, "title")

    title2.text = "recueillis et publiés avec une " \
                  "traduction française, des éclaircissements, " \
                  "des notes et les mélodies originales par " \
                  "Th. de La Villemarqué"

    author = ET.SubElement(titleStmt, "author")

    forename = ET.SubElement(author, "forename")

    forename.text = "Théodore"

    surname = ET.SubElement(author, "surname")

    surname.text = "Hersart de La Villemarqué"

    # publicationStmt

    publicationStmt = ET.SubElement(fileDesc, 'publicationStmt')

    publisher = ET.SubElement(publicationStmt, "publisher")

    forename1 = ET.SubElement(publisher, "forename")

    forename1.text = "Albert"

    surname1 = ET.SubElement(publisher, "surname")

    surname1.text = "Franck"

    pubPlace = ET.SubElement(publicationStmt, "pubPlace")

    address = ET.SubElement(pubPlace, "address")

    addrLine = ET.SubElement(address, "addrLine")

    addrLine.text = "69, rue de Richelieu Paris"

    date = ET.SubElement(publicationStmt, "date")

    date.set("when-iso", "1846")

    date.text = "1846"

    distributor = ET.SubElement(publicationStmt, "distributor")

    distributor.set("facs", "https://fr.wikisource.org/wiki/Barzaz_Breiz/1846")

    distributor.text = "Wikisource"

    availability = ET.SubElement(publicationStmt, "availability")

    licence = ET.SubElement(availability, "licence")

    licence.set("target",
                "https://creativecommons.org/licenses/by-sa/3.0/deed.fr")

    licence.text = "Licence Creative Commons Attribution-" \
                   "partage dans les mêmes conditions"

    # sourceDesc

    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")

    pSD = ET.SubElement(sourceDesc, "p")

    pSD.text = "Ici informations supplémentaire " \
               "sur la source à voir apparaître"

    # Text

    text = ET.SubElement(TEI, "text")

    # Body

    body = ET.SubElement(text, 'body')

    divGenerale = ET.SubElement(body, 'div')

    divGenerale.set('type', 'chanson')

    # Titre

    head = ET.SubElement(divGenerale, 'head')
    for titre in titres:
        head.text = titre.text

    # Appelle de la sous-fonction de traitement layoutDivP()

    # div Argument

    layoutDivP('argument', arguments, divGenerale)

    # div transcription

    layoutDivP('transcription', transcriptions, divGenerale)

    # div original

    layoutDivP('original', originaux, divGenerale)

    # div Notes et éclaircissements

    layoutDivP('notes_et_éclaircissements', Ne, divGenerale)

    # methode .tostring() du module etree qui permet de décoder
    # une byte string en chaine de caractère unicode et
    # de produire un document xml lisible

    XmlTeiChanson = ET.tostring(TEI,
                                encoding="UTF-8",
                                method="xml",
                                pretty_print=True,
                                xml_declaration=True,
                                standalone=True)

    return XmlTeiChanson
