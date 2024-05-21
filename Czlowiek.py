from Organizm import TypOrganizmu
from Komentator import Komentator
from Punkt import Punkt
from Organizm import Kierunek
from Zwierze import Zwierze
from Umiejetnosc import Umiejetnosc
class Czlowiek(Zwierze):
    ZASIEG_RUCHU = 1
    SZANSA_WYKONYWANIA_RUCHU = 1
    SILA = 5
    INICJATYWA = 4

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.CZLOWIEK, swiat, pozycja, turaUrodzenia, Czlowiek.SILA, Czlowiek.INICJATYWA)
        self.setZasiegRuchu(Czlowiek.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(Czlowiek.SZANSA_WYKONYWANIA_RUCHU)
        self.kierunekRuchu = Kierunek.BRAK_KIERUNKU
        self.setKolor("#0000ff")
        self.umiejetnosc = Umiejetnosc()

    def specUmiej(self):
        self.setSila(self.getSila() - 1)

    def ZaplanujRuch(self):
        x = self.getPozycja().getX()
        y = self.getPozycja().getY()
        self.LosujDowolnePole(self.getPozycja())  # BLOKUJE KIERUNKI NIEDOZWOLONE PRZY GRANICY SWIATA
        if self.kierunekRuchu == Kierunek.BRAK_KIERUNKU or self.CzyKierunekZablokowany(self.kierunekRuchu):
            return self.getPozycja()
        else:
            if self.kierunekRuchu == Kierunek.GORA:
                return Punkt(x, y - 1)
            elif self.kierunekRuchu == Kierunek.DOL:
                return Punkt(x, y + 1)
            elif self.kierunekRuchu == Kierunek.LEWO:
                return Punkt(x - 1, y)
            elif self.kierunekRuchu == Kierunek.PRAWO:
                return Punkt(x + 1, y)
            else:
                return Punkt(x, y)

    def Akcja(self):
        if self.umiejetnosc.getCzyJestAktywna():
            Komentator.DodajKomentarz(self.OrganizmToString() + " Zwiekszenie sily jest aktywne (Pozostaly czas " + str(self.umiejetnosc.getCzasTrwania()) + " tur)")
        for i in range(self.getZasiegRuchu()):
            przyszlaPozycja = self.ZaplanujRuch()
            if self.getSwiat().CzyPoleJestZajete(przyszlaPozycja) and self.getSwiat().CoZnajdujeSieNaPolu(przyszlaPozycja) != self:
                self.Kolizja(self.getSwiat().CoZnajdujeSieNaPolu(przyszlaPozycja))
                break
            elif self.getSwiat().CoZnajdujeSieNaPolu(przyszlaPozycja) != self:
                self.WykonajRuch(przyszlaPozycja)
            if self.umiejetnosc.getCzyJestAktywna():
                self.specUmiej()
        self.kierunekRuchu = Kierunek.BRAK_KIERUNKU
        self.umiejetnosc.SprawdzWarunki()

    def TypOrganizmuToString(self):
        return "Czlowiek"

    def getUmiejetnosc(self):
        return self.umiejetnosc

    def setKierunekRuchu(self, kierunekRuchu):
        self.kierunekRuchu = kierunekRuchu