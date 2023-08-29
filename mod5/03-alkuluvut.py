luku = int(input("Anna luku: "))
lista = [2, 3, 5, 7]

for i in range(4):
    if luku % lista[i] == 0:
        print("Ei alkulukua")
        break

if luku % lista[i] != 0:
    print("Alkuluku!")

print("Lopetetaan")