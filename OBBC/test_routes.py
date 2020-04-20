import unittest
from app.app import app


class testMainRoads(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.liste = list(range(1,5))
    print("Initialisation des tests ...\n")

    def testMainRoads(self):
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
        error404 = self.app.get('/blabla')
        self.assertEqual(error404.status, '404 NOT FOUND', 'error404 failed')
    print("... Test de l'erreur 404 Ok !\n")

    def testAdd(self):
        print("Test pour les redirections ...")
        for id in self.liste:
            page_theme = self.app.get('/themes/'+str(id))
            page_dialecte = self.app.get('/nav_carte_dialectes/'+str(id))
            print("page themes :", id, "=> OK ! ")
            print("page dialectes :", id, "=> OK ! ")
            assert page_theme.status == '200 OK', 'themes failed'
            assert page_dialecte.status == '200 OK', 'dialectes failed'
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


