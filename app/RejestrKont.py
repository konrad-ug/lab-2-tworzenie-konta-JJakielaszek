from .Konto import Konto

class RejestrKont:
    registry= []

    @classmethod
    def add_account(cls,konto):
        cls.registry.append(konto)
        pass

    @classmethod
    def how_many(cls):
        return len(cls.registry)

    @classmethod
    def search_account(cls, pesel):
        for konto in cls.registry:
            if konto.pesel == pesel:
                return konto
        return None