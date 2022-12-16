from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, ekan_siirto):
        return input("Toisen pelaajan siirto: ")


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ekan_siirto):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        self._tekoaly.aseta_siirto(ekan_siirto)
        return siirto


class KPSParempiTekoaly(KPSTekoaly):
    def __init__(self):
        self._tekoaly = TekoalyParannettu(10)
