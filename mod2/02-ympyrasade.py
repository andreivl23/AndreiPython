import math  # lisätään math moduuli

pi_arvo = math.pi  # lisätään math moduulista Pin arvo muutujaan
sade = int(input("Anna ympyrän säde: "))
tulos = sade*pi_arvo
pyor_numero = round(tulos, 2)  # pyöristetään kahden desimaalin tarkkuuteen.
print("Ympyrän pinta ala on:", pyor_numero)
