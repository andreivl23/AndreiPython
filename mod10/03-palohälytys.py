from time import sleep


class Hissi:
    def __init__(self, i, minfloor, maxfloor):
        self.elevatornro = i
        self.min = int(minfloor)
        self.max = int(maxfloor)
        self.floor = int(minfloor)

    def moveto(self, dest):

        if self.floor < dest:
            for i in range(abs(self.floor - dest)):
                self.up()
        if self.floor > dest:
            for i in range(abs(self.floor - dest)):
                self.down()

    def up(self):
        if self.floor < self.max:
            self.floor += 1
            sleep(.4)
            print(f"Elevator N.{self.elevatornro} at floor {self.floor}.")

    def down(self):
        if self.floor > self.min:
            self.floor -= 1
            sleep(.4)
            print(f"Elevator N.{self.elevatornro} at floor {self.floor}.")


class Talo:
    def __init__(self, minfloor, maxfloor, elevators):
        self.elevatorcount = int(elevators)
        self.minfloor = minfloor
        self.maxfloor = maxfloor
        self.elevators = []
        for i in range(int(elevators)):
            self.elevators.append(Hissi(i, int(minfloor), int(maxfloor)))

    def drive(self, elevator, floor):
        self.elevators[elevator].moveto(floor)

    def fire(self):
        print("Fire! Sending elevators down.")
        for i in range(self.elevatorcount):
            self.elevators[i].moveto(self.minfloor)

def main():
    Talo1 = Talo(0, 10, 2)
    Talo1.drive(0, 5)
    Talo1.drive(1, 9)
    Talo1.fire()


main()