import random

arpakuutiot = int(input("Kuinka monta arpakuutioita?: "))
arvo = 0
summa = 0

for i in range(arpakuutiot):
    arvo = random.randint(1,6)
    summa += arvo

print("Summa on", summa)