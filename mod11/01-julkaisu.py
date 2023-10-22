class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta(self):
        print("Julkaisun nimi on " + self.nimi)


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta(self):
        super().tulosta()
        print("Kirjailija: " + self.kirjailija + "\nSivumäärä:", self.sivumaara)


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimitaja):
        super().__init__(nimi)
        self.toimitaja = paatoimitaja

    def tulosta(self):
        super().tulosta()
        print("Päätoimittaja: " + self.toimitaja)


if __name__ == '__main__':
    kirja1 = Kirja("Hytti n:o 6", "Roosa Liksom", 200)
    kirja1.tulosta()
    print()
    lehti1 = Lehti("Aku Ankka", "Aki Hyyppä")
    lehti1.tulosta()
