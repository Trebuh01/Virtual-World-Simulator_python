from Roslina import Roslina
import Organizm
import Punkt
from enum import Enum
import Swiat
from Organizm import TypOrganizmu
class Trawa(Roslina):
    SILA = 0
    INICJATYWA = 0

    def __init__(self, swiat: Swiat, pozycja: Punkt, turaUrodzenia: int):
        super().__init__(TypOrganizmu.TRAWA, swiat, pozycja, turaUrodzenia, Trawa.SILA, Trawa.INICJATYWA)
        self.kolor = "#00ff00"

    def TypOrganizmuToString(self) -> str:
        return "Trawa"