'''
Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi. Ohjelma kysyy käyttäjältä,
haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
(ICAO-koodi on lentoaseman yksilöivä tunniste.
Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)
'''

def uusilentoasema(lentoasemat):

    nimi = input("Anna lentoaseman nimi: ")
    icao = input("Anna lentoaseman icao: ")
    lentoasemat[icao] = nimi
    return lentoasemat
def main():
    lentoasemat = {}

    valintateksti = """\n1) Lisää uusi lentoasema
2) Hae lentoasema
3) Lopeta\n"""

    while True:
        print(valintateksti)
        valinta = int(input("Mitä haluat tehdä?: "))
        if valinta == 1:
            uusilentoasema(lentoasemat)
        elif valinta == 2:
            icao = input("Anna ICAO: ")
            print(lentoasemat[icao])
        elif valinta == 3:
            print("Lopetetaan.")
            break
        else:
            print("Virhellinen valinta")

main()