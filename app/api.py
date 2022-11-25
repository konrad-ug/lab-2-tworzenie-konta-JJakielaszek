from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto
import json

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify("Konto stworzone"), 201

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return f'Ilość kont w rejestrze {RejestrKont.how_many()}', 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f'Request o konto z peselem: {pesel}')
    konto = RejestrKont.search_account(pesel)
    print(konto)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel), 200