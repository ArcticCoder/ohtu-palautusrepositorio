KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.alkio_taulu = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.alkio_taulu[i]:
                return True
        return False

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.alkio_taulu[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            self._kasvata_tarvittaessa()
            return True
        return False

    def lisaa_taulu(self, taulu):
        for alkio in taulu:
            self.lisaa(alkio)

    def poista(self, n):
        poistettava_indeksi = -1
        for i in range(0, self.alkioiden_lkm):
            if n == self.alkio_taulu[i]:
                poistettava_indeksi = i
                break

        if poistettava_indeksi != -1:
            self.alkioiden_lkm = self.alkioiden_lkm - 1

            for i in range(poistettava_indeksi, self.alkioiden_lkm):
                self.alkio_taulu[i] = self.alkio_taulu[i + 1]

            return True

        return False

    def poista_taulu(self, taulu):
        for alkio in taulu:
            self.poista(alkio)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def joukko_tauluksi(self):
        return [self.alkio_taulu[i] for i in range(0, self.alkioiden_lkm)]

    @staticmethod
    def yhdiste(a, b):
        yhdiste_joukko = IntJoukko()
        a_taulu = a.joukko_tauluksi()
        b_taulu = b.joukko_tauluksi()

        yhdiste_joukko.lisaa_taulu(a_taulu)
        yhdiste_joukko.lisaa_taulu(b_taulu)

        return yhdiste_joukko

    @staticmethod
    def leikkaus(a, b):
        leikkaus_joukko = IntJoukko()
        a_taulu = a.joukko_tauluksi()
        b_taulu = b.joukko_tauluksi()

        leikkaus_taulu = [alkio for alkio in a_taulu if alkio in b_taulu]
        leikkaus_joukko.lisaa_taulu(leikkaus_taulu)

        return leikkaus_joukko

    @staticmethod
    def erotus(a, b):
        erotus_joukko = IntJoukko()
        a_taulu = a.joukko_tauluksi()
        b_taulu = b.joukko_tauluksi()

        erotus_joukko.lisaa_taulu(a_taulu)
        erotus_joukko.poista_taulu(b_taulu)

        return erotus_joukko

    def _kasvata_tarvittaessa(self):
        if self.alkioiden_lkm == len(self.alkio_taulu):
            self.alkio_taulu = self.alkio_taulu  + ([0] * self.kasvatuskoko)

    def __str__(self):
        str_taulu = [str(alkio) for alkio in self.joukko_tauluksi()]
        tuotos = "{" + ", ".join(str_taulu) + "}"
        return tuotos
