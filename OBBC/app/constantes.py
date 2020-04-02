"""

Script constantes.py pour définir les différentes variables fixes de l'app OBBC.

Author : Lucas Terriel
Date: 31/03/2020

"""

from lxml import etree as ET

# Parsage du fichier XML servant de data set pour
# l'application à partir de la méthode .parse() du module etree
# renvoie un objet ElementTree de type list.

source_doc = ET.parse("app/data_xml-xslt/Barzaz-Breiz.xml")

# Parsage des feuilles XSL pour effectuer
# les transformation à partir de .parse() du module etree

xslt_doc_affichage = ET.parse(
    "app/data_xml-xslt/Barzaz-Breiz_affichage.xsl")
xslt_doc_themeResultats = ET.parse(
    "app/data_xml-xslt/BB_resultatsThemes.xsl")
xslt_doc_dialecteResultats = ET.parse(
    "app/data_xml-xslt/BB_resultatsDialectes.xsl")

# Transformation des documents XSL en objet XSLT, pour l'affichage des pages

xslt_transformer_1 = ET.XSLT(xslt_doc_affichage)
xslt_transformer_2 = ET.XSLT(xslt_doc_themeResultats)
xslt_transformer_3 = ET.XSLT(xslt_doc_dialecteResultats)
