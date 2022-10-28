import unittest

from matplotlib.pyplot import pie

from ..Konto import Konto, KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto("Dariusz", "Januszewski", "20156925182")
        drugie_konto = Konto("imie2", "nazwisko2", "435675")
        trzecie_konto = Konto("imie3", "nazwisko3", "5326897662364364323")
        czwarte_konto = Konto("imie4", "nazwisko4", "20015378357", "PROM_111")
        piate_konto = Konto("imie5", "nazwisko5", "55550000000", "promocja")
        szoste_konto = Konto("imie6", "nazwisko6", "66660000000", "PROM_6")
        siodme_konto = Konto("imie7", "nazwisko7", "77770000000", "PROM_7777777")
        osiem_konto = Konto("imie8", "nazwisko8", "19505378357", "PROM_111")
        dziewiec_konto = Konto("imie9", "nazwisko9", "2001", "PROM_111")
        self.assertEqual(pierwsze_konto.imie, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "20156925182", "Pesel nie zosta przypisany")
        self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel!", "Za krutki pesel")
        self.assertEqual(trzecie_konto.pesel, "Niepoprawny pesel!", "Za dlugi pesel")
        self.assertEqual(czwarte_konto.saldo, 50, "Kod promocyjny nie dziala")
        self.assertEqual(piate_konto.saldo, 0, "Bledny kod promocyjny dziala (wrong prefix)")
        self.assertEqual(szoste_konto.saldo, 0, "Bledny kod promocyjny dziala (too short")
        self.assertEqual(siodme_konto.saldo, 0, "Bledny kod promocyjny dziala (too long)")
        self.assertEqual(osiem_konto.saldo, 0, "Kod promocyjny dziala dla ludzi przed 1960")
        self.assertEqual(dziewiec_konto.saldo, 0, "Kod promocyjny dziala przy niepoprawnym peselu")
    
class TestCreateTransfer(unittest.TestCase):
    imie = "name1"
    nazwisko = "surname1"
    pesel = "669235964276"

    company_name = "test_name1"
    nip_correct = "1234567890"


    def test_wyslanie_przelewu_wystarczajace_srodki(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 1000
        pierwsze_konto.przelewOut(100)
        self.assertEqual(pierwsze_konto.saldo, 900, "Brak zmiany salda po wyslaniu przelewu")

    def test_wyslanie_przelewu_niewystarczajace_srodki(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 0
        pierwsze_konto.przelewOut(100)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zmiana salda po wyslaniu przelewu (niewystarczajace srodki)")

    def test_otrzymania_przelewu(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 0
        pierwsze_konto.przelewIn(100)
        self.assertEqual(pierwsze_konto.saldo, 100, "Brak zmiany salda po otrzymaniu przelewu")

    def test_firmowe_wyslanie_przelewu_wystarczajace_srodki(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 1000
        company.przelewOut(100)
        self.assertEqual(company.saldo, 900, "Brak zmiany salda (firmowe) po wyslaniu przelewu")

    def test_firmowe_wyslanie_przelewu_niewystarczajace_srodki(self):
        company = Konto(self.imie, self.nazwisko, self.pesel)
        company.saldo = 0
        company.przelewOut(100)
        self.assertEqual(company.saldo, 0, "Zmiana salda (firmowe) po wyslaniu przelewu (niewystarczajace srodki)")

###################### Przelew ekspresowy ###########################

    def test_wyslanie_przelewu_ekspresowego_wystarczajace_srodki(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 1000
        pierwsze_konto.przelewEksOut(100)
        self.assertEqual(pierwsze_konto.saldo, 899, "Brak zmiany salda po wyslaniu przelewu")

    def test_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 0
        pierwsze_konto.przelewEksOut(100)
        self.assertEqual(pierwsze_konto.saldo, 0, "Zmiana salda po wyslaniu przelewu (niewystarczajace srodki)")

    def test_firmowe_wyslanie_przelewu_ekspresowego_wystarczajace_srodki(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 1000
        company.przelewEksOut(100)
        self.assertEqual(company.saldo, 895, "Brak zmiany salda (firmowe) po wyslaniu przelewu")

    def test_firmowe_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki(self):
        company = Konto(self.imie, self.nazwisko, self.pesel)
        company.saldo = 0
        company.przelewEksOut(100)
        self.assertEqual(company.saldo, 0, "Zmiana salda (firmowe) po wyslaniu przelewu (niewystarczajace srodki)")


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
        self.assertEqual(company_long.nip, "Niepoprawny NIP!", "Zapisano niepoprawny NIP (too long)")
        self.assertEqual(company_short.nip, "Niepoprawny NIP!", "Zapisano niepoprawny NIP (too short)")

    #tutaj proszę dodawać nowe testy