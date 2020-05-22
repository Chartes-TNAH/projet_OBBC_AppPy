"""
script de test : validation
par un schéma RelaxNG de la source XML TEI

schéma de validation : odd-OBBC.rng
source rng : oddbyexample.xsl

Author : Lucas Terriel
Date : 22/05/2020
"""

# Import du package built-in sys pour intéragir avec
# les retours système

import sys

# Bibliothèque standard de test

import unittest

# Modules pour traitement XML, RNG, XSLT

from lxml import etree as ET
from bs4 import BeautifulSoup as bs

# Pour colorer la sortie du terminal

from termcolor import colored


def validator_rng(source_xml, schema_rng):
    """ Linter de validation XMLTEI

    :param source_xml: document xml à valider
    :type source_xml: str
    :param schema_rng: schéma RelaxNG
    :type schema_rng: str
    :returns: logs
    :type returns: str
    """

    # STEP 1 : TEST DE LA SYNTAXE XML PAR LE PARSEUR

    try:
        ET.parse(source_xml)

    except ET.XMLSyntaxError:
        # S'il existe une erreur lxml, on renvoie un message de log, et
        # la cause de cette erreur qui correspond au log du système récupéré
        # le '%' est une autre méthode de formatage des chaines de caractères
        print(colored('Failed to Parse XML source, Error Syntax !\n Error log : %s',
                      'red') % sys.exc_info()[1])
        # En cas d'erreur on quitte alors le programme
        sys.exit()

    # STEP 2 : SI LE PARSAGE OK, ON STOCKE SON CONTENU DANS UNE VARIABLE

    input_xml = ET.parse(source_xml)

    # Récupération du namespace tei dans l'élément racine

    root = input_xml.getroot()

    root.attrib["xmlns"] = "http://www.tei-c.org/ns/1.0"

    # --- (issue :) création d'une soupe Beautifulsoup pour
    # récupérer la déclaration XML

    final = ET.tostring(input_xml, pretty_print=True, xml_declaration=True)

    soup = bs(final, 'xml')

    soup_tei = soup.prettify()

    with open('xml_tei_test.xml', 'w') as file:
        file.write(soup_tei)

    # On parse de nouveau le document xml contenant la déclaration

    input_xml_valid = ET.parse('xml_tei_test.xml')

    # STEP 3 : ON PARSE LE SCHEMA RNG

    relaxng_doc = ET.parse(schema_rng)
    relaxng = ET.RelaxNG(relaxng_doc)

    # STEP 4a : SI LE RESULTAT DU PARSEUR DE LA SOURCE XML PAR LE SCHEMA RENVOIE TRUE, ALORS
    # LE DOCUMENT EST VALIDE

    if relaxng(input_xml_valid):
        validation = 'RNG OK'
        print(colored('Great Job ! Your document is valid !', 'green'))

    # STEP 4b : SI LE RESULTAT DU PARSEUR DE LA SOURCE XML PAR LE SCHEMA RENVOIE FALSE, ALORS
    # LE DOCUMENT EST INVALIDE

    if not relaxng(input_xml_valid):
        print(colored('Sorry, your document is invalid !', 'red'))
        # On stocke le message d'erreur rng
        try:
            relaxng.assertValid(input_xml)
        # On lève le message d'erreur
        except ET.DocumentInvalid:
            print(colored('Error log : %s', 'red') % sys.exc_info()[1])

    return validation


class TestRngValidation(unittest.TestCase):
    """classe pour la validation de la source xml TEI
    """
    def setUp(self):
        """ Initialisation du test"""

        self.xml = './app/data_xml-xslt/Barzaz-Breiz.xml'
        self.rng = './odd-OBBC.rng'

    print("Initialisation des tests RNG...\n")

    def test_rng(self):
        """ On teste le retour du linter RNG"""
        self.assertEqual(validator_rng(self.xml, self.rng), 'RNG OK')


if __name__ == '__main__':
    unittest.main()
