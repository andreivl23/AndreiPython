import mysql.connector
from flask import Flask


app = Flask(__name__)

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port=3306,
         database='flight_game',
         user='root',
         password='123321',
         autocommit=True
         )


def haeicao(icao):
    sql = "SELECT name, municipality FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    name = tulos[0][0]
    municipality = tulos[0][1]
    return name, municipality


@app.route('/kenttä/<icao>')
def getname(icao):
    name, municipality = haeicao(icao)
    vastaus = {
        "ICAO": icao.upper(),
        "Name": name,
        "Municipality": municipality
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
