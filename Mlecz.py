from Roslina import Roslina
import Komentator
from enum import Enum
import random
import Punkt
import Swiat
from Organizm import TypOrganizmu
class Mlecz(Roslina):
    SILA = 0
    INICJATYWA = 0
    ILE_PROB = 3
    def __init__(self, swiat: Swiat, pozycja: Punkt, tura_urodzenia: int):
        super().__init__(TypOrganizmu.MLECZ, swiat, pozycja, tura_urodzenia, Mlecz.SILA, Mlecz.INICJATYWA)
        self.kolor = ("#ffd700")

    def Akcja(self):
        for _ in range(Mlecz.ILE_PROB):
            tmp_losowanie = random.randint(0, 99)
            if tmp_losowanie < self.getSzansaRozmnazania():
                self.Rozprzestrzenianie()

    def TypOrganizmuToString(self):
        return "Mlecz"



