import requests
import json

apikey = ""

kaupunki = input("Kirjoita kaupunki: ")


geopyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=1&appid={apikey}"
vastaus1 = requests.get(geopyynto)
lat = vastaus1.json()[0]["lat"]
lon = vastaus1.json()[0]["lon"]

weatherpyynto = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&lang=fi&appid={apikey}"

try:
    vastaus2 = requests.get(weatherpyynto)
    #print(vastaus)
    if vastaus2.status_code == 200:
        json_vastaus = vastaus2.json()
        # print(json.dumps(json_vastaus, indent=2))

        weather = json_vastaus["weather"][0]["description"]
        temp_kelvin = int(json_vastaus["main"]["temp"])
        # 0K − 273.15 = -273,1°C
        temp_cels = temp_kelvin - 273.15
        print(f"Lämpötila on {temp_cels:.1f}C ja sää on {weather}")

except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
