from Zwierze import Zwierze
from Organizm import TypOrganizmu
import colorsys
class Wilk(Zwierze):
    ZASIEG_RUCHU = 1
    SZANSA_WYKONYWANIA_RUCHU = 1
    SILA = 9
    INICJATYWA = 5

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.WILK, swiat, pozycja, turaUrodzenia, Wilk.SILA, Wilk.INICJATYWA)
        self.setZasiegRuchu(Wilk.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(Wilk.SZANSA_WYKONYWANIA_RUCHU)
        self.setKolor("#40e0d0")

    def TypOrganizmuToString(self):
        return "Wilk"