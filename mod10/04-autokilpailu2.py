from random import randint
from time import sleep

class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, kiihdytys):
        self.nopeus += kiihdytys
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0
        return

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        return


class Kilpailu:

    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        tunnit = 0
        while not self.kilpailu_ohi():
            tunnit += 1
            for i in range(len(self.autot)):
                self.autot[i].kiihdyta(randint(-10, 15))
                self.autot[i].kulje(1)
            if tunnit == 10:
                self.printstatus()
                tunnit = 0

    def kilpailu_ohi(self):
        for i in range(len(self.autot)):
            if self.autot[i].matka >= self.pituus:
                return True
        return False

    def printstatus(self):
        print("\nRekkari :: Ajettu etäisyys :: Huippunopeus")
        for i in range(len(self.autot)):
            print(f"{self.autot[i].rekkari} ::::::::: {self.autot[i].matka} km :::: {self.autot[i].huippunopeus} km/h")

def main():
    autot = []
    for i in range(10):
        auto = Auto(f"ABC-{i + 1}", randint(100, 200))
        autot.append(auto)

    ralli = Kilpailu("Suuri Romuralli", 8000, autot)
    print(ralli.nimi + " aloitetaan kohta!")
    sleep(2)
    ralli.tunti_kuluu()
    ralli.printstatus()

if __name__ == '__main__':
    main()