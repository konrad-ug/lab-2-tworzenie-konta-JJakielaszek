import unittest

from parameterized import parameterized
from ..Konto import Konto, KontoFirmowe

class TestTakeCreditCompanyAccount(unittest.TestCase):
    company_name = "test_name1"
    nip_correct = "1234567890"

    def setUp(self):
        self.konto_firmowe = KontoFirmowe(self.company_name, self.nip_correct)

    @parameterized.expand([
        #historia, #saldo, #kwota_kredytu #oczekiwany_wynik #oczekiwane_saldo
        ([700, 4000, -1755, 200, 1000], 5000, 500, True, 5500),
        ([700, 4000, -200, 1000, -500], 5000, 500, False, 5000),
        ([], 5000, 500, False, 5000),
        ([700, 4000, -1755, 200, 1000], 1000, 800, False, 1000),
        ([700, 4000, -1755, 200, 1000], 0, 100, False, 0)
    ])

    def test_kredyt_dla_konta_firmowego(self, historia, poczatkowe_saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto_firmowe.historia = historia
        self.konto_firmowe.saldo = poczatkowe_saldo
        credit_result = self.konto_firmowe.zaciagnij_kredyt(kwota)
        self.assertEquals(credit_result, oczekiwany_wynik)
        self.assertEquals(self.konto_firmowe.saldo, oczekiwane_saldo)