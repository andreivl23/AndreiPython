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

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
        return

autot = []

for i in range(11):
    auto = Auto(f"ABC-{i}", randint(100,200))
    autot.append(auto)

stop = 0

while stop != 1:
    for i in range(10):
        autot[i].kiihdyta(randint(-10,15))
        autot[i].kulje(1)
        if autot[i].matka >= 10000:
            stop = 1

print("Rekkari :: Ajettu etäisyys :: Huippunopeus")
for i in range(10):
    print(f"{autot[i+1].rekkari} ::::::::: {autot[i].matka} km :::: {autot[i].huippunopeus} km/h")