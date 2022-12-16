from peli_tehdas import PeliTehdas


def main():
    while True:
        pelityyppi = PeliTehdas.valitse_pelityyppi()
        peli = PeliTehdas.luo_peli(pelityyppi)

        if not peli:
            break

        print("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
        peli.pelaa()


if __name__ == "__main__":
    main()
