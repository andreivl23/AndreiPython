vuosi = int(input("Vuosi?: "))

if (vuosi % 100) == 0 and (vuosi % 400) == 0:
    print("Karkausvuosi 100!")
elif (vuosi % 4) == 0 and (vuosi % 100) != 0:
    print("Karkausvuosi!")

else:
    print("Ei karkausvuosi")