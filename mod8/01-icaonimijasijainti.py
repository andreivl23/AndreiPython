import mysql.connector

yhteys = mysql.connector.connect(
         host='172.232.129.9',
         port= 3306,
         database='flight_game',
         user='guest',
         password='Dmentors',
         autocommit=True
         )
def haeICAO(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"\nLentoaseman nimi on {rivi[0]} ja se on sijaintikunnassa {rivi[1]}")
    return

def main():

    icao = input("Anna lentokentän ICAO: ")
    haeICAO(icao)


main()