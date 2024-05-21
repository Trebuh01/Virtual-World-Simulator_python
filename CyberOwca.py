from enum import Enum
from random import randint
import Zwierze
import Komentator
from Punkt import Punkt
from zwierzeta.Owca import Owca
from Organizm import TypOrganizmu
class CyberOwca(Owca):
    ZASIEG_RUCHU = 1
    SZANSA_WYKONYWANIA_RUCHU = 1
    SILA_CYBER = 11
    INICJATYWA = 4


    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(swiat, pozycja, turaUrodzenia)
        self.setTypOrganizmu(TypOrganizmu.CYBER_OWCA)
        self.setSila(self.SILA_CYBER)
        self.setInicjatywa(self.INICJATYWA)
        self.setSzansaRozmnazania(0.1)

        self.setZasiegRuchu(self.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(self.SZANSA_WYKONYWANIA_RUCHU)
        self.setKolor("#000000")


    def LosujDowolnePole(self, pozycja):
        if not self.getSwiat().czyIstniejeBarszczSosnowskiego():
            return super().LosujDowolnePole(pozycja)

        cel = self.znajdzNajblizszyBarszczSosnowskiego().getPozycja()
        dx = abs(pozycja.getX() - cel.getX())
        dy = abs(pozycja.getY() - cel.getY())

        if dx >= dy:
            if pozycja.getX() > cel.getX():
                return Punkt(pozycja.getX() - 1, pozycja.getY())
            else:
                return Punkt(pozycja.getX() + 1, pozycja.getY())
        else:
            if pozycja.getY() > cel.getY():
                return Punkt(pozycja.getX(), pozycja.getY() - 1)
            else:
                return Punkt(pozycja.getX(), pozycja.getY() + 1)


    def znajdzNajblizszyBarszczSosnowskiego(self):
        tmpBarszcz = None
        najmniejszaOdleglosc = self.getSwiat().getSizeX() + self.getSwiat().getSizeY() + 1
        for i in range(self.getSwiat().getSizeY()):
            for j in range(self.getSwiat().getSizeX()):
                tmpOrganizm = self.getSwiat().getPlansza()[i][j]
                if tmpOrganizm is not None and tmpOrganizm.getTypOrganizmu() == TypOrganizmu.BARSZCZ_SOSNOWSKIEGO:
                    tmpOdleglosc = self.znajdzOdleglosc(tmpOrganizm.getPozycja())
                    if najmniejszaOdleglosc > tmpOdleglosc:
                        najmniejszaOdleglosc = tmpOdleglosc
                        tmpBarszcz = tmpOrganizm
        return tmpBarszcz


    def znajdzOdleglosc(self, otherPozycja):
        dx = abs(self.getPozycja().getX() - otherPozycja.getX())
        dy = abs(self.getPozycja().getY() - otherPozycja.getY())
        return dx + dy


    def TypOrganizmuToString(self):
        return "Cyber owca"
