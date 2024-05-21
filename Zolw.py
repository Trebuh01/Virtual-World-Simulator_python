from Zwierze import Zwierze
from Organizm import TypOrganizmu
from Komentator import Komentator
class Zolw(Zwierze):
    ZASIEG_RUCHU = 1
    SZANSA_WYKONYWANIA_RUCHU = 0.25
    SILA = 2
    INICJATYWA = 1

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.ZOLW, swiat, pozycja, turaUrodzenia, self.SILA, self.INICJATYWA)
        self.setZasiegRuchu(self.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(self.SZANSA_WYKONYWANIA_RUCHU)
        self.setKolor("#006400")

    def TypOrganizmuToString(self):
        return "Zolw"

    def DzialaniePodczasAtaku(self, atakujacy, ofiara):
        if self == ofiara:
            if atakujacy.getSila() < 5 and atakujacy.CzyJestZwierzeciem():
                Komentator.DodajKomentarz(self.OrganizmToString() + " odpiera atak " + atakujacy.OrganizmToString())
                return True
            else:
                return False
        else:
            if atakujacy.getSila() >= ofiara.getSila():
                return False
            else:
                if ofiara.getSila() < 5 and ofiara.CzyJestZwierzeciem():
                    Komentator.DodajKomentarz(self.OrganizmToString() + " odpiera atak " + ofiara.OrganizmToString())
                    return True
                else:
                    return False