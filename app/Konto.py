class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_prom=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel if len(pesel) == 11 else "Niepoprawny pesel!"
        self.saldo = 0
        self.historia = []
        if kod_prom != None:
            self.checkPromoCode(kod_prom)
### Kod Promocyjny
    def checkPromoCode(self, kod_prom):
        if len(kod_prom) == 8 and kod_prom[0:5] == "PROM_":
            self.checkPromoAge()

    def checkPromoAge(self):
        if self.pesel != "Niepoprawny pesel!" and int(self.pesel[0:4]) >= 1960:
                self.saldo += 50
### Przelewy
    def przelewIn(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def przelewOut(self, kwota):
        if (self.saldo >= kwota):
            self.saldo -= kwota
            self.historia.append(-kwota)
    
    def przelewEksOut(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= (kwota + 1)
            self.historia.append(-kwota)
            self.historia.append(-1)
### Kredyt
    def checkLastSum(self, amount, kwota):
        if (sum(self.historia[-amount:]) > kwota):
            return True
        else:
            return False

    def checkLastTransaction(self, amount):
        if (min(self.historia[-amount:]) > 0):
            return True
        else:
            return False

    def creditIsValid(self, kwota):
        if (len(self.historia) >= 5):
            if (self.checkLastTransaction(3) and self.checkLastSum(5, kwota)):
                return True
            else:
                return False
        else:
            return False

    def zaciagnij_kredyt(self, kwota):
        if (self.creditIsValid(kwota)):
            self.saldo += kwota
            return True
        else:
            return False

class KontoFirmowe(Konto):
    def __init__(self, company_name, nip):
        self.company_name = company_name
        self.nip = nip if len(nip) == 10 else "Niepoprawny NIP!"
        self.saldo = 0
        self.historia = []
        
    def przelewEksOut(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= (kwota + 5)
            self.historia.append(-kwota)
            self.historia.append(-5)

    def checkAccountSaldo(self, kwota):
        if (self.saldo >= kwota * 2):
            return True
        else:
            return False

    def paymentZUS(self):
        for transfer in self.historia:
            if transfer == -1755:
                return True
        return False 
    
    def creditIsValid(self, kwota):
        if (self.checkAccountSaldo(kwota) and self.paymentZUS()):
            return True
        else:
            return False

    def zaciagnij_kredyt(self, kwota):
        if (self.creditIsValid(kwota)):
            self.saldo += kwota
            return True
        else:
            return False