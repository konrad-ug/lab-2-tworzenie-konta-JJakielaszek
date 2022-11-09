import unittest

from ..Konto import Konto, KontoFirmowe

class TestCreateTransfer(unittest.TestCase):
    imie = "name1"
    nazwisko = "surname1"
    pesel = "669235964276"

    company_name = "test_name1"
    nip_correct = "1234567890"

##
###################### Przelew standardowy ###########################
##

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

##
###################### Przelew ekspresowy ###########################
##

    def test_wyslanie_przelewu_ekspresowego_wystarczajace_srodki(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 1000
        pierwsze_konto.przelewEksOut(100)
        self.assertEqual(pierwsze_konto.saldo, 899, "Brak zmiany salda po wyslaniu przelewu")

    def test_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 80
        pierwsze_konto.przelewEksOut(100)
        self.assertEqual(pierwsze_konto.saldo, 80, "Zmiana salda po wyslaniu przelewu (niewystarczajace srodki)")

    def test_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki_na_oplate(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        pierwsze_konto.saldo = 100
        pierwsze_konto.przelewEksOut(100)
        self.assertEqual(pierwsze_konto.saldo, -1, "Brak zmiany salda po wyslaniu przelewe (niewystarczajace srodki na oplate)")

    def test_firmowe_wyslanie_przelewu_ekspresowego_wystarczajace_srodki(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 1000
        company.przelewEksOut(100)
        self.assertEqual(company.saldo, 895, "Brak zmiany salda (firmowe) po wyslaniu przelewu")

    def test_firmowe_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 80
        company.przelewEksOut(100)
        self.assertEqual(company.saldo, 80, "Zmiana salda (firmowe) po wyslaniu przelewu (niewystarczajace srodki)")

    def test_firmowe_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki_na_oplate(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 100
        company.przelewEksOut(100)
        self.assertEqual(company.saldo, -5, "Brak zmiany salda (firmowe) po wyslaniu przelewu (niewystarczajace srodki na oplate)")

class TestTransferHistory(unittest.TestCase):
    imie = "name1"
    nazwisko = "surname1"
    pesel = "669235964276"

    company_name = "test_name1"
    nip_correct = "1234567890"

    def test_wyslanie_przelewu_wystarczajace_srodki(self):
        person = Konto(self.imie, self.nazwisko, self.pesel)
        person.saldo = 1000
        person.przelewOut(100)
        length_history = len(person.historia)
        last_transfer = person.historia[-1]
        self.assertEqual(length_history, 1, "Brak wpisu w historii przelewow (przelewOut)")
        self.assertEqual(last_transfer, -100, "Bledna zmiana w historii przelewow (przelewOut)")
    
    def test_wyslanie_przelewu_niewystarczajace_srodki(self):
        person = Konto(self.imie, self.nazwisko, self.pesel)
        person.saldo = 1
        person.przelewOut(100)
        length_history = len(person.historia)
        self.assertEqual(length_history, 0, "Zmiana historii przelewow przy niewystarczajacych srodkach")

    def test_otrzymanie_przelewu(self):
        person = Konto(self.imie, self.nazwisko, self.pesel)
        person.przelewIn(100)
        length_history = len(person.historia)
        last_transfer = person.historia[-1]
        self.assertEqual(length_history, 1, "Brak wpisu w historii przelewow (przelewIn)")
        self.assertEqual(last_transfer, 100, "Bledna zmiana w historii przelewow (przelewIn)")

    def test_serii_przelewow(self):
        person = Konto(self.imie, self.nazwisko, self.pesel)
        person.saldo = 1000
        person.przelewOut(100)
        person.przelewIn(200)
        person.przelewOut(2000)
        person.przelewIn(300)
        length_history = len(person.historia)
        self.assertEqual(length_history, 3, "Bledna ilosc wpisow w historii przelewow")
        self.assertEqual(person.historia[0], -100, "Bledna zmiana w historii przelewow (seria 1")
        self.assertEqual(person.historia[1], 200, "Bledna zmiana w historii przelewow (seria 2")
        self.assertEqual(person.historia[2], 300, "Bledna zmiana w historii przelewow (seria 3")

    def test_wyslanie_przelewu_ekspresowego_wystarczajace_srodki(self):
        person = Konto(self.imie, self.nazwisko, self.pesel)
        person.saldo = 1000
        person.przelewEksOut(100)
        length_history = len(person.historia)
        self.assertEqual(length_history, 2, "Bledna ilosc wpisow w historii przelewow (ekspresowy - wystarczajace srodki)")
        self.assertEqual(person.historia[0], -100, "Bledny zmiana w historii przelewow (kwota)")
        self.assertEqual(person.historia[1], -1, "Bledna zmiana w historii przelewow (oplata)")

    def test_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki(self):
        person= Konto(self.imie, self.nazwisko, self.pesel)
        person.saldo = 80
        person.przelewEksOut(100)
        length_history = len(person.historia)
        self.assertEqual(length_history, 0, "Bledna ilosc wpisow w historii przelewow (ekspresowy - niewystarczajace srodki)")

    def test_firmowe_wyslanie_przelewu_ekspresowego_wystarczajace_srodki(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 1000
        company.przelewEksOut(100)
        length_history = len(company.historia)
        self.assertEqual(length_history, 2, "Bledna ilosc wpisow w historii przelewow (ekspresowy - wystarczajace srodki)")
        self.assertEqual(company.historia[0], -100, "Bledny zmiana w historii przelewow (kwota)")
        self.assertEqual(company.historia[1], -5, "Bledna zmiana w historii przelewow (oplata)")

    def test_firmowe_wyslanie_przelewu_ekspresowego_niewystarczajace_srodki_na_oplate(self):
        company = KontoFirmowe(self.company_name, self.nip_correct)
        company.saldo = 100
        company.przelewEksOut(100)
        length_history = len(company.historia)
        self.assertEqual(length_history, 2, "Bledna ilosc wpisow w historii przelewow (firma - ekspresowy - niewystarczajace srodki na oplate)")
        self.assertEqual(company.historia[0], -100, "Bledny zmiana w historii przelewow (firma- kwota)")
        self.assertEqual(company.historia[1], -5, "Bledna zmiana w historii przelewow (firma - oplata)")