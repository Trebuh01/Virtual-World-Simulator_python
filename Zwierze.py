from abc import ABC, abstractmethod
from typing import List
import random
from Organizm import Organizm
from Komentator import Komentator
import FabrykaOrganizmow
class Zwierze(Organizm):
    def __init__(self, typ_organizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa):
        super().__init__(typ_organizmu, swiat, pozycja, tura_urodzenia, sila, inicjatywa)
        #self.czy_rozmnazal_sie = False
        self.szansa_rozmnazania = 0.5
        self.zasieg_ruchu = 0
        self.szansa_wykonywania_ruchu = 0.0

    def Akcja(self):
        for _ in range(self.zasieg_ruchu):
            przyszla_pozycja = self.ZaplanujRuch()
            if self.swiat.CzyPoleJestZajete(przyszla_pozycja) and self.swiat.CoZnajdujeSieNaPolu(przyszla_pozycja) != self:
                self.Kolizja(self.swiat.CoZnajdujeSieNaPolu(przyszla_pozycja))
                break
            elif self.swiat.CoZnajdujeSieNaPolu(przyszla_pozycja) != self:
                self.WykonajRuch(przyszla_pozycja)

    def Kolizja(self, other):
        if self.getTypOrganizmu() == other.getTypOrganizmu():
            szansa = int(self.szansa_rozmnazania * 100)
            tmp_losowanie = random.randint(0, 99)
            if tmp_losowanie < szansa:
                self.rozmnazanie(other)
        else:
            if other.DzialaniePodczasAtaku(self, other) or self.DzialaniePodczasAtaku(self, other):
                return
            slabszy = other if self.sila >= other.sila else self
            silniejszy = self if self.sila >= other.sila else other
            self.swiat.UsunOrganizm(slabszy)
            silniejszy.WykonajRuch(slabszy.pozycja)
            Komentator.DodajKomentarz(f"{silniejszy.OrganizmToString()} zabija {slabszy.OrganizmToString()}")

    def CzyJestZwierzeciem(self):
        return True

    def ZaplanujRuch(self):
        tmp_losowanie = random.randint(0, 99)
        if tmp_losowanie >= int(self.szansa_wykonywania_ruchu * 100):
            return self.pozycja
        else:
            return self.LosujDowolnePole(self.pozycja)

    def rozmnazanie(self, other):
        if self.getCzyRozmnazalSie or other.getCzyRozmnazalSie:
            return
        tmp1_punkt = self.LosujPoleNiezajete()(self.pozycja)
        if tmp1_punkt == self.pozycja:
            tmp2_punkt = other.LosujPoleNiezajete(other.pozycja)
            if tmp2_punkt == other.pozycja:
                return
            else:
                tmp_organizm = FabrykaOrganizmow.StworzNowyOrganizm()(self.getTypOrganizmu(), self.swiat, tmp2_punkt)
                Komentator.DodajKomentarz(f"Narodziny {tmp_organizm.OrganizmToString()}")
                self.swiat.DodajOrganizm(tmp_organizm)
                self.setCzyRozmnazalSie(True)
                other.setCzyRozmnazalSie(True)
        else:
            tmp_organizm = FabrykaOrganizmow.StworzNowyOrganizm(self.getTypOrganizmu(), self.swiat, tmp1_punkt)
            Komentator.DodajKomentarz(f"Narodziny {tmp_organizm.OrganizmToString()}")
            self.swiat.DodajOrganizm(tmp_organizm)
            self.setCzyRozmnazalSie(True)
            other.setCzyRozmnazalSie(True)

    def getZasiegRuchu(self):
        return self.zasieg_ruchu

    def setZasiegRuchu(self, zasieg_ruchu):
        self.zasieg_ruchu = zasieg_ruchu

    def getSzansaWykonywaniaRuchu(self):
        return self.szansa_wykonywania_ruchu

    def setSzansaWykonywaniaRuchu(self, szansa_wykonywania_ruchu):
        self.szansa_wykonywania_ruchu = szansa_wykonywania_ruchu
