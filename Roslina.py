from random import randint
from Organizm import Organizm
import FabrykaOrganizmow
import Punkt
from Komentator import Komentator


class Roslina(Organizm):

    def __init__(self, typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa):
        super().__init__(typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa)
        self.szansaRozmnazania = 0.3

    def Akcja(self):
        tmpLosowanie = randint(0, 99)
        if tmpLosowanie < self.getSzansaRozmnazania() * 100:
            self.Rozprzestrzenianie()

    def CzyJestZwierzeciem(self):
        return False

    def Rozprzestrzenianie(self):
        tmpPunkt = self.LosujPoleNiezajete(self.pozycja)
        if tmpPunkt == self.pozycja:
            return
        else:
            tmpOrganizm = FabrykaOrganizmow.StworzNowyOrganizm(self.typOrganizmu, self.swiat, tmpPunkt)
            Komentator.DodajKomentarz(f"Wzrost nowej rosliny {tmpOrganizm.OrganizmToString()}")
            self.swiat.DodajOrganizm(tmpOrganizm)

    def Kolizja(self, other):
        pass
