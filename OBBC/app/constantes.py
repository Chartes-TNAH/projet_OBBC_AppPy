"""

Définition des différentes variables fixes de l'app OBBC.

Author : Lucas Terriel
Date: 31/03/2020

"""

from lxml import etree as ET

# On utilise lxml pour parser le fichier XML servant de dataset pour
# l'application à partir de la méthode .parse() du module etree
# qui instancie un objet ElementTree de type list.

SOURCE_DOCUMENT = ET.parse("app/data_xml-xslt/Barzaz-Breiz.xml")

# On parse les feuilles XSL

XSL_AFFICHAGE_PARSE = ET.parse(
    "app/data_xml-xslt/Barzaz-Breiz_affichage.xsl")
XSL_THEME_RESULTATS_PARSE = ET.parse(
    "app/data_xml-xslt/BB_resultatsThemes.xsl")
XSL_DIALECTES_RESULTATS_PARSE = ET.parse(
    "app/data_xml-xslt/BB_resultatsDialectes.xsl")

# Instanciation des documents XSL en objet XSLT, pour l'affichage des pages

XSLT_TRANSFORMER_1 = ET.XSLT(XSL_AFFICHAGE_PARSE)
XSLT_TRANSFORMER_2 = ET.XSLT(XSL_THEME_RESULTATS_PARSE)
XSLT_TRANSFORMER_3 = ET.XSLT(XSL_DIALECTES_RESULTATS_PARSE)
