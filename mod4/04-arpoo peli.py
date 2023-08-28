import random

luku = random.randint(1,10)
arvaus = int(input("Arvaa numero 1-10: "))
while arvaus != luku:
    if arvaus > luku:
        print("Liian suuri arvaus")
    if arvaus < luku:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa numero 1-10: "))
print("Oikein!")