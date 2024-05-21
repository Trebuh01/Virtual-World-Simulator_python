from enum import Enum
from random import randint
from Zwierze import Zwierze
from Komentator import Komentator
import Punkt
from Organizm import TypOrganizmu


class Antylopa(Zwierze):
    ZASIEG_RUCHU = 2
    SZANSA_WYKONYWANIA_RUCHU = 1
    SILA = 4
    INICJATYWA = 4

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.ANTYLOPA, swiat, pozycja, turaUrodzenia, self.SILA, self.INICJATYWA)
        self.setZasiegRuchu(self.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(self.SZANSA_WYKONYWANIA_RUCHU)
        self.kolor = "#008b8b"

    def TypOrganizmuToString(self):
        return "Antylopa"

    def DzialaniePodczasAtaku(self, atakujacy, ofiara):
        tmpLosowanie = randint(0, 99)
        if tmpLosowanie < 50:
            if self == atakujacy:
                Komentator.DodajKomentarz(f"{self.OrganizmToString()} ucieka przed {ofiara.OrganizmToString()}")
                tmpPozycja = self.LosujPoleNiezajete(ofiara.pozycja)
                if tmpPozycja != ofiara.pozycja:
                    self.WykonajRuch(tmpPozycja)
            elif self == ofiara:
                Komentator.DodajKomentarz(f"{self.OrganizmToString()} ucieka przed {atakujacy.OrganizmToString()}")
                tmpPozycja = self.pozycja
                self.WykonajRuch(self.LosujPoleNiezajete(self.pozycja))
                if self.pozycja == tmpPozycja:
                    self.swiat.UsunOrganizm(self)
                    Komentator.DodajKomentarz(f"{atakujacy.OrganizmToString()} zabija {self.OrganizmToString()}")
                atakujacy.WykonajRuch(tmpPozycja)
            return True
        else:
            return False
