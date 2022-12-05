#Syötteen validointi jokaisessa luokassa erikseen, jotta erilaiset komennot
#voivat käsitellä syötettä ja palautua virheestä eri tavoilla.
#Esim. summalle neutraali alkio on 0, mutta mahd. kertolaskulle 1

class Summa:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo
        self._arvo = 0

    def suorita(self):
        self._arvo = 0
        try:
            self._arvo = int(self._lue_arvo())
        except Exception:
            pass
        self._sovellus.plus(self._arvo)

    def kumoa(self):
        self._sovellus.miinus(self._arvo)
        self._arvo = 0

class Erotus:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo
        self._arvo = 0

    def suorita(self):
        self._arvo = 0
        try:
            self._arvo = int(self._lue_arvo())
        except Exception:
            pass
        self._sovellus.miinus(self._arvo)

    def kumoa(self):
        self._sovellus.plus(self._arvo)
        self._arvo = 0

class Nollaus:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._vanha_arvo = 0

    def suorita(self):
        self._vanha_arvo = self._sovellus.tulos
        self._sovellus.nollaa()

    def kumoa(self):
        self._sovellus.plus(self._vanha_arvo)
        self._vanha_arvo = 0

class Kumoa:
    def __init__(self, sovellus, edellinen_komento):
        self._sovellus = sovellus
        self._kumottava_komento = edellinen_komento

    def suorita(self):
        self._kumottava_komento.kumoa()

class Tuntematon:
    def suorita(self):
        pass

    def kumoa(self):
        pass
