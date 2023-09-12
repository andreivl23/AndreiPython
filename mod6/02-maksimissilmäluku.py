import random
def noppa(tahkoja):
    silmaluku = random.randint(1,tahkoja)
    return silmaluku

def main():

    tahkoja = int(input("Tahkoja: "))
    silmaluku = noppa(tahkoja)

    while silmaluku != tahkoja:

            print(f"Heitetään... Silmäluku on {silmaluku}")
            silmaluku = noppa(tahkoja)


    print(f"No niin saatiin silmaluvuksi {silmaluku}.")

main()