import random
from Organizm import TypOrganizmu
from Organizm import Organizm
from Punkt import Punkt
import FabrykaOrganizmow
import Umiejetnosc
from Komentator import Komentator
from zwierzeta import Czlowiek

class Swiat:
    def __init__(self, sizeX, sizeY, swiatGUI=None):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.numerTury = 0
        self.czyCzlowiekZyje = True
        self.czyJestKoniecGry = False
        self.pauza = True
        self.plansza = [[None for _ in range(sizeX)] for _ in range(sizeY)]
        self.organizmy = []
        self.swiatGUI = swiatGUI

    def ZapiszSwiat(self, nazwaPliku):
        try:
            with open(nazwaPliku + ".txt", "w") as file:
                file.write(f"{self.sizeX} {self.sizeY} {self.numerTury} {self.czyCzlowiekZyje} {self.czyJestKoniecGry}\n")
                for o in self.organizmy:
                    line = f"{o.getTypOrganizmu()} {o.getPozycja().getX()} {o.getPozycja().getY()} {o.getSila()} {o.getTuraUrodzenia()} {o.getCzyUmarl()}"
                    if o.getTypOrganizmu() == TypOrganizmu.CZLOWIEK:
                        czl = o
                        line += f" {czl.getUmiejetnosc().getCzasTrwania()} {czl.getUmiejetnosc().getCooldown()} {czl.getUmiejetnosc().getCzyJestAktywna()} {czl.getUmiejetnosc().getCzyMoznaAktywowac()}"
                    file.write(line + "\n")
        except IOError as e:
            print("Error:", e)

    @staticmethod
    def WczytajSwiat(nameOfFile):
        try:
            nameOfFile += ".txt"
            file = open(nameOfFile, "r")

            line = file.readline()
            line = line.rstrip()
            properties = line.split(" ")
            sizeX = int(properties[0])
            sizeY = int(properties[1])
            tmpSwiat = Swiat(sizeX, sizeY)
            numerTury = int(properties[2])
            tmpSwiat.numerTury = numerTury
            czyCzlowiekZyje = bool(properties[3])
            tmpSwiat.czyCzlowiekZyje = czyCzlowiekZyje

            if properties[4] == "True":
                czyJestKoniecGry = 1
            else:
                czyJestKoniecGry = 0
            tmpSwiat.czlowiek = None

            for line in file.readlines():
                line = line.rstrip()  # Usunięcie znaku końca linii
                properties = line.split(" ")
                typOrganizmu = TypOrganizmu[properties[0].split(".")[1]]
                x = int(properties[1])
                y = int(properties[2])

                tmpOrganizm = FabrykaOrganizmow.StworzNowyOrganizm(typOrganizmu, tmpSwiat, Punkt(x, y))
                sila = int(properties[3])
                tmpOrganizm.setSila(sila)
                turaUrodzenia = int(properties[4])
                tmpOrganizm.setTuraUrodzenia(turaUrodzenia)
                if properties[5] == "True":
                    czyUmarl = 1
                else:
                    czyUmarl = 0
                tmpOrganizm.setCzyUmarl(czyUmarl)

                if typOrganizmu == TypOrganizmu.CZLOWIEK:
                    tmpSwiat.czlowiek = tmpOrganizm
                    czasTrwania = int(properties[6])
                    tmpSwiat.czlowiek.getUmiejetnosc().setCzasTrwania(czasTrwania)
                    cooldown = int(properties[7])
                    tmpSwiat.czlowiek.getUmiejetnosc().setCooldown(cooldown)
                    czyJestAktywna = bool(properties[8])
                    tmpSwiat.czlowiek.getUmiejetnosc().setCzyJestAktywna(czyJestAktywna)
                    if properties[9] == "True":
                        czyMoznaAktywowac = 1
                    else:
                        czyMoznaAktywowac = 0
                    tmpSwiat.czlowiek.getUmiejetnosc().setCzyMoznaAktywowac(czyMoznaAktywowac)

                tmpSwiat.DodajOrganizm(tmpOrganizm)

            file.close()
            return tmpSwiat
        except IOError as e:
            print("Error:", e)
        return None

    def GenerujSwiat(self, zapelnienieSwiata):
        liczbaOrganizmow = int(self.sizeX * self.sizeY * zapelnienieSwiata)
        # DODAWANIE CZLOWIEKA
        pozycja = self.WylosujWolnePole()
        tmpOrganizm = FabrykaOrganizmow.StworzNowyOrganizm(TypOrganizmu.CZLOWIEK, self, pozycja)
        self.DodajOrganizm(tmpOrganizm)
        self.czlowiek = tmpOrganizm
        # DODAWANIE POZOSTALYCH ORGANIZMOW
        for i in range(liczbaOrganizmow - 1):
            pozycja = self.WylosujWolnePole()
            if pozycja != Punkt(-1, -1):
                self.DodajOrganizm(FabrykaOrganizmow.StworzNowyOrganizm(Organizm.LosujTyp(), self, pozycja))
            else:
                return

    def WykonajTure(self):
        if self.czyJestKoniecGry:
            return
        self.numerTury += 1
        Komentator.DodajKomentarz("\nTURA " + str(self.numerTury))
        print(self.numerTury)
        print(str(len(self.organizmy)) + "\n")
        self.SortujOrganizmy()
        for organizm in self.organizmy:
            if organizm.getTuraUrodzenia() != self.numerTury and not organizm.getCzyUmarl():
                organizm.Akcja()
        i = 0
        while i < len(self.organizmy):
            if self.organizmy[i].getCzyUmarl():
                self.organizmy.pop(i)
            else:
                i += 1
        for organizm in self.organizmy:
            organizm.setCzyRozmnazalSie(False)

    def SortujOrganizmy(self):
        self.organizmy.sort(key=lambda o: (o.getInicjatywa(), o.getTuraUrodzenia()), reverse=True)

    def WylosujWolnePole(self):
        rand = random.Random()
        wolnePola = []
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                if self.plansza[i][j] is None:
                    wolnePola.append(Punkt(j, i))
        if not wolnePola:
            return Punkt(-1, -1)
        return wolnePola[rand.randint(0, len(wolnePola) - 1)]

    def CzyPoleJestZajete(self, pole):
        return self.plansza[pole.y][pole.x] is not None

    def CoZnajdujeSieNaPolu(self, pole):
        return self.plansza[pole.y][pole.x]

    def DodajOrganizm(self, organizm):
        self.organizmy.append(organizm)
        pozycja = organizm.getPozycja()
        self.plansza[pozycja.y][pozycja.x] = organizm

    def UsunOrganizm(self, organizm):
        pozycja = organizm.getPozycja()
        self.plansza[pozycja.y][pozycja.x] = None
        organizm.setCzyUmarl(True)
        if organizm.getTypOrganizmu() == TypOrganizmu.CZLOWIEK:
            self.czyCzlowiekZyje = False
            self.czlowiek = None

    def getSizeX(self):
        return self.sizeX

    def getSizeY(self):
        return self.sizeY

    def getNumerTury(self):
        return self.numerTury

    def getPlansza(self):
        return self.plansza

    def setPlansza(self, plansza):
        self.plansza = plansza

    def getCzyCzlowiekZyje(self):
        return self.czyCzlowiekZyje

    def getCzyJestKoniecGry(self):
        return self.czyJestKoniecGry

    def getOrganizmy(self):
        return self.organizmy

    def getCzlowiek(self):
        return self.czlowiek

    def setCzlowiek(self, czlowiek):
        self.czlowiek = czlowiek

    def setCzyCzlowiekZyje(self, czyCzlowiekZyje):
        self.czyCzlowiekZyje = czyCzlowiekZyje

    def setCzyJestKoniecGry(self, czyJestKoniecGry):
        self.czyJestKoniecGry = czyJestKoniecGry

    def isPauza(self):
        return self.pauza

    def setPauza(self, pauza):
        self.pauza = pauza

    def getSwiatGUI(self):
        return self.swiatGUI

    def setSwiatGUI(self, swiatGUI):
        self.swiatGUI = swiatGUI

    def czyIstniejeBarszczSosnowskiego(self):
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                if self.plansza[i][j] is not None and self.plansza[i][j].getTypOrganizmu() == TypOrganizmu.BARSZCZ_SOSNOWSKIEGO:
                    return True
        return False