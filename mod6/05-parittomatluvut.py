def poisparitomaton(lista):
    lista2 = []
    for i in lista:
        if i % 2 == 0 and i != 0:
            lista2.append(i)
    return lista2

def main():
    lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    lista2 = poisparitomaton(lista)
    print(f"Alkuperäinen lista:\n{lista}\nVain parilliset luvut:\n{lista2}")

main()