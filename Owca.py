from Zwierze import Zwierze
from Organizm import TypOrganizmu
class Owca(Zwierze):
    ZASIEG_RUCHU = 1
    SZANSA_WYKONYWANIA_RUCHU = 1
    SILA = 4
    INICJATYWA = 4

    def __init__(self, swiat, pozycja, turaUrodzenia):
        super().__init__(TypOrganizmu.OWCA, swiat, pozycja, turaUrodzenia, Owca.SILA, Owca.INICJATYWA)
        self.setZasiegRuchu(Owca.ZASIEG_RUCHU)
        self.setSzansaWykonywaniaRuchu(Owca.SZANSA_WYKONYWANIA_RUCHU)
        self.setKolor("#8b4513")

    def TypOrganizmuToString(self):
        return "Owca"