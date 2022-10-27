class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_prom=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
        self.saldo = 0
        if kod_prom != None:
            self.setSaldo(kod_prom)

    def setSaldo(self, kod_prom):
        if len(kod_prom) == 8 and kod_prom[0:5] == "PROM_":
            if self.pesel != "Niepoprawny pesel!" and int(self.pesel[0:4]) >= 1960:
                self.saldo += 50