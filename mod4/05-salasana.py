user = input("Anna käyttäjätunnuksesi: ")
password = input("Anna salasana: ")
kertoja = 0

while kertoja != 5:

    if user == "python" and password == "rules":
        print("Tervetuloa!")
        break
    else:
        user = input("Anna käyttäjätunnuksesi: ")
        password = input("Anna salasana: ")
        kertoja += 1

if kertoja == 5:
    print("Pääsy evätty.")