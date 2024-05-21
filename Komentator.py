class Komentator:
    tekst = ""
    @staticmethod
    def DodajKomentarz(komentarz):
        Komentator.tekst += komentarz + "\n"

    @staticmethod
    def getTekst():
        return Komentator.tekst

    @staticmethod
    def CzyszczenieKomentarzy():
        Komentator.tekst = ""
