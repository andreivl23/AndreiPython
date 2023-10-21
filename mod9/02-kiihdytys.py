class Auto:
    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, kiihdytys):
        self.nopeus += kiihdytys
        if self.nopeus > 142:
            self.nopeus = 142
        if self.nopeus < 0:
            self.nopeus = 0
        return

auto1 = Auto("ABC-123", "142 km/h")
print(f"Auton rekkari on {auto1.rekkari} ja huippunopeus on {auto1.huippunopeus}")
print("Kiihdytään...")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"Auton nopeus on {auto1.nopeus} km/h")
print("Jarrutaan...")
auto1.kiihdyta(-200)
print(f"Auton nopeus on {auto1.nopeus} km/h")

