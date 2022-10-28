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

    def przelewIn(self, kwota):
        self.saldo += kwota

    def przelewOut(self, kwota):
        if (self.saldo >= kwota):
            self.saldo -= kwota
    
    def przelewEksOut(self, kwota):
        if (self.saldo + 1) >= kwota:
            self.saldo -= (kwota + 1)

class KontoFirmowe(Konto):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if len(nip) == 10 else "Niepoprawny NIP!"
        self.saldo = 0
        
    def przelewEksOut(self, kwota):
        if (self.saldo + 5) >= kwota:
            self.saldo -= (kwota + 5)