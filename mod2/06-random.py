import random

def randomi():
    return random.randint(0, 9)

def randomi_1_6():
    return random.randint(1, 6)


yksi = str(randomi())
kaksi = str(randomi())
kolme = str(randomi())

print(yksi+kaksi+kolme)

nelja = str(randomi_1_6())
viisi = str(randomi_1_6())
kuusi = str(randomi_1_6())
seitseman = str(randomi_1_6())

print(nelja+viisi+kuusi+seitseman)