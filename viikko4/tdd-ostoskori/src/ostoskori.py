from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._tuotteet = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        summa = 0
        for _, tuote in self._tuotteet.items():
            summa += tuote.lukumaara()
        return summa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for _, tuote in self._tuotteet.items():
            summa += tuote.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() not in self._tuotteet:
            self._tuotteet[lisattava.nimi()] = Ostos(lisattava)
        else:
            self._tuotteet[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        self._tuotteet[poistettava.nimi()].muuta_lukumaaraa(-1)
        if self._tuotteet[poistettava.nimi()].lukumaara() == 0:
            del self._tuotteet[poistettava.nimi()]

    def tyhjenna(self):
        self._tuotteet = {}
        # tyhjentää ostoskorin

    def ostokset(self):
        return list(self._tuotteet.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
