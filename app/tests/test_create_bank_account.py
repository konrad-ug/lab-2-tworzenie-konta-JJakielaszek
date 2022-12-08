import unittest

from ..Konto import Konto, KontoFirmowe

class TestCreateBankAccount(unittest.TestCase):
    imie = "name1"
    nazwisko = "surname1"
    pesel_correct = "20017801637"
    pesel_long = "200146396363268"
    pesel_short = "199736"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel_correct)
        drugie_konto = Konto(self.imie, self.nazwisko, self.pesel_short)
        trzecie_konto = Konto(self.imie, self.nazwisko, self.pesel_long)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel_correct, "Pesel nie zosta przypisany")
        self.assertEqual(pierwsze_konto.saldo, 0, "Poczatkowe saldo nie jest zerowe!")
        self.assertEqual(len(pierwsze_konto.historia), 0, "Niepoprawna poczatkowa historia transferow")
        self.assertEqual(drugie_konto.pesel, "Niepoprawny pesel!", "Za krutki pesel")
        self.assertEqual(trzecie_konto.pesel, "Niepoprawny pesel!", "Za dlugi pesel")

class TestCreateAccountPromotionalCode(unittest.TestCase):
    imie = "name1"
    nazwisko = "surname1"
    pesel_correct_age = "20017801637"
    pesel_wrong_age = "19507392022"
    pesel_long = "200146396363268"
    pesel_short = "195036"

    def test_kod_promocyjny(self):
        czwarte_konto = Konto(self.imie, self.nazwisko, self.pesel_correct_age, "PROM_111")
        piate_konto = Konto(self.imie, self.nazwisko, self.pesel_correct_age, "promocja")
        szoste_konto = Konto(self.imie, self.nazwisko, self.pesel_correct_age, "PROM_6")
        siodme_konto = Konto(self.imie, self.nazwisko, self.pesel_correct_age, "PROM_7777777")
        osiem_konto = Konto(self.imie, self.nazwisko, self.pesel_wrong_age, "PROM_111")
        dziewiec_konto = Konto(self.imie, self.nazwisko, self.pesel_long, "PROM_111")
        dziesiate_konto = Konto(self.imie, self.nazwisko, self.pesel_short, "PROM_111")
        self.assertEqual(czwarte_konto.saldo, 50, "Kod promocyjny nie dziala")
        self.assertEqual(piate_konto.saldo, 0, "Bledny kod promocyjny dziala (wrong prefix)")
        self.assertEqual(szoste_konto.saldo, 0, "Bledny kod promocyjny dziala (too short code)")
        self.assertEqual(siodme_konto.saldo, 0, "Bledny kod promocyjny dziala (too long code)")
        self.assertEqual(osiem_konto.saldo, 0, "Kod promocyjny dziala dla ludzi przed 1960")
        self.assertEqual(dziewiec_konto.saldo, 0, "Kod promocyjny dziala przy niepoprawnym peselu(too long pesel")
        self.assertEqual(dziesiate_konto.saldo, 0, "Kod promocyjny dziala przy niepoprawnym peselu(too short pesel)")
    


