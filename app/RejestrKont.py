

class RejestrKont:
    konta = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.konta.append(konto)

    @classmethod
    def wyszukaj_konto(cls, pesel):
        for account in cls.konta:
            if account.pesel == pesel:
                return account
            else:
                return None

    @classmethod
    def ile_kont(cls):
        return len(cls.konta)