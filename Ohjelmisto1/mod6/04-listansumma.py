def laskenta(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa

def main():

    lista = [28419,24142,3231,4342,5345]
    summa = laskenta(lista)
    print(summa)

main()