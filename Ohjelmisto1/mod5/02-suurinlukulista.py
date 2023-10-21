syote = input("Anna luku: ")
lista = []

while syote != "":
    syote = int(syote)
    lista.append(syote)
    syote = input("Anna luku: ")

#sorted(lista, reverse=True)
lista.sort(reverse=True)

for luku in lista[0:5]:
    print(luku, end=" ")

#print(lista[0:5])

print("\nLopetetaan")