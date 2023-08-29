import math, random

x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
pi_arvo = math.pi
sade = 1
N = int(input("Montako kertoja?: "))
n = 0
A_pinta_ala = pi_arvo * sade ** 2
B_pinta_ala = 4 * sade
#ero = B_pinta_ala / A_pinta_ala
yhtalo = x ** 2 + y ** 2 < 1
kertoja = 0

while kertoja != N:

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    yhtalo = x ** 2 + y ** 2 < 1
    kertoja += 1
    if yhtalo == True:
        n += 1

print((4*n/N))