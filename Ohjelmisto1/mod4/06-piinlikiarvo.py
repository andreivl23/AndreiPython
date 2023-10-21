import random

N = int(input("Montako kertoja?: "))
n = kierros = x = y = 0

while kierros != N:

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    kierros += 1
    if x ** 2 + y ** 2 < 1 == True:
        n += 1

print((4 * n / N))
