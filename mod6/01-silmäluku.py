import random
def noppa():
    silmaluku = random.randint(1,6)
    return silmaluku

silmaluku = noppa()

while silmaluku != 6:

        print(f"Heitetään... Silmäluku on {silmaluku}")
        silmaluku = noppa()


print(f"No niin saatiin silmaluvuksi {silmaluku}.")