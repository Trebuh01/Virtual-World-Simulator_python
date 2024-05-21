from random import randint
from Roslina import Roslina
from enum import Enum
from Komentator import Komentator
import random
import Punkt
import Swiat
from Organizm import TypOrganizmu
class WilczeJagody(Roslina):
    SILA = 99
    INICJATYWA = 0

    def __init__(self, swiat, pozycja: Punkt, tura_urodzenia: int):
        super().__init__(TypOrganizmu.WILCZE_JAGODY, swiat, pozycja, tura_urodzenia, self.SILA, self.INICJATYWA)
        self.setKolor("#8b0000")
        self.setSzansaRozmnazania(0.05)

    def Akcja(self):
        tmp_losowanie = randint(0, 99)
        if tmp_losowanie < self.szansaRozmnazania * 100:
            self.Rozprzestrzenianie()

    def TypOrganizmuToString(self):
        return "Wilcze jagody"

    def DzialaniePodczasAtaku(self, atakujacy, ofiara):
        Komentator.DodajKomentarz(atakujacy.OrganizmToString() + " zjada " + self.TypOrganizmuToString())
        if atakujacy.sila >= self.SILA:
            self.swiat.UsunOrganizm(self)
            Komentator.DodajKomentarz(atakujacy.OrganizmToString() + " niszczy krzak wilczej jagody")
        if atakujacy.CzyJestZwierzeciem():
            self.swiat.UsunOrganizm(atakujacy)
            Komentator.DodajKomentarz(atakujacy.OrganizmToString() + " zostaje zabity przez wilcze jagody")
        return True