from django.test import TestCase
from .views import es_palindromo

# Create your tests here.
class testPalindromo(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_no_es_palindromo(self):
        self.assertFalse(es_palindromo("abbaa"))

    def test_si_es_palindromo(self):
        self.assertTrue(es_palindromo("abba"))