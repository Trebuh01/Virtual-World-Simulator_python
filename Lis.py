from Zwierze import Zwierze
from Organizm import TypOrganizmu
from Organizm import Kierunek
from Organizm import Organizm
from random import randint
from Punkt import Punkt
class Lis(Zwierze):
    ZASIEG_RUCHU = 1
    SZANSA_WYKONYWANIA_RUCHU = 1
    SILA = 3
    INICJATYWA = 7

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.LIS, swiat, pozycja, turaUrodzenia, self.SILA, self.INICJATYWA)
        self.setZasiegRuchu(self.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(self.SZANSA_WYKONYWANIA_RUCHU)
        self.setKolor("#eb6d13")

    def TypOrganizmuToString(self):
        return "Lis"

    def LosujDowolnePole(self, pozycja):
        self.OdblokujWszystkieKierunki()
        pozX = pozycja.getX()
        pozY = pozycja.getY()
        sizeX = self.getSwiat().getSizeX()
        sizeY = self.getSwiat().getSizeY()
        ileKierunkowMozliwych = 0
        tmpOrganizm = None

        if pozX == 0 or (tmpOrganizm is not None and isinstance(tmpOrganizm,
                                                                Organizm) and tmpOrganizm.getSila() > self.getSila()):
            self.ZablokujKierunek(Kierunek.LEWO)

        else:
            ileKierunkowMozliwych += 1

        if pozX == sizeX - 1 or (tmpOrganizm is not None and tmpOrganizm.getSila() > self.getSila()):
            self.ZablokujKierunek(Kierunek.PRAWO)
        else:
            ileKierunkowMozliwych += 1

        if pozY == 0 or (tmpOrganizm is not None and tmpOrganizm.getSila() > self.getSila()):
            self.ZablokujKierunek(Kierunek.GORA)
        else:
            ileKierunkowMozliwych += 1

        if pozY == sizeY - 1 or (tmpOrganizm is not None and tmpOrganizm.getSila() > self.getSila()):
            self.ZablokujKierunek(Kierunek.DOL)
        else:
            ileKierunkowMozliwych += 1

        if ileKierunkowMozliwych == 0:
            return Punkt(pozX, pozY)

        r = randint(0, ileKierunkowMozliwych - 1)
        for k in Kierunek:
            if not self.CzyKierunekZablokowany(k):
                if r == 0:
                    if k == Kierunek.LEWO:
                        return Punkt(pozX - 1, pozY)
                    elif k == Kierunek.PRAWO:
                        return Punkt(pozX + 1, pozY)
                    elif k == Kierunek.GORA:
                        return Punkt(pozX, pozY - 1)
                    elif k == Kierunek.DOL:
                        return Punkt(pozX, pozY + 1)
                r -= 1