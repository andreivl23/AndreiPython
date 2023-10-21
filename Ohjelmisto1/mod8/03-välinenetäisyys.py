import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='123321',
         autocommit=True
         )
def haekoordinatit(icao):

    sql = "SELECT latitude_deg, longitude_deg FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def main():

    icao = input("Anna ICAO: ") #EFHK
    koordinatit1 = haekoordinatit(icao)
    icao = input("Anna toinen ICAO: ") #EETN
    koordinatit2 = haekoordinatit(icao)
    print(koordinatit2,koordinatit1)
    print(f"Etäisyys näiden lentokentien välillä on {distance.distance(koordinatit1,koordinatit2).km:.2f} kilometria.")

main()