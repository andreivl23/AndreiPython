import random

satu_numero = ""
kokonum = ""


def randomi():
    return random.randint(0, 9)


def randomi_1_6():
    return random.randint(1, 6)


for i in range(3):
    satu_numero = randomi()
    kokonum += str(satu_numero)


print(kokonum)
kokonum = ""

for i in range(4):
    satu_numero = randomi_1_6()
    kokonum += str(satu_numero)

print(kokonum)
