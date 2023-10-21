'''
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
'''

def pizza(halk,hinta):

    pizzahinta = hinta / ((halk/100)** 2/2  * 3.14159)
    return pizzahinta
def main():

    for i in range(2):
        halk = int(input(f"Anna {i+1}. pizan halkaisija sentteinä: "))
        hinta = int(input(f"Anna {i+1}. pizan hinta: "))
        if i == 0:
            pizzahinta1 = pizza(halk,hinta)
        if i == 1:
            pizzahinta2 = pizza(halk,hinta)

    if pizzahinta1 > pizzahinta2:
        print(f"Toinen pizza antaa paremman vastineen rahalle hinnalla {pizzahinta2:.2f}€/m2 (Ensimmäinen pizza on {pizzahinta1:.2f}€/m2)")
    elif pizzahinta2 > pizzahinta1:
        print(f"Ensimmäinen pizza antaa paremman vastineen rahalle hinnalla {pizzahinta1:.2f}€/m2 (Toinen pizza on {pizzahinta2:.2f}€/m2)")

main()