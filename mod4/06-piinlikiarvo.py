import random

x = random.uniform(-1, 1)
y = random.uniform(-1, 1)
N = int(input("Montako kertoja?: "))
n = 0
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