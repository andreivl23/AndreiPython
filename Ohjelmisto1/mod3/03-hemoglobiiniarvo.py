hemoglobiini = int(input("Mikä on sinun hemoglobiiniarvosi?: "))
print("1) Nainen\n2) Mies")
sukupuoli = input("Mikä on sinun biologinen sukupuoli?: ")

if sukupuoli == "Nainen" or sukupuoli == "1":
    if hemoglobiini > 117 and hemoglobiini < 175:
        print("Normaali")
    elif hemoglobiini < 117:
        print("Alhainen")
    else:
        print("Korkea")
elif sukupuoli == "Mies" or sukupuoli == "2":
    if hemoglobiini > 134 and hemoglobiini < 195:
        print("Normaali")
    elif hemoglobiini < 134:
        print("Alhainen")
    else:
        print("Korkea")