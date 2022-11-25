import unittest

from ..Konto import Konto
from ..RejestrKont import RejestrKont

class TestAccountsRegistry(unittest.TestCase):
    imie = "name"
    nazwisko = "surname"
    pesel = "11111111111"

    def setUp(self) -> None:
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    def test_1_dodawanie_konta(self):
        RejestrKont.add_account(self.konto)
        self.assertEqual(RejestrKont.how_many(), 1)

    def test_2_dodawanie_kolejnych_kont(self):
        RejestrKont.add_account(self.konto)
        RejestrKont.add_account(self.konto)
        self.assertEqual(RejestrKont.how_many(), 3)

    def test_przeszukiwanie_rejestru_istniejace_konto(self):
        self.assertEqual(RejestrKont.search_account(self.pesel), self.imie+' '+self.nazwisko)

    def test_przeszukiwanie_rejesrtu_nieistniejace_konto(self):
        self.assertEqual(RejestrKont.search_account("0436236753"), None)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.registry = []