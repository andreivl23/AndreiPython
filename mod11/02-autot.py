from random import randint


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

    def kulje(self, tunnit, nopeus):
        self.matka += nopeus * tunnit
        return


class Electric(Auto):
    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Combustion(Auto):
    def __init__(self, rekkari, huippunopeus, bensatanki):
        super().__init__(rekkari, huippunopeus)
        self.bensatanki = bensatanki


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

    sahkoauto1 = Electric("ABC-15", 180, 52.5)
    auto1 = Combustion("ACD-123", 165, 32.3)

    autot.append(sahkoauto1)
    autot.append(auto1)

    kilpailu1 = Kilpailu("Kilpailu", 500, autot)

    for i in range(len(autot)):
        autot[i].kulje(3, randint(50, 100))

    kilpailu1.printstatus()


if __name__ == '__main__':
    main()
