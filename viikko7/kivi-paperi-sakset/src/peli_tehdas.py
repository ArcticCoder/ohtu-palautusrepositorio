from kps_pelityypit import KPSPelaajaVsPelaaja, KPSTekoaly, KPSParempiTekoaly

def luo_peli(tyyppi):
    if tyyppi == 'a':
        return KPSPelaajaVsPelaaja()
    if tyyppi == 'b':
        return KPSTekoaly()
    if tyyppi == 'c':
        return KPSParempiTekoaly()

    return None
