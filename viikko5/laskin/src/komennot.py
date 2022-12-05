#Syötteen validointi jokaisessa luokassa erikseen, jotta erilaiset komennot
#voivat käsitellä syötettä ja palautua virheestä eri tavoilla.
#Esim. summalle neutraali alkio on 0, mutta mahd. kertolaskulle 1

class Summa:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo

    def suorita(self):
        arvo = 0
        try:
            arvo = int(self._lue_arvo())
        except Exception:
            pass
        self._sovellus.plus(arvo)

class Erotus:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo

    def suorita(self):
        arvo = 0
        try:
            arvo = int(self._lue_arvo())
        except Exception:
            pass
        self._sovellus.miinus(arvo)

class Nollaus:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo

    def suorita(self):
        self._sovellus.nollaa()

class Kumoa:
    def __init__(self, sovellus, lue_arvo):
        self._sovellus = sovellus
        self._lue_arvo = lue_arvo

    def suorita(self):
        pass

class Tuntematon:
    def suorita(self):
        pass
