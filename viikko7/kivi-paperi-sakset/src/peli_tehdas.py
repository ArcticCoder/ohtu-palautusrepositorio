from kps_pelityypit import KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly

class PeliTehdas():
    @staticmethod
    def valitse_pelityyppi():
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        return input()

    @staticmethod
    def luo_peli(tyyppi):
        if tyyppi == 'a':
            return KPSPelaajaVsPelaaja()
        if tyyppi == 'b':
            return KPSTekoaly()
        if tyyppi == 'c':
            return KPSParempiTekoaly()

        return None
