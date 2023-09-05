'''
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.
'''

kuukaudet = ("Tammikuu","Helmikuu","Maliskuu","Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu","Elokuu","Syyskuu","Lokakuu","Marraskuu","Joulukuu")
kaudet = ("talvi","kevät","kesä","syksy")

kuukausi = int(input("Anna kuukausi numerona: "))

# If is started only if user gave value between 1 and 12
if 1 <= kuukausi <= 12:
    # % 12 gives 0 as an answer if the month is 12th, and 0 is Winter. // gives floored int number. 5/3 = 1,66 5//3 = 1
    kausinumero = (kuukausi % 12) // 3
    kausi = kaudet[kausinumero]
    print(f"{kuukaudet[kuukausi-1]} on {kausi}")