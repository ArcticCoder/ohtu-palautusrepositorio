import komennot


class Komentotehdas:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo 

        self._komennot = {
                "summa": komennot.Summa(self._sovellus, self._lue_arvo),
                "erotus": komennot.Erotus(self._sovellus, self._lue_arvo),
                "nollaus": komennot.Nollaus(self._sovellus, self._lue_arvo),
                "kumoa": komennot.Kumoa(self._sovellus, self._lue_arvo),
                }

    def hae(self, komento):
        if komento in self._komennot:
            return self._komennot[komento]

        return komennot.Tuntematon()
