import requests


pyynto = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        # print(json.dumps(json_vastaus, indent=2))

        print("\n"+json_vastaus["value"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")
