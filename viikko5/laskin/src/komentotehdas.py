import komennot


class Komentotehdas:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo 
        self._edellinen_komento = None

        self._komennot = {
                "summa": komennot.Summa(self._sovellus, self._lue_arvo),
                "erotus": komennot.Erotus(self._sovellus, self._lue_arvo),
                "nollaus": komennot.Nollaus(self._sovellus, self._lue_arvo),
                }

    def hae(self, komento):
        if komento in self._komennot:
            komento_olio = self._komennot[komento]
        elif komento == "kumoa":
            return komennot.Kumoa(self._sovellus, self._edellinen_komento)
        else:
            komento_olio = komennot.Tuntematon()

        self._edellinen_komento = komento_olio
        return komento_olio
