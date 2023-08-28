leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luoti: "))

naulat = leiviska * 20 + naula
luotit = naulat * 32 + luoti
grammat = luotit * 13.3
#kilogrammat = grammat // 1000  # double slash gives the whole number
#grammaa = grammat % 1000  # % gives remainder after division

# print("Massa on", kilogrammat, "kilogrammaa ja", int(grammaa), "grammaa")
print(f"Massa on {grammat // 1000} kilogrammaa ja {grammat % 1000:.0f} grammaa")
print("Oikea tulos grammoissa: ", grammat)
