import unittest

from ..Konto import Konto

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

    #tutaj proszę dodawać nowe testy