"""
script de test : tests pour les redirections
sur OBBC

Author : Lucas Terriel
Date : 22/05/2020
"""

# Import du package de tests

import unittest

# Import de l'application comme module

from app.app import app


class TestMainRoads(unittest.TestCase):
    """ Classe de tests de redirection
    """
    def setUp(self):
        """ Initialisation des attributs de classe
        pour le test
        """
        self.app = app.test_client()
        self.liste = list(range(1, 5))
    print("Initialisation des tests ...\n")

    def testMainRoads(self):
        """Tests divers de retour code HTTP
        """
        m1 = self.app.get('/')
        m2 = self.app.get('/themes')
        m3 = self.app.get('/nav_carte_dialectes')
        m4 = self.app.get('/sommaire')
        m5 = self.app.get('/galerie')
        m6 = self.app.get('/a_propos')
        m7 = self.app.get('/bibliographie')
        m8 = self.app.get('/contact')
        m9 = self.app.get('/CGU')
        assert m1.status == '200 OK', 'm1 failed'
        assert m2.status == '200 OK', 'm2 failed'
        assert m3.status == '200 OK', 'm3 failed'
        assert m4.status == '200 OK', 'm4 failed'
        assert m5.status == '200 OK', 'm5 failed'
        assert m6.status == '200 OK', 'm6 failed'
        assert m7.status == '200 OK', 'm7 failed'
        assert m8.status == '200 OK', 'm8 failed'
        assert m9.status == '200 OK', 'm9 failed'
        print("... Test des routes principales OK !\n")

    def testError404(self):
        """ Test retour code HTTP == 404
        """
        error404 = self.app.get('/blabla')
        self.assertEqual(error404.status, '404 NOT FOUND', 'error404 failed')
    print("... Test de l'erreur 404 Ok !\n")

    def testAdd(self):
        """ Tests de redirections par variation de l'id du XML TEI
        """
        print("Test pour les redirections ...")

        # 1 <= id <= 4 : correspond aux thèmes et aux dialectes qui reste au nombre de 4

        for id in self.liste:
            page_theme = self.app.get(f'/themes/{str(id)}')
            page_dialecte = self.app.get(f'/nav_carte_dialectes/{str(id)}')
            print(f'page themes : {id} => OK ! ')
            print(f'page dialectes : {id} => OK ! ')
            assert page_theme.status == '200 OK', 'themes failed'
            assert page_dialecte.status == '200 OK', 'dialectes failed'

            # On teste les cas où l'index est en-dehors de la liste (out of range)

            theme = self.app.get('/themes/5')
            self.assertEqual(theme.status, '404 NOT FOUND', 'error404 failed')
            dialecte = self.app.get('/nav_carte_dialectes/5')
            self.assertEqual(dialecte.status, '404 NOT FOUND', 'error404 failed')
            theme = self.app.get('/themes/0')
            self.assertEqual(theme.status, '404 NOT FOUND', 'error404 failed')
            dialecte = self.app.get('/nav_carte_dialectes/0')
            self.assertEqual(dialecte.status, '404 NOT FOUND', 'error404 failed')

        print("... Test redirection OK!\n")


if __name__ == '__main__':
    unittest.main ()
