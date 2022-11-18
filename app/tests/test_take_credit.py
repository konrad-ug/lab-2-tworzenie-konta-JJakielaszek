import unittest
from parameterized import parameterized

from ..Konto import Konto, KontoFirmowe

class TestTakeCreditKonto(unittest.TestCase):
    imie = "name1"
    nazwisko = "surname1"
    pesel = "669235964276"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([
        ([], 500, False, 0),
        ([-100, 100, 100, 600], 500, False, 0),
        ([-100, -100, 1000, 1000, 1000], 500, True, 500),
        ([-100, -100, 1000, -100, 1000], 500, False, 0),
        ([-1000, -1000, 100, 100, 100], 500, False, 0)
    ])

    def test_kredyt_dla_konta(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        credit_result = self.konto.zaciagnij_kredyt(kwota)
        self.assertEquals(credit_result, oczekiwany_wynik)
        self.assertEquals(self.konto.saldo, oczekiwane_saldo)
