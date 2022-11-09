import unittest

from ..Konto import Konto, KontoFirmowe

class TestCreateCompanyBankAccount(unittest.TestCase):
    company_name = "test_name1"
    nip_correct = "1234567890"
    nip_long = "123456789123456789"
    nip_short = "1234"

    def test_tworzenie_konta_firmowego(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company_long = KontoFirmowe(self.company_name, self.nip_long)
        company_short = KontoFirmowe(self.company_name, self.nip_short)
        self.assertEqual(company.company_name, self.company_name, "Nazwa firmy nie zostala zapisana")
        self.assertEqual(company.nip, self.nip_correct, "NIP nie zostal zapisany")
        self.assertEqual(company.saldo, 0, "Niepoprawne saldo poczatkowe")
        self.assertEqual(len(company.historia), 0, "Niepoprawna poczatkowa historia transferow")
        self.assertEqual(company_long.nip, "Niepoprawny NIP!", "Zapisano niepoprawny NIP (too long)")
        self.assertEqual(company_short.nip, "Niepoprawny NIP!", "Zapisano niepoprawny NIP (too short)")