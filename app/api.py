from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.Konto import Konto
import json

app = Flask(__name__)

@app.route("/konta/stworz_konto", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    isValid = RejestrKont.search_account(dane["pesel"])
    if (isValid != None):
        return jsonify("Istnieje konto o pdanym peselu! "), 400
    else:
        konto = Konto(dane["imie"], dane["nazwisko"], dane["pesel"])
        RejestrKont.add_account(konto)
        return jsonify("Konto stworzone"), 201
        

@app.route("/konta/ile_kont", methods=['GET'])
def ile_kont():
    return jsonify(f'Ilość kont w rejestrze {RejestrKont.how_many()}'), 200

@app.route("/konta/konto/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    print(f'Request o konto z peselem: {pesel}')
    konto = RejestrKont.search_account(pesel)
    print(konto)
    return jsonify(imie=konto.imie, nazwisko=konto.nazwisko, pesel=konto.pesel, saldo=konto.saldo), 200

@app.route("/konta/konto/<pesel>", methods=['PUT'])
def update_account(pesel):
    dane = request.get_json()
    print(f"Request o update konta z danymi: {dane}")
    konto = RejestrKont.search_account(pesel)
    print("Konto znalezione")
    konto.imie = dane["imie"] if "imie" in dane else konto.imie
    konto.nazwisko = dane["nazwisko"] if "nazwisko" in dane else konto.nazwisko
    konto.pesel = dane["pesel"] if "pesel" in dane else konto.pesel
    konto.saldo = dane["saldo"] if "saldo" in dane else konto.saldo
    return jsonify("Konto zaktualizowane"), 200

@app.route("/konta/konto/<pesel>", methods=['DELETE'])
def delete_account(pesel):
    dane = request.get_json()
    print(f"Request o delete konta z peselem: {pesel}")
    konto = RejestrKont.search_account(pesel)
    print("Konto znalezione")
    RejestrKont.registry.remove(konto)
    return jsonify("Konto usunięte pomyślnie"), 200