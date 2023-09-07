import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='123321',
         autocommit=True
         )
def haemaakoodi(maakoodi):
    sql = "SELECT type FROM airport"
    sql += " WHERE iso_country='" + maakoodi + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    mediumfries = smallfries = largefries = helifries = closedfries = 0
    if kursori.rowcount >0 :
        for rivi in tulos:
            if rivi[0] == "small_airport":
                smallfries += 1
            if rivi[0] == "medium_airport":
                mediumfries += 1
            if rivi[0] == "large_airport":
                largefries += 1
            if rivi[0] == "heliport":
                helifries += 1
            if rivi[0] == "closed":
                closedfries += 1
        print(f"Pienet lentokentät: {smallfries}")
        print(f"Keski lentokentät: {mediumfries}")
        print(f"Isot lentokentät: {largefries}")
        print(f"Helikopterikenttät: {helifries}")
        print(f"Suljetut lentokentät: {closedfries}")
    return

def main():

    maakoodi = input("Anna maakoodi: ")
    haemaakoodi(maakoodi)


main()