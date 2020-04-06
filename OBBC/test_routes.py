from app.app import app

import unittest



class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_main_roads(self):
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
        assert m6.status == '200 OK', 'm7 failed'
        assert m7.status == '200 OK', 'm8 failed'
        assert m8.status == '200 OK', 'm9 failed'
        assert m9.status == '200 OK', 'm10 failed'



    def recherche(self):
        liste = ["mer", "soldats", "fleur", "/"]
        for mot in liste:
            search = self.app.get('/recherche?keyword='+mot)
            assert search.status == '200 OK', 'search failed'

    def resultatTheme(self):
        for i in range(1,5):
            a_themes = self.app.get('/themes/'+str(i))
            self.assertEqual(a_themes.status_code, 200, 'a_themes : 404 error')
        a_themes1 = self.app.get('/themes/1')
        assert b'Chants mythologiques' in a_themes1.data, 'a_themes1 : results failed'
        a_themes2 = self.app.get('/themes/2')
        assert b'Chants historiques' in a_themes2.data, 'a_themes2 : results failed'
        a_themes3 = self.app.get('/themes/3')
        assert b'Chants domestiques' in a_themes3.data, 'a_themes3 : results failed'
        a_themes4 = self.app.get('/themes/4')
        assert b'chants religieux' in a_themes4.data, 'a_themes4 : results failed'


    def test_404(self):
        error404 = self.app.get('/blabla')
        self.assertEqual(error404.status, '404 NOT FOUND', 'error404 failed')


