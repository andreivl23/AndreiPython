from time import sleep


class Hissi:
    def __init__(self, min, max):
        self.min = int(min)
        self.max = int(max)
        self.floor = int(min)

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
            print(self.floor)
    def down(self):
        if self.floor > self.min:
            self.floor -= 1
            sleep(.4)
            print(self.floor)


hissi1 = Hissi(0,10)
dest = 0
while not dest < 0:

    dest = int(input("Which floor to go to?: "))
    hissi1.moveto(dest)


