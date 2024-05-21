import random
from Punkt import Punkt
from enum import Enum


class Kierunek(Enum):
    LEWO = 0
    PRAWO = 1
    GORA = 2
    DOL = 3
    BRAK_KIERUNKU = 4
class TypOrganizmu(Enum):
        CZLOWIEK = 0
        WILK = 1
        OWCA = 2
        LIS = 3
        ZOLW = 4
        ANTYLOPA = 5
        CYBER_OWCA = 6
        TRAWA = 7
        MLECZ = 8
        GUARANA = 9
        WILCZE_JAGODY = 10
        BARSZCZ_SOSNOWSKIEGO = 11
class Organizm:
    def __init__(self, value):
        self.value = value

    def getValue(self):
        return self.value

    LICZBA_ROZNYCH_GATUNKOW = 12
    def __init__(self, typOrganizmu, swiat, pozycja, turaUrodzenia, sila, inicjatywa):
        self.typOrganizmu = typOrganizmu
        self.swiat = swiat
        self.pozycja = pozycja
        self.turaUrodzenia = turaUrodzenia
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.czyUmarl = False
        self.kierunek = [True, True, True, True]
        self.czyRozmnazalSie = False
        self.kolor = None
        self.szansaRozmnazania = 0.0

    def TypOrganizmuToString(self):
        pass

    def Akcja(self):
        pass

    def Kolizja(self, other):
        pass

    def CzyJestZwierzeciem(self):
        pass

    def DzialaniePodczasAtaku(self, atakujacy, ofiara):
        return False

    def OrganizmToString(self):
        return f"{self.TypOrganizmuToString()} x[{self.pozycja.getX()}] y[{self.pozycja.getY()}] sila[{self.sila}]"

    def WykonajRuch(self, przyszlaPozycja):
        x = przyszlaPozycja.getX()
        y = przyszlaPozycja.getY()
        self.swiat.getPlansza()[self.pozycja.getY()][self.pozycja.getX()] = None
        self.swiat.getPlansza()[y][x] = self
        self.pozycja.setX(x)
        self.pozycja.setY(y)

    @staticmethod
    def LosujTyp():
        typy = [
            TypOrganizmu.ANTYLOPA,
            TypOrganizmu.BARSZCZ_SOSNOWSKIEGO,
            TypOrganizmu.GUARANA,
            TypOrganizmu.LIS,
            TypOrganizmu.MLECZ,
            TypOrganizmu.OWCA,
            TypOrganizmu.TRAWA,
            TypOrganizmu.WILCZE_JAGODY,
            TypOrganizmu.WILK,
            TypOrganizmu.CYBER_OWCA,
            TypOrganizmu.ZOLW
        ]
        tmp = random.randint(0, Organizm.LICZBA_ROZNYCH_GATUNKOW - 2)  # BEZ CZLOWIEKA
        return typy[tmp]

    def LosujDowolnePole(self, pozycja):
        self.OdblokujWszystkieKierunki()
        pozX = pozycja.getX()
        pozY = pozycja.getY()
        sizeX = self.swiat.getSizeX()
        sizeY = self.swiat.getSizeY()
        ileKierunkowMozliwych = 0

        if pozX == 0:
            self.ZablokujKierunek(Kierunek.LEWO)
        else:
            ileKierunkowMozliwych += 1

        if pozX == sizeX - 1:
            self.ZablokujKierunek(Kierunek.PRAWO)
        else:
            ileKierunkowMozliwych += 1

        if pozY == 0:
            self.ZablokujKierunek(Kierunek.GORA)
        else:
            ileKierunkowMozliwych += 1

        if pozY == sizeY - 1:
            self.ZablokujKierunek(Kierunek.DOL)
        else:
            ileKierunkowMozliwych += 1

        if ileKierunkowMozliwych == 0:
            return pozycja

        while True:
            tmpLosowanie = random.randint(0, 99)
            # RUCH W LEWO
            if tmpLosowanie < 25 and not self.CzyKierunekZablokowany(Kierunek.LEWO):
                return Punkt(pozX - 1, pozY)
            # RUCH W PRAWO
            elif 25 <= tmpLosowanie < 50 and not self.CzyKierunekZablokowany(Kierunek.PRAWO):
                return Punkt(pozX + 1, pozY)
            # RUCH W GORE
            elif 50 <= tmpLosowanie < 75 and not self.CzyKierunekZablokowany(Kierunek.GORA):
                return Punkt(pozX, pozY - 1)
            # RUCH W DOL
            elif tmpLosowanie >= 75 and not self.CzyKierunekZablokowany(Kierunek.DOL):
                return Punkt(pozX, pozY + 1)

    def LosujPoleNiezajete(self, pozycja):
        self.OdblokujWszystkieKierunki()
        pozX = pozycja.getX()
        pozY = pozycja.getY()
        sizeX = self.swiat.getSizeX()
        sizeY = self.swiat.getSizeY()
        ileKierunkowMozliwych = 0

        if pozX == 0:
            self.ZablokujKierunek(Kierunek.LEWO)
        else:
            if not self.swiat.CzyPoleJestZajete(Punkt(pozX - 1, pozY)):
                ileKierunkowMozliwych += 1
            else:
                self.ZablokujKierunek(Kierunek.LEWO)

        if pozX == sizeX - 1:
            self.ZablokujKierunek(Kierunek.PRAWO)
        else:
            if not self.swiat.CzyPoleJestZajete(Punkt(pozX + 1, pozY)):
                ileKierunkowMozliwych += 1
            else:
                self.ZablokujKierunek(Kierunek.PRAWO)

        if pozY == 0:
            self.ZablokujKierunek(Kierunek.GORA)
        else:
            if not self.swiat.CzyPoleJestZajete(Punkt(pozX, pozY - 1)):
                ileKierunkowMozliwych += 1
            else:
                self.ZablokujKierunek(Kierunek.GORA)

        if pozY == sizeY - 1:
            self.ZablokujKierunek(Kierunek.DOL)
        else:
            if not self.swiat.CzyPoleJestZajete(Punkt(pozX, pozY + 1)):
                ileKierunkowMozliwych += 1
            else:
                self.ZablokujKierunek(Kierunek.DOL)

        if ileKierunkowMozliwych == 0:
            return Punkt(pozX, pozY)

        while True:
            tmpLosowanie = random.randint(0, 99)
            # RUCH W LEWO
            if tmpLosowanie < 25 and not self.CzyKierunekZablokowany(Kierunek.LEWO):
                return Punkt(pozX - 1, pozY)
            # RUCH W PRAWO
            elif 25 <= tmpLosowanie < 50 and not self.CzyKierunekZablokowany(Kierunek.PRAWO):
                return Punkt(pozX + 1, pozY)
            # RUCH W GORE
            elif 50 <= tmpLosowanie < 75 and not self.CzyKierunekZablokowany(Kierunek.GORA):
                return Punkt(pozX, pozY - 1)
            # RUCH W DOL
            elif tmpLosowanie >= 75 and not self.CzyKierunekZablokowany(Kierunek.DOL):
                return Punkt(pozX, pozY + 1)

    def ZablokujKierunek(self, kierunek):
        self.kierunek[kierunek.value] = False

    def OdblokujKierunek(self, kierunek):
        self.kierunek[kierunek.value] = True

    def OdblokujWszystkieKierunki(self):
        self.OdblokujKierunek(Kierunek.LEWO)
        self.OdblokujKierunek(Kierunek.PRAWO)
        self.OdblokujKierunek(Kierunek.GORA)
        self.OdblokujKierunek(Kierunek.DOL)

    def CzyKierunekZablokowany(self, kierunek):
        return not self.kierunek[kierunek.value]

    def getSila(self):
        return self.sila

    def getInicjatywa(self):
        return self.inicjatywa

    def getTuraUrodzenia(self):
        return self.turaUrodzenia

    def getCzyUmarl(self):
        return self.czyUmarl

    def getCzyRozmnazalSie(self):
        return self.czyRozmnazalSie

    def getSwiat(self):
        return self.swiat

    def getPozycja(self):
        return self.pozycja

    def getTypOrganizmu(self):
        return self.typOrganizmu

    def setSila(self, sila):
        self.sila = sila

    def setInicjatywa(self, inicjatywa):
        self.inicjatywa = inicjatywa

    def setTuraUrodzenia(self, turaUrodzenia):
        self.turaUrodzenia = turaUrodzenia

    def setCzyUmarl(self, czyUmarl):
        self.czyUmarl = czyUmarl

    def setCzyRozmnazalSie(self, czyRozmnazalSie):
        self.czyRozmnazalSie = czyRozmnazalSie

    def setSwiat(self, swiat):
        self.swiat = swiat

    def setPozycja(self, pozycja):
        self.pozycja = pozycja

    def setTypOrganizmu(self, typOrganizmu):
        self.typOrganizmu = typOrganizmu

    def getKolor(self):
        return self.kolor

    def setKolor(self, kolor):
        self.kolor = kolor

    def getSzansaRozmnazania(self):
        return self.szansaRozmnazania

    def setSzansaRozmnazania(self, szansaRozmnazania):
        self.szansaRozmnazania = szansaRozmnazania