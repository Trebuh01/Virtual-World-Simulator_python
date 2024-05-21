class Umiejetnosc:
    def __init__(self):
        self.CZAS_TRWANIA_UMIEJETNOSCI = 5
        self.COOLDOWN_UMIEJETNOSCI = 10
        self.czyMoznaAktywowac = True
        self.czyJestAktywna = False
        self.czasTrwania = 0
        self.cooldown = 0

    def SprawdzWarunki(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.czasTrwania > 0:
            self.czasTrwania -= 1
        if self.czasTrwania == 0:
            self.Dezaktywuj()
        if self.cooldown == 0:
            self.czyMoznaAktywowac = True

    def Aktywuj(self):
        if self.cooldown == 0:
            self.czyJestAktywna = True
            self.czyMoznaAktywowac = False
            self.cooldown = self.COOLDOWN_UMIEJETNOSCI
            self.czasTrwania = self.CZAS_TRWANIA_UMIEJETNOSCI

    def Dezaktywuj(self):
        self.czyJestAktywna = False

    def getCzyMoznaAktywowac(self):
        return self.czyMoznaAktywowac

    def setCzyMoznaAktywowac(self, czyMoznaAktywowac):
        self.czyMoznaAktywowac = czyMoznaAktywowac

    def getCzyJestAktywna(self):
        return self.czyJestAktywna

    def setCzyJestAktywna(self, czyJestAktywna):
        self.czyJestAktywna = czyJestAktywna

    def getCzasTrwania(self):
        return self.czasTrwania

    def setCzasTrwania(self, czasTrwania):
        self.czasTrwania = czasTrwania

    def getCooldown(self):
        return self.cooldown

    def setCooldown(self, cooldown):
        self.cooldown = cooldown
