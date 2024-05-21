from enum import Enum
from random import randint
from Roslina import Roslina
from Komentator import Komentator
from Punkt import Punkt
from Organizm import Kierunek
from Organizm import TypOrganizmu
from Organizm import Organizm



class BarszczSosnowskiego(Roslina):
    SILA = 10
    INICJATYWA = 0

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.BARSZCZ_SOSNOWSKIEGO, swiat, pozycja, turaUrodzenia, self.SILA, self.INICJATYWA)
        self.kolor = ("#800080")
        self.szansaRozmnazania = 0.05

    def Akcja(self):
        pozX = self.pozycja.x
        pozY = self.pozycja.y
        self.LosujDowolnePole(self.pozycja)  # BLOKUJE GRANICE
        for i in range(4):
            tmpOrganizm = None
            if i == 0 and not self.CzyKierunekZablokowany(Kierunek.DOL):
                tmpOrganizm = self.swiat.CoZnajdujeSieNaPolu(Punkt(pozX, pozY + 1))
            elif i == 1 and not self.CzyKierunekZablokowany(Kierunek.GORA):
                tmpOrganizm = self.swiat.CoZnajdujeSieNaPolu(Punkt(pozX, pozY - 1))
            elif i == 2 and not self.CzyKierunekZablokowany(Kierunek.LEWO):
                tmpOrganizm = self.swiat.CoZnajdujeSieNaPolu(Punkt(pozX - 1, pozY))
            elif i == 3 and not self.CzyKierunekZablokowany(Kierunek.PRAWO):
                tmpOrganizm = self.swiat.CoZnajdujeSieNaPolu(Punkt(pozX + 1, pozY))

            if tmpOrganizm is not None and tmpOrganizm.CzyJestZwierzeciem() and tmpOrganizm.typOrganizmu != TypOrganizmu.CYBER_OWCA:
                self.swiat.UsunOrganizm(tmpOrganizm)
                Komentator.DodajKomentarz(f"{self.OrganizmToString()} zabija {tmpOrganizm.OrganizmToString()}")

        tmpLosowanie = randint(0, 99)
        if tmpLosowanie < self.szansaRozmnazania * 100:
            self.Rozprzestrzenianie()

    def TypOrganizmuToString(self):
        return "Barszcz Sosnowskiego"

    def DzialaniePodczasAtaku(self, atakujacy, ofiara):
        if atakujacy.sila >= 10:
            self.swiat.UsunOrganizm(self)
            Komentator.DodajKomentarz(f"{atakujacy.OrganizmToString()} zjada {self.OrganizmToString()}")
            atakujacy.WykonajRuch(ofiara.pozycja)

        if (atakujacy.CzyJestZwierzeciem() and atakujacy.typOrganizmu != TypOrganizmu.CYBER_OWCA) or atakujacy.sila < 10:
            self.swiat.UsunOrganizm(atakujacy)
            Komentator.DodajKomentarz(f"{self.OrganizmToString()} zabija {atakujacy.OrganizmToString()}")

        return True
