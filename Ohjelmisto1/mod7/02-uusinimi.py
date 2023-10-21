'''
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
yötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä.
Käytä joukkotietorakennetta nimien tallentamiseen.
'''

def nimet(nimi,nimijoukko):

    nimijoukko.add(nimi)
    return nimijoukko

def main():
    nimijoukko = {""}
    nimi = input("Anna nimi: ")
    while nimi != "":
        if not nimi in nimijoukko:
            print("Uusi nimi")
            nimet(nimi,nimijoukko)
        else:
            print("Aiemmin syötetty nimi")
        nimi = input("Anna nimi: ")
    for nimi in nimijoukko:
        print(nimi)
main()