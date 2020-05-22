import unittest
from termcolor import colored
from lxml import etree as ET
from bs4 import BeautifulSoup as bs

import sys

from app.app import app

def validator_rng(source_xml, schema_rng):
    """ a little program to validate a xml source
    with a RelaxNG schema
    :param source_xml: source xml name to validate
    :type source_xml: str
    :param schema_rng: RNG schema for validate
    :type schema_rng: str
    :returns: differents log messages for validation
    :type returns: logs str
    """

    # STEP 1 : TEST SYNTAXE ET PARSAGE DE LA SOURCE XML

    # (Option mettre ceci dans une fonction)




    try:
        ET.parse(source_xml)

    except ET.XMLSyntaxError:
        c = 'Syntax Error'
        # S'il existe une erreur lxml, on renvoie un message de log, et
        # la cause de cette erreur qui correspond au log du système
        print(colored('Failed to Parse XML source, Error Syntax !\n Error log : %s', 'red') % sys.exc_info()[1])
        # En cas d'erreur on quitte le programme
        sys.exit()


    # STEP 2 : SI LE PARSAGE OK, ON STOCKE SON CONTENU DANS UNE VARIABLE

    input_xml = ET.parse(source_xml)

    # On ajoute le namespace

    root = input_xml.getroot()

    root.attrib["xmlns"]="http://www.tei-c.org/ns/1.0"

    final = ET.tostring(input_xml, pretty_print=True, xml_declaration=True)




    soup = bs(final, 'xml')

    soup_TEI = soup.prettify()

    with open('test.xml', 'w') as f:
        f.write(soup_TEI)

    input_2 = ET.parse('test.xml')








    # STEP 3 : ON PARSE LE SCHEMA RNG

    relaxng_doc = ET.parse(schema_rng)
    relaxng = ET.RelaxNG(relaxng_doc)

    # STEP 4a : SI LE PARSAGE DE LA SOURCE XML PAR LE RNG RENVOIE TRUE, ALORS
    # LE DOCUMENT EST VALIDE

    if relaxng(input_2):
        validation = 'RNG OK'
        print(colored('Great Job ! Your document is valid !', 'green'))

    # STEP 4b : SI LE PARSAGE DE LA SOURCE XML PAR LE RNG RENVOIE FALSE, ALORS
    # LE DOCUMENT EST INVALIDE

    if not relaxng(input_2):
        print(colored('Sorry, your document is invalid !', 'red'))
        b = 'Bad'
        # On stocke le message d'erreur rng
        try:
            relaxng.assertValid(input_xml)
        # On renvoie le message d'erreur
        except ET.DocumentInvalid:
            print(colored('Error log : %s', 'red') % sys.exc_info()[1])

    return validation





#validator_rng('./app/data_xml-xslt/Barzaz-Breiz.xml', './odd-OBBC.rng')


class testRNGvalidation(unittest.TestCase):
    def setUp(self):
        """ Initialisation du test"""

        self.xml = './app/data_xml-xslt/Barzaz-Breiz.xml'
        self.rng = './odd-OBBC.rng'
    print("Initialisation des tests RNG...\n")

    def testRNG(self):
        self.assertEqual(validator_rng(self.xml, self.rng), 'RNG OK')


if __name__ == '__main__':
    unittest.main()

