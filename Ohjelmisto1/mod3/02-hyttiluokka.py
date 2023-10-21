print("1) LUX\n2) A\n3) B\n4) C")
valinta = input("Valitse hyttiluokan: ")


if valinta == "1" or valinta == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif valinta == "2" or valinta == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif valinta == "3" or valinta == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif valinta == "4" or valinta == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")

