from flask import Flask

app = Flask(__name__)


@app.route('/alkuluku/<luku>')
def check(luku):
    luku = int(luku)
    isprime = True
    lista = [2, 3, 5, 7]
    for i in range(4):
        if luku % lista[i] == 0:
            isprime = False
    vastaus = {
        "luku": luku,
        "isPrime": isprime
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
