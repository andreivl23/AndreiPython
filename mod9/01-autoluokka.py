class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


auto1 = Auto("ABC-123", "142 km/h")

print(f"Auton rekkari on {auto1.rekkari} ja huippunopeus on {auto1.huippunopeus}")
print(f"Auton nopeus on {auto1.nopeus} km/h ja kuljettu matka on {auto1.matka} km")
