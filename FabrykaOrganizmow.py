
import Organizm
from rosliny.Guarana import Guarana
from rosliny.BarszczSosnowskiego import BarszczSosnowskiego
from rosliny.Mlecz import Mlecz
from rosliny.Trawa import Trawa
from rosliny.WilczeJagody import WilczeJagody
from zwierzeta.Antylopa import Antylopa
from zwierzeta.CyberOwca import CyberOwca
from zwierzeta.Czlowiek import Czlowiek
from zwierzeta.Lis import Lis
from zwierzeta.Owca import Owca
from zwierzeta.Wilk import Wilk
from zwierzeta.Zolw import Zolw
def StworzNowyOrganizm(typ_organizmu, swiat, pozycja):
    numer_tury = swiat.getNumerTury()

    if typ_organizmu == Organizm.TypOrganizmu.WILK:
        return Wilk(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.OWCA:
        return Owca(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.LIS:
        return Lis(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.ZOLW:
        return Zolw(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.ANTYLOPA:
        return Antylopa(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.CZLOWIEK:
        return Czlowiek(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.TRAWA:
        return Trawa(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.MLECZ:
        return Mlecz(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.GUARANA:
        return Guarana(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.WILCZE_JAGODY:
        return WilczeJagody(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.BARSZCZ_SOSNOWSKIEGO:
        return BarszczSosnowskiego(swiat, pozycja, numer_tury)
    elif typ_organizmu == Organizm.TypOrganizmu.CYBER_OWCA:
        return CyberOwca(swiat, pozycja, numer_tury)
    else:
        return None
