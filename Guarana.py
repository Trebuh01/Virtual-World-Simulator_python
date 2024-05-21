from enum import Enum
from random import randint
from Roslina import Roslina
from Komentator import Komentator
from Organizm import TypOrganizmu
from Organizm import Organizm

class Guarana(Roslina):
    ZWIEKSZENIE_SILY = 3
    SILA = 0
    INICJATYWA = 0
    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.GUARANA, swiat, pozycja, turaUrodzenia, self.SILA, self.INICJATYWA)
        self.kolor = ("#808000")

    def TypOrganizmuToString(self):
        return 'Guarana'

    def DzialaniePodczasAtaku(self, atakujacy, ofiara):
        tmpPozycja = self.pozycja
        self.swiat.UsunOrganizm(self)
        atakujacy.WykonajRuch(tmpPozycja)
        komentarz = atakujacy.OrganizmToString() + ' zjada ' + self.OrganizmToString() + ' i zwieksza swoja sile o ' + str(self.ZWIEKSZENIE_SILY)
        Komentator.DodajKomentarz(komentarz)
        atakujacy.setSila(atakujacy.getSila() + self.ZWIEKSZENIE_SILY)
        return True
