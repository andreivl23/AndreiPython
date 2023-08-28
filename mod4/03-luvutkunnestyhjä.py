
syote = input("Anna luku: ")
luku_max = syote
luku_min = syote

while syote != "":

    if int(syote) > int(luku_max):
        luku_max = int(syote)
#        print(luku_max)
    if int(syote) < int(luku_min):
        luku_min = int(syote)
#        print(luku_min)

    print("Annettu luku on: " + syote)
    syote = input("Anna luku: ")

print(f"\nPienin luku oli {luku_min} ja suurin oli {luku_max}")